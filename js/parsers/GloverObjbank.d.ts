// This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

interface DebugPosition {
  start: number;
  end: number;
  ioOffset: number;
}

declare class GloverObjbank {
  constructor(io: any, parent?: any, root?: any);
  __type: 'GloverObjbank';
  _io: any;

  directory: GloverObjbank.DirectoryEntry[];

  _debug: {
    directory: DebugPosition;
  };
}

declare namespace GloverObjbank {
  class Uv {
    constructor(io: any, parent?: any, root?: any);
    __type: 'Uv';
    _io: any;

    u1: GloverObjbank.S105;
    v1: GloverObjbank.S105;
    u2: GloverObjbank.S105;
    v2: GloverObjbank.S105;
    u3: GloverObjbank.S105;
    v3: GloverObjbank.S105;

    _debug: {
      u1: DebugPosition;
      v1: DebugPosition;
      u2: DebugPosition;
      v2: DebugPosition;
      u3: DebugPosition;
      v3: DebugPosition;
    };
  }
}

declare namespace GloverObjbank {
  class Vertex {
    constructor(io: any, parent?: any, root?: any);
    __type: 'Vertex';
    _io: any;

    x: number;
    y: number;
    z: number;

    _debug: {
      x: DebugPosition;
      y: DebugPosition;
      z: DebugPosition;
    };
  }
}

declare namespace GloverObjbank {
  class ObjectRoot {
    constructor(io: any, parent?: any, root?: any);
    __type: 'ObjectRoot';
    _io: any;

    mesh: GloverObjbank.Mesh;
    animation: GloverObjbank.Animation;
    objId: number;
    bankBaseAddr: number;
    u2: number;
    meshPtr: number;
    u3: number;
    u4: number;
    animationPtr: number;

    _debug: {
      objId: DebugPosition;
      bankBaseAddr: DebugPosition;
      u2: DebugPosition;
      meshPtr: DebugPosition;
      u3: DebugPosition;
      u4: DebugPosition;
      animationPtr: DebugPosition;
    };
  }
}

declare namespace GloverObjbank {
  class DisplayListCmd {
    constructor(io: any, parent?: any, root?: any);
    __type: 'DisplayListCmd';
    _io: any;

    cmd: number;
    w1: number;
    w0: number;

    _debug: {
      w1: DebugPosition;
      w0: DebugPosition;
    };
  }
}

declare namespace GloverObjbank {
  class DirectoryEntry {
    constructor(io: any, parent?: any, root?: any);
    __type: 'DirectoryEntry';
    _io: any;

    objRoot: GloverObjbank.ObjectRoot;
    objId: number;
    ptr: number;

    _debug: {
      objId: DebugPosition;
      ptr: DebugPosition;
    };
  }
}

declare namespace GloverObjbank {
  class AffineFrame {
    constructor(io: any, parent?: any, root?: any);
    __type: 'AffineFrame';
    _io: any;

    v1: number;
    v2: number;
    v3: number;
    v4: number;
    t: number;

    _debug: {
      v1: DebugPosition;
      v2: DebugPosition;
      v3: DebugPosition;
      v4: DebugPosition;
      t: DebugPosition;
    };
  }
}

declare namespace GloverObjbank {
  class AnimationDefinition {
    constructor(io: any, parent?: any, root?: any);
    __type: 'AnimationDefinition';
    _io: any;

    startTime: number;
    endTime: number;
    playbackSpeed: number;
    unused: number;

    _debug: {
      startTime: DebugPosition;
      endTime: DebugPosition;
      playbackSpeed: DebugPosition;
      unused: DebugPosition;
    };
  }
}

declare namespace GloverObjbank {
  class Face {
    constructor(io: any, parent?: any, root?: any);
    __type: 'Face';
    _io: any;

    v0: number;
    v1: number;
    v2: number;

    _debug: {
      v0: DebugPosition;
      v1: DebugPosition;
      v2: DebugPosition;
    };
  }
}

declare namespace GloverObjbank {
  class Sprite {
    constructor(io: any, parent?: any, root?: any);
    __type: 'Sprite';
    _io: any;

    textureId: number;
    runtimeDataPtr: number;
    x: number;
    y: number;
    z: number;
    width: number;
    height: number;
    u5: number;
    u6: number;
    flags: number;

    _debug: {
      textureId: DebugPosition;
      runtimeDataPtr: DebugPosition;
      x: DebugPosition;
      y: DebugPosition;
      z: DebugPosition;
      width: DebugPosition;
      height: DebugPosition;
      u5: DebugPosition;
      u6: DebugPosition;
      flags: DebugPosition;
    };
  }
}

declare namespace GloverObjbank {
  class Animation {
    constructor(io: any, parent?: any, root?: any);
    __type: 'Animation';
    _io: any;

    animationDefinitions: GloverObjbank.AnimationDefinition[];
    numAnimationDefinitions: number;
    currentAnimationIdx: number;
    u3: number;
    isPlaying: number;
    timeDelta: number;
    nextAnimIdx: number[];
    pad: number;
    nextIsPlaying: number[];
    nextTimeDelta: number[];
    nextAnimSlotIdx: number;
    u15: number;
    animationDefinitionsPtr: number;
    curTime: number;

    _debug: {
      numAnimationDefinitions: DebugPosition;
      currentAnimationIdx: DebugPosition;
      u3: DebugPosition;
      isPlaying: DebugPosition;
      timeDelta: DebugPosition;
      nextAnimIdx: DebugPosition;
      pad: DebugPosition;
      nextIsPlaying: DebugPosition;
      nextTimeDelta: DebugPosition;
      nextAnimSlotIdx: DebugPosition;
      u15: DebugPosition;
      animationDefinitionsPtr: DebugPosition;
      curTime: DebugPosition;
    };
  }
}

declare namespace GloverObjbank {
  class Mesh {
    constructor(io: any, parent?: any, root?: any);
    __type: 'Mesh';
    _io: any;

    rotation: GloverObjbank.AffineFrame[];
    geometry: GloverObjbank.Geometry;
    scale: GloverObjbank.AffineFrame[];
    translation: GloverObjbank.AffineFrame[];
    child: GloverObjbank.Mesh;
    sibling: GloverObjbank.Mesh;
    displayList: GloverObjbank.DisplayListCmd[];
    sprites: GloverObjbank.Sprite[];
    id: number;
    name: string;
    meshAlpha: number;
    spriteAlpha: number;
    numScale: number;
    numTranslation: number;
    numRotation: number;
    geometryPtr: number;
    displayListPtr: number;
    scalePtr: number;
    translationPtr: number;
    rotationPtr: number;
    numSprites: number;
    spritesPtr: number;
    numChildren: number;
    renderMode: number;
    childPtr: number;
    siblingPtr: number;
    runtimeCollisionDataPtr: number;

    _debug: {
      id: DebugPosition;
      name: DebugPosition;
      meshAlpha: DebugPosition;
      spriteAlpha: DebugPosition;
      numScale: DebugPosition;
      numTranslation: DebugPosition;
      numRotation: DebugPosition;
      geometryPtr: DebugPosition;
      displayListPtr: DebugPosition;
      scalePtr: DebugPosition;
      translationPtr: DebugPosition;
      rotationPtr: DebugPosition;
      numSprites: DebugPosition;
      spritesPtr: DebugPosition;
      numChildren: DebugPosition;
      renderMode: DebugPosition;
      childPtr: DebugPosition;
      siblingPtr: DebugPosition;
      runtimeCollisionDataPtr: DebugPosition;
    };
  }
}

declare namespace GloverObjbank {
  class Geometry {
    constructor(io: any, parent?: any, root?: any);
    __type: 'Geometry';
    _io: any;

    textureIds: number[];
    faces: GloverObjbank.Face[];
    vertexCn: number[];
    uvsUnmodified: GloverObjbank.Uv[];
    flags: number[];
    vertices: GloverObjbank.Vertex[];
    uvs: GloverObjbank.Uv[];
    faceCn: number[];
    numFaces: number;
    numVertices: number;
    verticesPtr: number;
    facesPtr: number;
    faceCnPtr: number;
    uvsPtr: number;
    uvsUnmodifiedPtr: number;
    vertexCnPtr: number;
    flagsPtr: number;
    textureIdsPtr: number;

    _debug: {
      numFaces: DebugPosition;
      numVertices: DebugPosition;
      verticesPtr: DebugPosition;
      facesPtr: DebugPosition;
      faceCnPtr: DebugPosition;
      uvsPtr: DebugPosition;
      uvsUnmodifiedPtr: DebugPosition;
      vertexCnPtr: DebugPosition;
      flagsPtr: DebugPosition;
      textureIdsPtr: DebugPosition;
    };
  }
}

declare namespace GloverObjbank {
  class S105 {
    constructor(io: any, parent?: any, root?: any);
    __type: 'S105';
    _io: any;

    value: number;
    raw: number;

    _debug: {
      raw: DebugPosition;
    };
  }
}

export = GloverObjbank;
export as namespace GloverObjbank;
