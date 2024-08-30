import numpy as np

VALENCE_SCORE_TABLE_SIZE = 32
CACHE_FUNCTION_TABLE_SIZE = 32
CACHE_DECAY_POWER = 1.5
LAST_TRI_SCORE = 0.75
VALENCE_BOOST_SCALE = 2.0
VALENCE_BOOST_POWER = 0.5

POSITION_SCORE = (LAST_TRI_SCORE,)*3 + tuple(
    (1 - (i - 3) / (CACHE_FUNCTION_TABLE_SIZE - 3)) ** CACHE_DECAY_POWER
        for i in range(3, CACHE_FUNCTION_TABLE_SIZE))

VALENCE_SCORE = (0,) + tuple(
    (i ** -VALENCE_BOOST_POWER) * VALENCE_BOOST_SCALE
        for i in range(1, VALENCE_SCORE_TABLE_SIZE-1))

def get_vtx_score(num_active_tris, cache_position):
    if num_active_tris == 0:
        return 0

    if cache_position > 0:
        score = POSITION_SCORE[cache_position]
    else:
        score = 0

    if num_active_tris < len(VALENCE_SCORE):
        score += VALENCE_SCORE[num_active_tris]

    return score

def optimize(prims, cache_size):
    tri_indices = [[] for v in range(prims.vertex_count)]
    for idx_idx, idx in enumerate(prims.indices):
        tri_indices[idx >> 2].append(idx_idx//3)

    last_score = [0] * prims.vertex_count
    cache_tag = [0] * prims.vertex_count
    tri_added = set()
    tri_score = [0] * prims.face_count

    for v_idx in range(prims.vertex_count):
        last_score[v_idx] = get_vtx_score(len(tri_indices[v_idx]), cache_tag[v_idx])
        for f_idx in tri_indices[v_idx]:
            tri_score[f_idx] += last_score[v_idx]

    best_triangle = -1
    best_score = -1
    for f_idx in range(prims.face_count):
        if tri_score[f_idx] > best_score:
            best_triangle = f_idx
            best_score = tri_score[f_idx]

    new_indices = np.zeros(prims.indices.shape, prims.indices.dtype)
    new_indices_cursor = 0

    cache = [-1] * (cache_size + 3)
    scan_cursor = 0

    while best_triangle >= 0:
        tri_added.add(best_triangle)

        face_verts = prims.indices[best_triangle*3:(best_triangle*3)+3]
        new_indices[new_indices_cursor:new_indices_cursor+3] = face_verts
        face_verts >>= 2
        new_indices_cursor += 3

        for face_v_idx, v_idx in enumerate(face_verts):
            end_pos = cache_tag[v_idx]
            if end_pos < 0:
                end_pos = cache_size + face_v_idx
            if end_pos > face_v_idx:
                for shift_idx in range(end_pos, face_v_idx, -1):
                    cache[shift_idx] = cache[shift_idx-1]
                    if cache[shift_idx] >= 0:
                        cache_tag[cache[shift_idx]] += 1
                cache[face_v_idx] = v_idx
                cache_tag[v_idx] = face_v_idx
            tri_indices[v_idx].remove(best_triangle)

        for c_idx in range(cache_size+3):
            v_idx = cache[c_idx]
            if v_idx < 0:
                break
            if c_idx >= cache_size:
                cache_tag[v_idx] = -1
                cache[c_idx] = -1
            new_score = get_vtx_score(len(tri_indices[v_idx]), cache_tag[v_idx])
            score_delta = new_score - last_score[v_idx]
            for f_idx in tri_indices[v_idx]:
                tri_score[f_idx] += score_delta

        best_triangle = -1
        best_score = -1
        for c_idx in range(cache_size):
            v_idx = cache[c_idx]
            if v_idx < 0:
                break
            for f_idx in tri_indices[v_idx]:
                if tri_score[f_idx] > best_score:
                    best_triangle = f_idx
                    best_score = tri_score[f_idx]

        if best_triangle < 0:
            while scan_cursor < prims.face_count:
                if scan_cursor not in tri_added:
                    best_triangle = scan_cursor
                    break
                scan_cursor += 1

    prims.indices = new_indices
