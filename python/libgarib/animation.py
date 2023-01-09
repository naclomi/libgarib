import math

import numpy as np

from dataclasses import dataclass
from .parsers.glover_objbank import GloverObjbank

FRAME_TO_SEC = 1/29.97


neutralTranslationAnimation = [np.zeros((1,3), dtype="f"), np.zeros(1, dtype="i")]
neutralRotationAnimation = [np.zeros((1,4), dtype="f"), np.zeros(1, dtype="i")]
neutralScaleAnimation = [np.ones((1,3), dtype="f"), np.zeros(1, dtype="i")]

@dataclass
class InterpolatedFrame:
    v1: float
    v2: float
    v3: float
    v4: float
    t: float

def lerp(a, b, t):
    return a*(1-t) + b*t

def lerpFrame(frame1, frame2, t):
    if t <= frame1.t:
        return frame1
    elif t >= frame2.t:
        return frame2
    else:
        original_t = t
        t -= frame1.t
        t /= frame2.t - frame1.t
        return InterpolatedFrame(
            lerp(frame1.v1, frame2.v1, t),
            lerp(frame1.v2, frame2.v2, t),
            lerp(frame1.v3, frame2.v3, t),
            lerp(frame1.v4, frame2.v4, t),
            original_t
        )

def slerpFrame(frame1, frame2, t):
    if t <= frame1.t:
        return frame1
    elif t >= frame2.t:
        return frame2
    else:
        original_t = t
        t -= frame1.t
        t /= frame2.t - frame1.t

        dot = ((frame1.v1 * frame2.v1) +
               (frame1.v2 * frame2.v2) + 
               (frame1.v3 * frame2.v3) +
               (frame1.v4 * frame2.v4))

        if dot < 0.0:
            dot = -dot
            tmp = (-frame2.v1, -frame2.v2, -frame2.v3, -frame2.v4)
        else:
            tmp = (frame2.v1, frame2.v2, frame2.v3, frame2.v4)

        if dot < 0.95:
            theta = math.acos(dot)
            sin_1minust = math.sin(theta * (1-t))
            sin_t = math.sin(theta * t)
            sin_theta = math.sin(theta)
            return InterpolatedFrame(
                (frame1.v1 * sin_1minust + tmp[0] * sin_t) / sin_theta,
                (frame1.v2 * sin_1minust + tmp[1] * sin_t) / sin_theta,
                (frame1.v3 * sin_1minust + tmp[2] * sin_t) / sin_theta,
                (frame1.v4 * sin_1minust + tmp[3] * sin_t) / sin_theta,
                original_t
            )
        else:
            return InterpolatedFrame(
                frame1.v1*(1-t) + frame2.v1*t,
                frame1.v2*(1-t) + frame2.v2*t,
                frame1.v3*(1-t) + frame2.v3*t,
                frame1.v4*(1-t) + frame2.v4*t,
                original_t
            )
