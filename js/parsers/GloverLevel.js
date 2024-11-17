// This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define(['kaitai-struct/KaitaiStream'], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory(require('kaitai-struct/KaitaiStream'));
  } else {
    root.GloverLevel = factory(root.KaitaiStream);
  }
}(typeof self !== 'undefined' ? self : this, function (KaitaiStream) {
var GloverLevel = (function() {
  function GloverLevel(_io, _parent, _root) {
    this.__type = 'GloverLevel';
    this._io = _io;
    this._parent = _parent;
    this._root = _root || this;
    this._debug = {};

    this._read();
  }
  GloverLevel.prototype._read = function() {
    this._debug.length = { start: this._io.pos, ioOffset: this._io.byteOffset };
    this.length = this._io.readU4be();
    this._debug.length.end = this._io.pos;
    this._debug.name = { start: this._io.pos, ioOffset: this._io.byteOffset };
    this.name = KaitaiStream.bytesToStr(this._io.readBytesTerm(0, false, true, true), "ASCII");
    this._debug.name.end = this._io.pos;
    this._debug.body = { start: this._io.pos, ioOffset: this._io.byteOffset };
    this.body = [];
    this._debug.body.arr = [];
    var i = 0;
    while (!this._io.isEof()) {
      this._debug.body.arr[this.body.length] = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.body.push(new Cmd(this._io, this, this._root));
      this._debug.body.arr[this.body.length - 1].end = this._io.pos;
      i++;
    }
    this._debug.body.end = this._io.pos;
  }

  var PuzzleCondGloverChangedTouchingPlatform = GloverLevel.PuzzleCondGloverChangedTouchingPlatform = (function() {
    function PuzzleCondGloverChangedTouchingPlatform(_io, _parent, _root) {
      this.__type = 'PuzzleCondGloverChangedTouchingPlatform';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondGloverChangedTouchingPlatform.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.startedOrStopped = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.startedOrStopped = this._io.readS2be();
      this._debug.startedOrStopped.end = this._io.pos;
    }

    return PuzzleCondGloverChangedTouchingPlatform;
  })();

  var PuzzleAction0x54 = GloverLevel.PuzzleAction0x54 = (function() {
    function PuzzleAction0x54(_io, _parent, _root) {
      this.__type = 'PuzzleAction0x54';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleAction0x54.prototype._read = function() {
      this._debug.u320x14 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x14 = this._io.readU2be();
      this._debug.u320x14.end = this._io.pos;
      this._debug.u320x16 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x16 = this._io.readU2be();
      this._debug.u320x16.end = this._io.pos;
      this._debug.u320x18 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x18 = this._io.readU2be();
      this._debug.u320x18.end = this._io.pos;
      this._debug.u320x1a = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x1a = this._io.readU2be();
      this._debug.u320x1a.end = this._io.pos;
      this._debug.u320x1c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x1c = this._io.readU2be();
      this._debug.u320x1c.end = this._io.pos;
      this._debug.u320x1e = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x1e = this._io.readU2be();
      this._debug.u320x1e.end = this._io.pos;
      this._debug.u320x10 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x10 = this._io.readU2be();
      this._debug.u320x10.end = this._io.pos;
      this._debug.u160x0e = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x0e = this._io.readU2be();
      this._debug.u160x0e.end = this._io.pos;
      this._debug.u320x24 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x24 = this._io.readU4be();
      this._debug.u320x24.end = this._io.pos;
      this._debug.u320x28 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x28 = this._io.readU4be();
      this._debug.u320x28.end = this._io.pos;
      this._debug.u320x2c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x2c = this._io.readU4be();
      this._debug.u320x2c.end = this._io.pos;
      this._debug.u160x0a = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x0a = this._io.readU2be();
      this._debug.u160x0a.end = this._io.pos;
    }

    return PuzzleAction0x54;
  })();

  var PlatSound0xc2 = GloverLevel.PlatSound0xc2 = (function() {
    function PlatSound0xc2(_io, _parent, _root) {
      this.__type = 'PlatSound0xc2';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSound0xc2.prototype._read = function() {
      this._debug.soundId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.soundId = this._io.readU2be();
      this._debug.soundId.end = this._io.pos;
      this._debug.volume = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.volume = this._io.readU2be();
      this._debug.volume.end = this._io.pos;
      this._debug.pitch = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.pitch = this._io.readU2be();
      this._debug.pitch.end = this._io.pos;
    }

    return PlatSound0xc2;
  })();

  var PuzzleCondBallChangedTouchingPlatform = GloverLevel.PuzzleCondBallChangedTouchingPlatform = (function() {
    function PuzzleCondBallChangedTouchingPlatform(_io, _parent, _root) {
      this.__type = 'PuzzleCondBallChangedTouchingPlatform';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondBallChangedTouchingPlatform.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.startedOrStopped = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.startedOrStopped = this._io.readS2be();
      this._debug.startedOrStopped.end = this._io.pos;
    }

    return PuzzleCondBallChangedTouchingPlatform;
  })();

  var PlatSpinPause0x7c = GloverLevel.PlatSpinPause0x7c = (function() {
    function PlatSpinPause0x7c(_io, _parent, _root) {
      this.__type = 'PlatSpinPause0x7c';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSpinPause0x7c.prototype._read = function() {
      this._debug.u160x0c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x0c = this._io.readU2be();
      this._debug.u160x0c.end = this._io.pos;
      this._debug.u160x0a = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x0a = this._io.readU2be();
      this._debug.u160x0a.end = this._io.pos;
    }

    return PlatSpinPause0x7c;
  })();

  var PlatMagnet0x8b = GloverLevel.PlatMagnet0x8b = (function() {
    function PlatMagnet0x8b(_io, _parent, _root) {
      this.__type = 'PlatMagnet0x8b';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatMagnet0x8b.prototype._read = function() {
      this._debug.u160x0c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x0c = this._io.readU2be();
      this._debug.u160x0c.end = this._io.pos;
      this._debug.u320x48 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x48 = this._io.readU4be();
      this._debug.u320x48.end = this._io.pos;
      this._debug.u320x4c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x4c = this._io.readU4be();
      this._debug.u320x4c.end = this._io.pos;
      this._debug.u320x50 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x50 = this._io.readU4be();
      this._debug.u320x50.end = this._io.pos;
      this._debug.u320x10 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x10 = this._io.readU4be();
      this._debug.u320x10.end = this._io.pos;
      this._debug.u320x14 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x14 = this._io.readU4be();
      this._debug.u320x14.end = this._io.pos;
      this._debug.u320x18 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x18 = this._io.readU4be();
      this._debug.u320x18.end = this._io.pos;
      this._debug.u320x1c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x1c = this._io.readU4be();
      this._debug.u320x1c.end = this._io.pos;
    }

    return PlatMagnet0x8b;
  })();

  var PuzzleActionCameraFlyTowardsPoint = GloverLevel.PuzzleActionCameraFlyTowardsPoint = (function() {
    function PuzzleActionCameraFlyTowardsPoint(_io, _parent, _root) {
      this.__type = 'PuzzleActionCameraFlyTowardsPoint';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionCameraFlyTowardsPoint.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
    }

    return PuzzleActionCameraFlyTowardsPoint;
  })();

  var EnemyInstructionError = GloverLevel.EnemyInstructionError = (function() {
    function EnemyInstructionError(_io, _parent, _root) {
      this.__type = 'EnemyInstructionError';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyInstructionError.prototype._read = function() {
    }

    return EnemyInstructionError;
  })();

  var PuzzleActionHidePlatform = GloverLevel.PuzzleActionHidePlatform = (function() {
    function PuzzleActionHidePlatform(_io, _parent, _root) {
      this.__type = 'PuzzleActionHidePlatform';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionHidePlatform.prototype._read = function() {
      this._debug.hideEnabled = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.hideEnabled = this._io.readU4be();
      this._debug.hideEnabled.end = this._io.pos;
      this._debug.platformTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platformTag = this._io.readS2be();
      this._debug.platformTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.GenericFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionHidePlatform;
  })();

  var Backdrop = GloverLevel.Backdrop = (function() {
    function Backdrop(_io, _parent, _root) {
      this.__type = 'Backdrop';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Backdrop.prototype._read = function() {
      this._debug.textureId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.textureId = this._io.readU4be();
      this._debug.textureId.end = this._io.pos;
      this._debug.decalPosX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.decalPosX = this._io.readU2be();
      this._debug.decalPosX.end = this._io.pos;
      this._debug.decalPosY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.decalPosY = this._io.readU2be();
      this._debug.decalPosY.end = this._io.pos;
      this._debug.sortKey = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.sortKey = this._io.readU2be();
      this._debug.sortKey.end = this._io.pos;
      this._debug.offsetY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.offsetY = this._io.readS2be();
      this._debug.offsetY.end = this._io.pos;
      this._debug.scaleX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.scaleX = this._io.readU2be();
      this._debug.scaleX.end = this._io.pos;
      this._debug.scaleY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.scaleY = this._io.readU2be();
      this._debug.scaleY.end = this._io.pos;
      this._debug.flipX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.flipX = this._io.readU2be();
      this._debug.flipX.end = this._io.pos;
      this._debug.flipY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.flipY = this._io.readU2be();
      this._debug.flipY.end = this._io.pos;
      this._debug.scrollSpeedX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.scrollSpeedX = this._io.readU2be();
      this._debug.scrollSpeedX.end = this._io.pos;
      this._debug.unused = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.unused = this._io.readU2be();
      this._debug.unused.end = this._io.pos;
      this._debug.decalParentIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.decalParentIdx = this._io.readU2be();
      this._debug.decalParentIdx.end = this._io.pos;
    }

    return Backdrop;
  })();

  var DiffuseLight = GloverLevel.DiffuseLight = (function() {
    function DiffuseLight(_io, _parent, _root) {
      this.__type = 'DiffuseLight';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    DiffuseLight.prototype._read = function() {
      this._debug.r = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.r = this._io.readU2be();
      this._debug.r.end = this._io.pos;
      this._debug.g = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.g = this._io.readU2be();
      this._debug.g.end = this._io.pos;
      this._debug.b = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.b = this._io.readU2be();
      this._debug.b.end = this._io.pos;
      this._debug.thetaX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.thetaX = this._io.readF4be();
      this._debug.thetaX.end = this._io.pos;
      this._debug.thetaY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.thetaY = this._io.readF4be();
      this._debug.thetaY.end = this._io.pos;
    }

    return DiffuseLight;
  })();

  var PuzzleCondPlatformDoesntExist = GloverLevel.PuzzleCondPlatformDoesntExist = (function() {
    function PuzzleCondPlatformDoesntExist(_io, _parent, _root) {
      this.__type = 'PuzzleCondPlatformDoesntExist';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondPlatformDoesntExist.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.reserved = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.reserved = this._io.readU2be();
      this._debug.reserved.end = this._io.pos;
    }

    return PuzzleCondPlatformDoesntExist;
  })();

  var PuzzleActionCameraTweenDistance = GloverLevel.PuzzleActionCameraTweenDistance = (function() {
    function PuzzleActionCameraTweenDistance(_io, _parent, _root) {
      this.__type = 'PuzzleActionCameraTweenDistance';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionCameraTweenDistance.prototype._read = function() {
      this._debug.distance = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.distance = this._io.readF4be();
      this._debug.distance.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
    }

    return PuzzleActionCameraTweenDistance;
  })();

  var PlatPathAcceleration = GloverLevel.PlatPathAcceleration = (function() {
    function PlatPathAcceleration(_io, _parent, _root) {
      this.__type = 'PlatPathAcceleration';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatPathAcceleration.prototype._read = function() {
      this._debug.acceleration = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.acceleration = this._io.readF4be();
      this._debug.acceleration.end = this._io.pos;
    }

    return PlatPathAcceleration;
  })();

  var Buzzer = GloverLevel.Buzzer = (function() {
    function Buzzer(_io, _parent, _root) {
      this.__type = 'Buzzer';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Buzzer.prototype._read = function() {
      this._debug.tag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.tag = this._io.readU2be();
      this._debug.tag.end = this._io.pos;
      this._debug.platform1Tag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platform1Tag = this._io.readU2be();
      this._debug.platform1Tag.end = this._io.pos;
      this._debug.platform2Tag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platform2Tag = this._io.readU2be();
      this._debug.platform2Tag.end = this._io.pos;
      this._debug.drawFlags = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.drawFlags = this._io.readU2be();
      this._debug.drawFlags.end = this._io.pos;
      this._debug.r = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.r = this._io.readU2be();
      this._debug.r.end = this._io.pos;
      this._debug.g = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.g = this._io.readU2be();
      this._debug.g.end = this._io.pos;
      this._debug.b = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.b = this._io.readU2be();
      this._debug.b.end = this._io.pos;
      this._debug.colorJitter = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.colorJitter = this._io.readU2be();
      this._debug.colorJitter.end = this._io.pos;
      this._debug.end1X = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.end1X = this._io.readF4be();
      this._debug.end1X.end = this._io.pos;
      this._debug.end1Y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.end1Y = this._io.readF4be();
      this._debug.end1Y.end = this._io.pos;
      this._debug.end1Z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.end1Z = this._io.readF4be();
      this._debug.end1Z.end = this._io.pos;
      this._debug.end2X = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.end2X = this._io.readF4be();
      this._debug.end2X.end = this._io.pos;
      this._debug.end2Y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.end2Y = this._io.readF4be();
      this._debug.end2Y.end = this._io.pos;
      this._debug.end2Z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.end2Z = this._io.readF4be();
      this._debug.end2Z.end = this._io.pos;
      this._debug.drawDiameter = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.drawDiameter = this._io.readF4be();
      this._debug.drawDiameter.end = this._io.pos;
      this._debug.drawThickness = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.drawThickness = this._io.readF4be();
      this._debug.drawThickness.end = this._io.pos;
    }

    return Buzzer;
  })();

  var PuzzleActionCameraLookAtPoint2 = GloverLevel.PuzzleActionCameraLookAtPoint2 = (function() {
    function PuzzleActionCameraLookAtPoint2(_io, _parent, _root) {
      this.__type = 'PuzzleActionCameraLookAtPoint2';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionCameraLookAtPoint2.prototype._read = function() {
      this._debug.lookatX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.lookatX = this._io.readF4be();
      this._debug.lookatX.end = this._io.pos;
      this._debug.lookatY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.lookatY = this._io.readF4be();
      this._debug.lookatY.end = this._io.pos;
      this._debug.lookatZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.lookatZ = this._io.readF4be();
      this._debug.lookatZ.end = this._io.pos;
      this._debug.duration = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.duration = this._io.readF4be();
      this._debug.duration.end = this._io.pos;
      this._debug.reserved = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.reserved = this._io.readU2be();
      this._debug.reserved.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.CameraFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionCameraLookAtPoint2;
  })();

  var PuzzleAny = GloverLevel.PuzzleAny = (function() {
    function PuzzleAny(_io, _parent, _root) {
      this.__type = 'PuzzleAny';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleAny.prototype._read = function() {
      this._debug.op = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.op = this._io.readU2be();
      this._debug.op.end = this._io.pos;
    }

    return PuzzleAny;
  })();

  var SetActorRotation = GloverLevel.SetActorRotation = (function() {
    function SetActorRotation(_io, _parent, _root) {
      this.__type = 'SetActorRotation';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    SetActorRotation.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
    }

    return SetActorRotation;
  })();

  var CameoInst = GloverLevel.CameoInst = (function() {
    function CameoInst(_io, _parent, _root) {
      this.__type = 'CameoInst';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    CameoInst.prototype._read = function() {
      this._debug.instType = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.instType = this._io.readU2be();
      this._debug.instType.end = this._io.pos;
      this._debug.body = { start: this._io.pos, ioOffset: this._io.byteOffset };
      switch (this.instType) {
      case 0:
        this.body = new CameoPlayAnimation(this._io, this, this._root);
        break;
      case 4:
        this.body = new CameoGrabTodo(this._io, this, this._root);
        break;
      case 6:
        this.body = new CameoLightningFlash(this._io, this, this._root);
        break;
      case 1:
        this.body = new CameoSetCameraAttention(this._io, this, this._root);
        break;
      case 3:
        this.body = new CameoSpin(this._io, this, this._root);
        break;
      case 5:
        this.body = new CameoSetEnemyFlagTodo(this._io, this, this._root);
        break;
      case 2:
        this.body = new CameoInst2(this._io, this, this._root);
        break;
      default:
        this.body = new CameoInstDefault(this._io, this, this._root);
        break;
      }
      this._debug.body.end = this._io.pos;
    }

    return CameoInst;
  })();

  var PuzzleCondDefault = GloverLevel.PuzzleCondDefault = (function() {
    function PuzzleCondDefault(_io, _parent, _root) {
      this.__type = 'PuzzleCondDefault';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondDefault.prototype._read = function() {
      this._debug.u320x24 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x24 = this._io.readU2be();
      this._debug.u320x24.end = this._io.pos;
      this._debug.u160x0a = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x0a = this._io.readU2be();
      this._debug.u160x0a.end = this._io.pos;
    }

    return PuzzleCondDefault;
  })();

  var PlatTurnTowardsPathPoint = GloverLevel.PlatTurnTowardsPathPoint = (function() {
    function PlatTurnTowardsPathPoint(_io, _parent, _root) {
      this.__type = 'PlatTurnTowardsPathPoint';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatTurnTowardsPathPoint.prototype._read = function() {
      this._debug.input1 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.input1 = this._io.readU4be();
      this._debug.input1.end = this._io.pos;
      this._debug.input2 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.input2 = this._io.readU4be();
      this._debug.input2.end = this._io.pos;
    }

    return PlatTurnTowardsPathPoint;
  })();

  var PlatMvspn0x5a = GloverLevel.PlatMvspn0x5a = (function() {
    function PlatMvspn0x5a(_io, _parent, _root) {
      this.__type = 'PlatMvspn0x5a';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatMvspn0x5a.prototype._read = function() {
      this._debug.u160x1c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x1c = this._io.readU2be();
      this._debug.u160x1c.end = this._io.pos;
      this._debug.u320x18 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x18 = this._io.readU4be();
      this._debug.u320x18.end = this._io.pos;
    }

    return PlatMvspn0x5a;
  })();

  var PlatMvspn0x74 = GloverLevel.PlatMvspn0x74 = (function() {
    function PlatMvspn0x74(_io, _parent, _root) {
      this.__type = 'PlatMvspn0x74';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatMvspn0x74.prototype._read = function() {
      this._debug.u320x34 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x34 = this._io.readU4be();
      this._debug.u320x34.end = this._io.pos;
      this._debug.u320x38 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x38 = this._io.readU4be();
      this._debug.u320x38.end = this._io.pos;
      this._debug.u320x3c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x3c = this._io.readU4be();
      this._debug.u320x3c.end = this._io.pos;
    }

    return PlatMvspn0x74;
  })();

  var PuzzleActionRegSet = GloverLevel.PuzzleActionRegSet = (function() {
    function PuzzleActionRegSet(_io, _parent, _root) {
      this.__type = 'PuzzleActionRegSet';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionRegSet.prototype._read = function() {
      this._debug.immValOrSrcReg = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.immValOrSrcReg = this._io.readF4be();
      this._debug.immValOrSrcReg.end = this._io.pos;
      this._debug.dstReg = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.dstReg = this._io.readU2be();
      this._debug.dstReg.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.RegisterFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionRegSet;
  })();

  var PuzzleActionPlatformConfigOrbit = GloverLevel.PuzzleActionPlatformConfigOrbit = (function() {
    function PuzzleActionPlatformConfigOrbit(_io, _parent, _root) {
      this.__type = 'PuzzleActionPlatformConfigOrbit';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionPlatformConfigOrbit.prototype._read = function() {
      this._debug.velocity = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velocity = this._io.readF4be();
      this._debug.velocity.end = this._io.pos;
      this._debug.platformTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platformTag = this._io.readS2be();
      this._debug.platformTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.PlatformMovementFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionPlatformConfigOrbit;
  })();

  var PlatOrbit = GloverLevel.PlatOrbit = (function() {
    function PlatOrbit(_io, _parent, _root) {
      this.__type = 'PlatOrbit';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatOrbit.prototype._read = function() {
      this._debug.u16120 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u16120 = this._io.readU2be();
      this._debug.u16120.end = this._io.pos;
      this._debug.u16136 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u16136 = this._io.readU2be();
      this._debug.u16136.end = this._io.pos;
      this._debug.u16134 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u16134 = this._io.readU2be();
      this._debug.u16134.end = this._io.pos;
      this._debug.u16132 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u16132 = this._io.readU2be();
      this._debug.u16132.end = this._io.pos;
      this._debug.u32116 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u32116 = this._io.readU4be();
      this._debug.u32116.end = this._io.pos;
      this._debug.name = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.name = KaitaiStream.bytesToStr(this._io.readBytes(8), "ASCII");
      this._debug.name.end = this._io.pos;
      this._debug.f112 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f112 = this._io.readF4be();
      this._debug.f112.end = this._io.pos;
      this._debug.f108 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f108 = this._io.readF4be();
      this._debug.f108.end = this._io.pos;
      this._debug.f104 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f104 = this._io.readF4be();
      this._debug.f104.end = this._io.pos;
      this._debug.f100 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f100 = this._io.readF4be();
      this._debug.f100.end = this._io.pos;
      this._debug.f96 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f96 = this._io.readF4be();
      this._debug.f96.end = this._io.pos;
      this._debug.f92 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f92 = this._io.readF4be();
      this._debug.f92.end = this._io.pos;
      this._debug.f88 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f88 = this._io.readF4be();
      this._debug.f88.end = this._io.pos;
      this._debug.f84 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f84 = this._io.readF4be();
      this._debug.f84.end = this._io.pos;
      this._debug.f80 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f80 = this._io.readF4be();
      this._debug.f80.end = this._io.pos;
      this._debug.u32176 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u32176 = this._io.readU4be();
      this._debug.u32176.end = this._io.pos;
    }

    return PlatOrbit;
  })();

  var PuzzleCondPlatformOrbitTodo = GloverLevel.PuzzleCondPlatformOrbitTodo = (function() {
    function PuzzleCondPlatformOrbitTodo(_io, _parent, _root) {
      this.__type = 'PuzzleCondPlatformOrbitTodo';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondPlatformOrbitTodo.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.idx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.idx = this._io.readS2be();
      this._debug.idx.end = this._io.pos;
    }

    return PuzzleCondPlatformOrbitTodo;
  })();

  var PlatSpike = GloverLevel.PlatSpike = (function() {
    function PlatSpike(_io, _parent, _root) {
      this.__type = 'PlatSpike';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSpike.prototype._read = function() {
    }

    return PlatSpike;
  })();

  var PlatActorSurfaceType = GloverLevel.PlatActorSurfaceType = (function() {
    function PlatActorSurfaceType(_io, _parent, _root) {
      this.__type = 'PlatActorSurfaceType';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatActorSurfaceType.prototype._read = function() {
      this._debug.value = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.value = this._io.readU2be();
      this._debug.value.end = this._io.pos;
    }

    return PlatActorSurfaceType;
  })();

  var PuzzleActionPlatformNudge = GloverLevel.PuzzleActionPlatformNudge = (function() {
    function PuzzleActionPlatformNudge(_io, _parent, _root) {
      this.__type = 'PuzzleActionPlatformNudge';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionPlatformNudge.prototype._read = function() {
      this._debug.velocity = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velocity = this._io.readF4be();
      this._debug.velocity.end = this._io.pos;
      this._debug.platformTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platformTag = this._io.readS2be();
      this._debug.platformTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.PlatformMovementFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionPlatformNudge;
  })();

  var Plat0x9f = GloverLevel.Plat0x9f = (function() {
    function Plat0x9f(_io, _parent, _root) {
      this.__type = 'Plat0x9f';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Plat0x9f.prototype._read = function() {
      this._debug.u320x6c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x6c = this._io.readU4be();
      this._debug.u320x6c.end = this._io.pos;
      this._debug.u320x70 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x70 = this._io.readU4be();
      this._debug.u320x70.end = this._io.pos;
      this._debug.u320x1c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x1c = this._io.readU4be();
      this._debug.u320x1c.end = this._io.pos;
      this._debug.u320x28 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x28 = this._io.readU4be();
      this._debug.u320x28.end = this._io.pos;
    }

    return Plat0x9f;
  })();

  var EnemyInstructionDash = GloverLevel.EnemyInstructionDash = (function() {
    function EnemyInstructionDash(_io, _parent, _root) {
      this.__type = 'EnemyInstructionDash';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyInstructionDash.prototype._read = function() {
      this._debug.destinationX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.destinationX = this._io.readF4be();
      this._debug.destinationX.end = this._io.pos;
      this._debug.destinationY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.destinationY = this._io.readF4be();
      this._debug.destinationY.end = this._io.pos;
      this._debug.destinationZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.destinationZ = this._io.readF4be();
      this._debug.destinationZ.end = this._io.pos;
      this._debug.velMagnitude = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velMagnitude = this._io.readF4be();
      this._debug.velMagnitude.end = this._io.pos;
    }

    return EnemyInstructionDash;
  })();

  var PlatReverseAtEndsOfPath = GloverLevel.PlatReverseAtEndsOfPath = (function() {
    function PlatReverseAtEndsOfPath(_io, _parent, _root) {
      this.__type = 'PlatReverseAtEndsOfPath';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatReverseAtEndsOfPath.prototype._read = function() {
    }

    return PlatReverseAtEndsOfPath;
  })();

  var PuzzleCondCameraWithinVolume = GloverLevel.PuzzleCondCameraWithinVolume = (function() {
    function PuzzleCondCameraWithinVolume(_io, _parent, _root) {
      this.__type = 'PuzzleCondCameraWithinVolume';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondCameraWithinVolume.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.l = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.l = this._io.readF4be();
      this._debug.l.end = this._io.pos;
      this._debug.w = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.w = this._io.readF4be();
      this._debug.w.end = this._io.pos;
      this._debug.h = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.h = this._io.readF4be();
      this._debug.h.end = this._io.pos;
    }

    return PuzzleCondCameraWithinVolume;
  })();

  var PlatSetInitialPos = GloverLevel.PlatSetInitialPos = (function() {
    function PlatSetInitialPos(_io, _parent, _root) {
      this.__type = 'PlatSetInitialPos';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSetInitialPos.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
    }

    return PlatSetInitialPos;
  })();

  var CameoSetEnemyFlagTodo = GloverLevel.CameoSetEnemyFlagTodo = (function() {
    function CameoSetEnemyFlagTodo(_io, _parent, _root) {
      this.__type = 'CameoSetEnemyFlagTodo';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    CameoSetEnemyFlagTodo.prototype._read = function() {
      this._debug.enemyIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.enemyIdx = this._io.readU2be();
      this._debug.enemyIdx.end = this._io.pos;
      this._debug.frameCount = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.frameCount = this._io.readS2be();
      this._debug.frameCount.end = this._io.pos;
      this._debug.precedingInstrIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.precedingInstrIdx = this._io.readS2be();
      this._debug.precedingInstrIdx.end = this._io.pos;
    }

    return CameoSetEnemyFlagTodo;
  })();

  var Actor0xbf = GloverLevel.Actor0xbf = (function() {
    function Actor0xbf(_io, _parent, _root) {
      this.__type = 'Actor0xbf';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Actor0xbf.prototype._read = function() {
      this._debug.mode = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.mode = this._io.readU2be();
      this._debug.mode.end = this._io.pos;
      this._debug.childMeshId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.childMeshId = this._io.readU4be();
      this._debug.childMeshId.end = this._io.pos;
    }

    return Actor0xbf;
  })();

  var PuzzleActionStartCameo = GloverLevel.PuzzleActionStartCameo = (function() {
    function PuzzleActionStartCameo(_io, _parent, _root) {
      this.__type = 'PuzzleActionStartCameo';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionStartCameo.prototype._read = function() {
      this._debug.reserved = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.reserved = this._io.readU4be();
      this._debug.reserved.end = this._io.pos;
      this._debug.cameoIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.cameoIdx = this._io.readS2be();
      this._debug.cameoIdx.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.GenericFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionStartCameo;
  })();

  var PlatMaxVelocity = GloverLevel.PlatMaxVelocity = (function() {
    function PlatMaxVelocity(_io, _parent, _root) {
      this.__type = 'PlatMaxVelocity';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatMaxVelocity.prototype._read = function() {
      this._debug.velocity = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velocity = this._io.readF4be();
      this._debug.velocity.end = this._io.pos;
    }

    return PlatMaxVelocity;
  })();

  var EnemyFinalize = GloverLevel.EnemyFinalize = (function() {
    function EnemyFinalize(_io, _parent, _root) {
      this.__type = 'EnemyFinalize';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyFinalize.prototype._read = function() {
    }

    return EnemyFinalize;
  })();

  var PlatMvspn0x59 = GloverLevel.PlatMvspn0x59 = (function() {
    function PlatMvspn0x59(_io, _parent, _root) {
      this.__type = 'PlatMvspn0x59';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatMvspn0x59.prototype._read = function() {
      this._debug.u160x24 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x24 = this._io.readU2be();
      this._debug.u160x24.end = this._io.pos;
      this._debug.u320x20 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x20 = this._io.readU4be();
      this._debug.u320x20.end = this._io.pos;
      this._debug.u320x28 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x28 = this._io.readU4be();
      this._debug.u320x28.end = this._io.pos;
      this._debug.u320x2c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x2c = this._io.readU4be();
      this._debug.u320x2c.end = this._io.pos;
      this._debug.u320x30 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x30 = this._io.readU4be();
      this._debug.u320x30.end = this._io.pos;
    }

    return PlatMvspn0x59;
  })();

  var Cameo = GloverLevel.Cameo = (function() {
    function Cameo(_io, _parent, _root) {
      this.__type = 'Cameo';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Cameo.prototype._read = function() {
    }

    return Cameo;
  })();

  var PuzzleCondPlatformSpin2Todo = GloverLevel.PuzzleCondPlatformSpin2Todo = (function() {
    function PuzzleCondPlatformSpin2Todo(_io, _parent, _root) {
      this.__type = 'PuzzleCondPlatformSpin2Todo';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondPlatformSpin2Todo.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.arg2 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.arg2 = this._io.readS2be();
      this._debug.arg2.end = this._io.pos;
    }

    return PuzzleCondPlatformSpin2Todo;
  })();

  var PuzzleCondEnemyIsTouchingPlatform = GloverLevel.PuzzleCondEnemyIsTouchingPlatform = (function() {
    function PuzzleCondEnemyIsTouchingPlatform(_io, _parent, _root) {
      this.__type = 'PuzzleCondEnemyIsTouchingPlatform';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondEnemyIsTouchingPlatform.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.invertResult = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.invertResult = this._io.readS2be();
      this._debug.invertResult.end = this._io.pos;
    }

    return PuzzleCondEnemyIsTouchingPlatform;
  })();

  var PlatConstantSpin = GloverLevel.PlatConstantSpin = (function() {
    PlatConstantSpin.Axis = Object.freeze({
      X: 0,
      Y: 1,
      Z: 2,

      0: "X",
      1: "Y",
      2: "Z",
    });

    function PlatConstantSpin(_io, _parent, _root) {
      this.__type = 'PlatConstantSpin';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatConstantSpin.prototype._read = function() {
      this._debug.axis = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PlatConstantSpin.Axis" };
      this.axis = this._io.readU2be();
      this._debug.axis.end = this._io.pos;
      this._debug.initialTheta = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.initialTheta = this._io.readF4be();
      this._debug.initialTheta.end = this._io.pos;
      this._debug.speed = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.speed = this._io.readF4be();
      this._debug.speed.end = this._io.pos;
    }

    return PlatConstantSpin;
  })();

  var PuzzleActionPlatformSpinAlongAxis = GloverLevel.PuzzleActionPlatformSpinAlongAxis = (function() {
    function PuzzleActionPlatformSpinAlongAxis(_io, _parent, _root) {
      this.__type = 'PuzzleActionPlatformSpinAlongAxis';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionPlatformSpinAlongAxis.prototype._read = function() {
      this._debug.axisIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.axisIdx = this._io.readU4be();
      this._debug.axisIdx.end = this._io.pos;
      this._debug.platformTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platformTag = this._io.readS2be();
      this._debug.platformTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.GenericFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionPlatformSpinAlongAxis;
  })();

  var PuzzlePlatformCloseToConfBoundaryEdge = GloverLevel.PuzzlePlatformCloseToConfBoundaryEdge = (function() {
    PuzzlePlatformCloseToConfBoundaryEdge.EdgeType = Object.freeze({
      X: 0,
      Y: 1,
      Z: 2,
      X_PLUS_W: 3,
      Y_PLUS_H: 4,
      Z_PLUS_D: 5,

      0: "X",
      1: "Y",
      2: "Z",
      3: "X_PLUS_W",
      4: "Y_PLUS_H",
      5: "Z_PLUS_D",
    });

    function PuzzlePlatformCloseToConfBoundaryEdge(_io, _parent, _root) {
      this.__type = 'PuzzlePlatformCloseToConfBoundaryEdge';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzlePlatformCloseToConfBoundaryEdge.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.edge = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzlePlatformCloseToConfBoundaryEdge.EdgeType" };
      this.edge = this._io.readU2be();
      this._debug.edge.end = this._io.pos;
    }

    return PuzzlePlatformCloseToConfBoundaryEdge;
  })();

  var VentDutyCycle = GloverLevel.VentDutyCycle = (function() {
    function VentDutyCycle(_io, _parent, _root) {
      this.__type = 'VentDutyCycle';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    VentDutyCycle.prototype._read = function() {
      this._debug.framesOff = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.framesOff = this._io.readS2be();
      this._debug.framesOff.end = this._io.pos;
      this._debug.framesOn = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.framesOn = this._io.readS2be();
      this._debug.framesOn.end = this._io.pos;
    }

    return VentDutyCycle;
  })();

  var Plat0xc3 = GloverLevel.Plat0xc3 = (function() {
    function Plat0xc3(_io, _parent, _root) {
      this.__type = 'Plat0xc3';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Plat0xc3.prototype._read = function() {
      this._debug.u160x86 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x86 = this._io.readU2be();
      this._debug.u160x86.end = this._io.pos;
      this._debug.u320x780x80 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x780x80 = this._io.readU2be();
      this._debug.u320x780x80.end = this._io.pos;
      this._debug.u160x84 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x84 = this._io.readU2be();
      this._debug.u160x84.end = this._io.pos;
    }

    return Plat0xc3;
  })();

  var SetGravity = GloverLevel.SetGravity = (function() {
    function SetGravity(_io, _parent, _root) {
      this.__type = 'SetGravity';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    SetGravity.prototype._read = function() {
      this._debug.strength = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.strength = this._io.readF4be();
      this._debug.strength.end = this._io.pos;
    }

    return SetGravity;
  })();

  var EndLevelData = GloverLevel.EndLevelData = (function() {
    function EndLevelData(_io, _parent, _root) {
      this.__type = 'EndLevelData';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EndLevelData.prototype._read = function() {
    }

    return EndLevelData;
  })();

  var PuzzleActionPlatformMoveToPointIdxMinusOne = GloverLevel.PuzzleActionPlatformMoveToPointIdxMinusOne = (function() {
    function PuzzleActionPlatformMoveToPointIdxMinusOne(_io, _parent, _root) {
      this.__type = 'PuzzleActionPlatformMoveToPointIdxMinusOne';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionPlatformMoveToPointIdxMinusOne.prototype._read = function() {
      this._debug.pointIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.pointIdx = this._io.readU4be();
      this._debug.pointIdx.end = this._io.pos;
      this._debug.platformTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platformTag = this._io.readS2be();
      this._debug.platformTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.GenericFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionPlatformMoveToPointIdxMinusOne;
  })();

  var SetObjectSparkle = GloverLevel.SetObjectSparkle = (function() {
    function SetObjectSparkle(_io, _parent, _root) {
      this.__type = 'SetObjectSparkle';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    SetObjectSparkle.prototype._read = function() {
      this._debug.period = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.period = this._io.readU2be();
      this._debug.period.end = this._io.pos;
    }

    return SetObjectSparkle;
  })();

  var PuzzleActionCameraLookAtGlover = GloverLevel.PuzzleActionCameraLookAtGlover = (function() {
    function PuzzleActionCameraLookAtGlover(_io, _parent, _root) {
      this.__type = 'PuzzleActionCameraLookAtGlover';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionCameraLookAtGlover.prototype._read = function() {
      this._debug.angle = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.angle = this._io.readF4be();
      this._debug.angle.end = this._io.pos;
      this._debug.distance = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.distance = this._io.readF4be();
      this._debug.distance.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
    }

    return PuzzleActionCameraLookAtGlover;
  })();

  var PlatFan0x8a = GloverLevel.PlatFan0x8a = (function() {
    function PlatFan0x8a(_io, _parent, _root) {
      this.__type = 'PlatFan0x8a';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatFan0x8a.prototype._read = function() {
      this._debug.enabled = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.enabled = this._io.readU2be();
      this._debug.enabled.end = this._io.pos;
      this._debug.forceVectorX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.forceVectorX = this._io.readF4be();
      this._debug.forceVectorX.end = this._io.pos;
      this._debug.forceVectorY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.forceVectorY = this._io.readF4be();
      this._debug.forceVectorY.end = this._io.pos;
      this._debug.forceVectorZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.forceVectorZ = this._io.readF4be();
      this._debug.forceVectorZ.end = this._io.pos;
      this._debug.u320x10 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x10 = this._io.readU4be();
      this._debug.u320x10.end = this._io.pos;
      this._debug.forceMinThreshold = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.forceMinThreshold = this._io.readF4be();
      this._debug.forceMinThreshold.end = this._io.pos;
      this._debug.u320x18 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x18 = this._io.readU4be();
      this._debug.u320x18.end = this._io.pos;
      this._debug.forceVectorMagnitude = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.forceVectorMagnitude = this._io.readF4be();
      this._debug.forceVectorMagnitude.end = this._io.pos;
    }

    return PlatFan0x8a;
  })();

  var PuzzleActionRegAdd = GloverLevel.PuzzleActionRegAdd = (function() {
    function PuzzleActionRegAdd(_io, _parent, _root) {
      this.__type = 'PuzzleActionRegAdd';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionRegAdd.prototype._read = function() {
      this._debug.immValOrSrcReg = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.immValOrSrcReg = this._io.readF4be();
      this._debug.immValOrSrcReg.end = this._io.pos;
      this._debug.dstReg = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.dstReg = this._io.readU2be();
      this._debug.dstReg.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.RegisterFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionRegAdd;
  })();

  var PlatSpinSound0xc5 = GloverLevel.PlatSpinSound0xc5 = (function() {
    function PlatSpinSound0xc5(_io, _parent, _root) {
      this.__type = 'PlatSpinSound0xc5';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSpinSound0xc5.prototype._read = function() {
      this._debug.soundId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.soundId = this._io.readU2be();
      this._debug.soundId.end = this._io.pos;
      this._debug.volume = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.volume = this._io.readU2be();
      this._debug.volume.end = this._io.pos;
      this._debug.pitch = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.pitch = this._io.readU2be();
      this._debug.pitch.end = this._io.pos;
    }

    return PlatSpinSound0xc5;
  })();

  var EnemyInstructionTurn = GloverLevel.EnemyInstructionTurn = (function() {
    function EnemyInstructionTurn(_io, _parent, _root) {
      this.__type = 'EnemyInstructionTurn';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyInstructionTurn.prototype._read = function() {
      this._debug.lookatX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.lookatX = this._io.readF4be();
      this._debug.lookatX.end = this._io.pos;
      this._debug.lookatY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.lookatY = this._io.readF4be();
      this._debug.lookatY.end = this._io.pos;
      this._debug.lookatZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.lookatZ = this._io.readF4be();
      this._debug.lookatZ.end = this._io.pos;
      this._debug.chooseRandomDirection = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.chooseRandomDirection = this._io.readU4be();
      this._debug.chooseRandomDirection.end = this._io.pos;
    }

    return EnemyInstructionTurn;
  })();

  var CameoLightningFlash = GloverLevel.CameoLightningFlash = (function() {
    function CameoLightningFlash(_io, _parent, _root) {
      this.__type = 'CameoLightningFlash';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    CameoLightningFlash.prototype._read = function() {
      this._debug.reserved = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.reserved = this._io.readU2be();
      this._debug.reserved.end = this._io.pos;
      this._debug.durationMin = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.durationMin = this._io.readU2be();
      this._debug.durationMin.end = this._io.pos;
      this._debug.durationRange = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.durationRange = this._io.readU2be();
      this._debug.durationRange.end = this._io.pos;
    }

    return CameoLightningFlash;
  })();

  var PuzzleActionEnemySetAiInstruction = GloverLevel.PuzzleActionEnemySetAiInstruction = (function() {
    function PuzzleActionEnemySetAiInstruction(_io, _parent, _root) {
      this.__type = 'PuzzleActionEnemySetAiInstruction';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionEnemySetAiInstruction.prototype._read = function() {
      this._debug.instructionIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.instructionIdx = this._io.readU4be();
      this._debug.instructionIdx.end = this._io.pos;
      this._debug.puzzleTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.puzzleTag = this._io.readS2be();
      this._debug.puzzleTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.GenericFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionEnemySetAiInstruction;
  })();

  var EnemyConditionalInstruction = GloverLevel.EnemyConditionalInstruction = (function() {
    function EnemyConditionalInstruction(_io, _parent, _root) {
      this.__type = 'EnemyConditionalInstruction';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyConditionalInstruction.prototype._read = function() {
      this._debug.instr = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.instr = new EnemyInstruction(this._io, this, this._root);
      this._debug.instr.end = this._io.pos;
    }

    return EnemyConditionalInstruction;
  })();

  var PuzzleCondGloverWithinRangeOfPoint2 = GloverLevel.PuzzleCondGloverWithinRangeOfPoint2 = (function() {
    function PuzzleCondGloverWithinRangeOfPoint2(_io, _parent, _root) {
      this.__type = 'PuzzleCondGloverWithinRangeOfPoint2';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondGloverWithinRangeOfPoint2.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.range = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.range = this._io.readF4be();
      this._debug.range.end = this._io.pos;
      this._debug.maxY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.maxY = this._io.readF4be();
      this._debug.maxY.end = this._io.pos;
      this._debug.minY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.minY = this._io.readF4be();
      this._debug.minY.end = this._io.pos;
    }

    return PuzzleCondGloverWithinRangeOfPoint2;
  })();

  var PuzzleCondBallWithinRangeOfPoint = GloverLevel.PuzzleCondBallWithinRangeOfPoint = (function() {
    function PuzzleCondBallWithinRangeOfPoint(_io, _parent, _root) {
      this.__type = 'PuzzleCondBallWithinRangeOfPoint';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondBallWithinRangeOfPoint.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.range = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.range = this._io.readF4be();
      this._debug.range.end = this._io.pos;
    }

    return PuzzleCondBallWithinRangeOfPoint;
  })();

  var PuzzleActionCameraFlyTowardsPointRelativeToGlover = GloverLevel.PuzzleActionCameraFlyTowardsPointRelativeToGlover = (function() {
    function PuzzleActionCameraFlyTowardsPointRelativeToGlover(_io, _parent, _root) {
      this.__type = 'PuzzleActionCameraFlyTowardsPointRelativeToGlover';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionCameraFlyTowardsPointRelativeToGlover.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.distance = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.distance = this._io.readF4be();
      this._debug.distance.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
    }

    return PuzzleActionCameraFlyTowardsPointRelativeToGlover;
  })();

  var AmbientSoundAtPoint = GloverLevel.AmbientSoundAtPoint = (function() {
    function AmbientSoundAtPoint(_io, _parent, _root) {
      this.__type = 'AmbientSoundAtPoint';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    AmbientSoundAtPoint.prototype._read = function() {
      this._debug.soundId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.soundId = this._io.readU2be();
      this._debug.soundId.end = this._io.pos;
      this._debug.volume = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.volume = this._io.readU2be();
      this._debug.volume.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.flags = this._io.readU2be();
      this._debug.flags.end = this._io.pos;
      this._debug.h0x06 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.h0x06 = this._io.readU2be();
      this._debug.h0x06.end = this._io.pos;
      this._debug.h0x08 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.h0x08 = this._io.readU2be();
      this._debug.h0x08.end = this._io.pos;
      this._debug.h0x0a = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.h0x0a = this._io.readU2be();
      this._debug.h0x0a.end = this._io.pos;
      this._debug.platformTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platformTag = this._io.readU2be();
      this._debug.platformTag.end = this._io.pos;
      this._debug.h0x0e = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.h0x0e = this._io.readU2be();
      this._debug.h0x0e.end = this._io.pos;
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.radius = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.radius = this._io.readF4be();
      this._debug.radius.end = this._io.pos;
    }

    return AmbientSoundAtPoint;
  })();

  var PuzzleActionCameraTurnTowardsFocus = GloverLevel.PuzzleActionCameraTurnTowardsFocus = (function() {
    function PuzzleActionCameraTurnTowardsFocus(_io, _parent, _root) {
      this.__type = 'PuzzleActionCameraTurnTowardsFocus';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionCameraTurnTowardsFocus.prototype._read = function() {
      this._debug.reserved = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.reserved = this._io.readF4be();
      this._debug.reserved.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
    }

    return PuzzleActionCameraTurnTowardsFocus;
  })();

  var PlatSetTag = GloverLevel.PlatSetTag = (function() {
    function PlatSetTag(_io, _parent, _root) {
      this.__type = 'PlatSetTag';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSetTag.prototype._read = function() {
      this._debug.tag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.tag = this._io.readU2be();
      this._debug.tag.end = this._io.pos;
    }

    return PlatSetTag;
  })();

  var PlatCopySpinFromParent = GloverLevel.PlatCopySpinFromParent = (function() {
    function PlatCopySpinFromParent(_io, _parent, _root) {
      this.__type = 'PlatCopySpinFromParent';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatCopySpinFromParent.prototype._read = function() {
    }

    return PlatCopySpinFromParent;
  })();

  var PuzzleActionSetFog = GloverLevel.PuzzleActionSetFog = (function() {
    function PuzzleActionSetFog(_io, _parent, _root) {
      this.__type = 'PuzzleActionSetFog';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionSetFog.prototype._read = function() {
      this._debug.r = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.r = this._io.readU2be();
      this._debug.r.end = this._io.pos;
      this._debug.g = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.g = this._io.readU2be();
      this._debug.g.end = this._io.pos;
      this._debug.b = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.b = this._io.readU2be();
      this._debug.b.end = this._io.pos;
      this._debug.minZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.minZ = this._io.readU2be();
      this._debug.minZ.end = this._io.pos;
      this._debug.u160x1c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x1c = this._io.readU2be();
      this._debug.u160x1c.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
    }

    return PuzzleActionSetFog;
  })();

  var PuzzleActionPlatformConfigSpin = GloverLevel.PuzzleActionPlatformConfigSpin = (function() {
    function PuzzleActionPlatformConfigSpin(_io, _parent, _root) {
      this.__type = 'PuzzleActionPlatformConfigSpin';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionPlatformConfigSpin.prototype._read = function() {
      this._debug.velocity = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velocity = this._io.readF4be();
      this._debug.velocity.end = this._io.pos;
      this._debug.platformTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platformTag = this._io.readS2be();
      this._debug.platformTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.PlatformMovementFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionPlatformConfigSpin;
  })();

  var Vent = GloverLevel.Vent = (function() {
    function Vent(_io, _parent, _root) {
      this.__type = 'Vent';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Vent.prototype._read = function() {
      this._debug.type = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.type = this._io.readU2be();
      this._debug.type.end = this._io.pos;
      this._debug.puzzleTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.puzzleTag = this._io.readU2be();
      this._debug.puzzleTag.end = this._io.pos;
      this._debug.parentTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.parentTag = this._io.readU2be();
      this._debug.parentTag.end = this._io.pos;
      this._debug.originX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.originX = this._io.readF4be();
      this._debug.originX.end = this._io.pos;
      this._debug.originY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.originY = this._io.readF4be();
      this._debug.originY.end = this._io.pos;
      this._debug.originZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.originZ = this._io.readF4be();
      this._debug.originZ.end = this._io.pos;
      this._debug.particleVelocityX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.particleVelocityX = this._io.readF4be();
      this._debug.particleVelocityX.end = this._io.pos;
      this._debug.particleVelocityY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.particleVelocityY = this._io.readF4be();
      this._debug.particleVelocityY.end = this._io.pos;
      this._debug.particleVelocityZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.particleVelocityZ = this._io.readF4be();
      this._debug.particleVelocityZ.end = this._io.pos;
    }

    return Vent;
  })();

  var PuzzleCond = GloverLevel.PuzzleCond = (function() {
    function PuzzleCond(_io, _parent, _root) {
      this.__type = 'PuzzleCond';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCond.prototype._read = function() {
      this._debug.condType = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.condType = this._io.readU2be();
      this._debug.condType.end = this._io.pos;
      this._debug.body = { start: this._io.pos, ioOffset: this._io.byteOffset };
      switch (this.condType) {
      case 14:
        this.body = new PuzzleCondPlatformOrbit2Todo(this._io, this, this._root);
        break;
      case 10:
        this.body = new PuzzleCondPlatformSpinTodo(this._io, this, this._root);
        break;
      case 17:
        this.body = new PuzzleCondBallPlatformTodo(this._io, this, this._root);
        break;
      case 42:
        this.body = new PuzzleCondPlatformDoesntExist(this._io, this, this._root);
        break;
      case 39:
        this.body = new PuzzleCondCameraWithinVolume(this._io, this, this._root);
        break;
      case 24:
        this.body = new PuzzleCondBallChangedTouchingPlatform(this._io, this, this._root);
        break;
      case 35:
        this.body = new PuzzleCondGloverWithinVolume(this._io, this, this._root);
        break;
      case 32:
        this.body = new PuzzlePlatformCloseToConfBoundaryEdge(this._io, this, this._root);
        break;
      case 13:
        this.body = new PuzzleCondPlatformSpin2Todo(this._io, this, this._root);
        break;
      case 11:
        this.body = new PuzzleCondPlatformOrbitTodo(this._io, this, this._root);
        break;
      case 12:
        this.body = new PuzzleCondPlatformPathAtPoint2(this._io, this, this._root);
        break;
      case 23:
        this.body = new PuzzleCondBallIsTouchingPlatform(this._io, this, this._root);
        break;
      case 15:
        this.body = new PuzzleCondGloverStandingOnPlatform(this._io, this, this._root);
        break;
      case 38:
        this.body = new PuzzleCondBallWithinRangeOfPoint(this._io, this, this._root);
        break;
      case 40:
        this.body = new PuzzleCondCameraWithinRangeOfPoint(this._io, this, this._root);
        break;
      case 9:
        this.body = new PuzzleCondPlatformPathAtPointAtRest(this._io, this, this._root);
        break;
      case 21:
        this.body = new PuzzleCondGloverIsTouchingPlatform(this._io, this, this._root);
        break;
      case 37:
        this.body = new PuzzleCondBallWithinVolume(this._io, this, this._root);
        break;
      case 41:
        this.body = new PuzzleCondGloverWithinRangeOfPoint2(this._io, this, this._root);
        break;
      case 36:
        this.body = new PuzzleCondGloverWithinRangeOfPoint(this._io, this, this._root);
        break;
      case 16:
        this.body = new PuzzleCondGloverPlatform2Todo(this._io, this, this._root);
        break;
      case 18:
        this.body = new PuzzleCondBallPlatform2Todo(this._io, this, this._root);
        break;
      case 26:
        this.body = new PuzzleCondEnemyChangedTouchingPlatform(this._io, this, this._root);
        break;
      case 31:
        this.body = new PuzzlePlatformTouchingConfBoundaryEdge(this._io, this, this._root);
        break;
      case 34:
        this.body = new PuzzleCond0x22(this._io, this, this._root);
        break;
      case 25:
        this.body = new PuzzleCondEnemyIsTouchingPlatform(this._io, this, this._root);
        break;
      case 22:
        this.body = new PuzzleCondGloverChangedTouchingPlatform(this._io, this, this._root);
        break;
      default:
        this.body = new PuzzleCondDefault(this._io, this, this._root);
        break;
      }
      this._debug.body.end = this._io.pos;
    }

    return PuzzleCond;
  })();

  var PlatMvspn0x73 = GloverLevel.PlatMvspn0x73 = (function() {
    function PlatMvspn0x73(_io, _parent, _root) {
      this.__type = 'PlatMvspn0x73';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatMvspn0x73.prototype._read = function() {
      this._debug.u160x0c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x0c = this._io.readU2be();
      this._debug.u160x0c.end = this._io.pos;
      this._debug.u320x34 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x34 = this._io.readU4be();
      this._debug.u320x34.end = this._io.pos;
      this._debug.u320x38 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x38 = this._io.readU4be();
      this._debug.u320x38.end = this._io.pos;
      this._debug.u320x3c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x3c = this._io.readU4be();
      this._debug.u320x3c.end = this._io.pos;
    }

    return PlatMvspn0x73;
  })();

  var EnemyInstructionAttack = GloverLevel.EnemyInstructionAttack = (function() {
    function EnemyInstructionAttack(_io, _parent, _root) {
      this.__type = 'EnemyInstructionAttack';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyInstructionAttack.prototype._read = function() {
      this._debug.unused1 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.unused1 = this._io.readU4be();
      this._debug.unused1.end = this._io.pos;
      this._debug.unused2 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.unused2 = this._io.readU4be();
      this._debug.unused2.end = this._io.pos;
    }

    return EnemyInstructionAttack;
  })();

  var EnemyInstructionRest = GloverLevel.EnemyInstructionRest = (function() {
    function EnemyInstructionRest(_io, _parent, _root) {
      this.__type = 'EnemyInstructionRest';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyInstructionRest.prototype._read = function() {
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
      this._debug.animStartPlaying = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.animStartPlaying = this._io.readU4be();
      this._debug.animStartPlaying.end = this._io.pos;
    }

    return EnemyInstructionRest;
  })();

  var PuzzleActionSetPlatformPathDirection = GloverLevel.PuzzleActionSetPlatformPathDirection = (function() {
    function PuzzleActionSetPlatformPathDirection(_io, _parent, _root) {
      this.__type = 'PuzzleActionSetPlatformPathDirection';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionSetPlatformPathDirection.prototype._read = function() {
      this._debug.direction = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.direction = this._io.readU4be();
      this._debug.direction.end = this._io.pos;
      this._debug.puzzleTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.puzzleTag = this._io.readU2be();
      this._debug.puzzleTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.PlatformMovementFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionSetPlatformPathDirection;
  })();

  var LookAtBall0x61 = GloverLevel.LookAtBall0x61 = (function() {
    function LookAtBall0x61(_io, _parent, _root) {
      this.__type = 'LookAtBall0x61';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    LookAtBall0x61.prototype._read = function() {
      this._debug.u320x6c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x6c = this._io.readU4be();
      this._debug.u320x6c.end = this._io.pos;
      this._debug.u320x1c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x1c = this._io.readU4be();
      this._debug.u320x1c.end = this._io.pos;
    }

    return LookAtBall0x61;
  })();

  var LookAtHand0x60 = GloverLevel.LookAtHand0x60 = (function() {
    function LookAtHand0x60(_io, _parent, _root) {
      this.__type = 'LookAtHand0x60';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    LookAtHand0x60.prototype._read = function() {
      this._debug.u320x6c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x6c = this._io.readU4be();
      this._debug.u320x6c.end = this._io.pos;
      this._debug.u320x1c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x1c = this._io.readU4be();
      this._debug.u320x1c.end = this._io.pos;
    }

    return LookAtHand0x60;
  })();

  var CameoInst2 = GloverLevel.CameoInst2 = (function() {
    function CameoInst2(_io, _parent, _root) {
      this.__type = 'CameoInst2';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    CameoInst2.prototype._read = function() {
      this._debug.subcommand = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.subcommand = this._io.readS2be();
      this._debug.subcommand.end = this._io.pos;
      this._debug.i0x02 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.i0x02 = this._io.readF4be();
      this._debug.i0x02.end = this._io.pos;
      this._debug.i0x06 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.i0x06 = this._io.readF4be();
      this._debug.i0x06.end = this._io.pos;
      this._debug.i0x0a = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.i0x0a = this._io.readF4be();
      this._debug.i0x0a.end = this._io.pos;
      this._debug.i0x0e = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.i0x0e = this._io.readU4be();
      this._debug.i0x0e.end = this._io.pos;
      this._debug.frameCount = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.frameCount = this._io.readS2be();
      this._debug.frameCount.end = this._io.pos;
      this._debug.precedingInstrIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.precedingInstrIdx = this._io.readS2be();
      this._debug.precedingInstrIdx.end = this._io.pos;
    }

    return CameoInst2;
  })();

  var Unknown = GloverLevel.Unknown = (function() {
    function Unknown(_io, _parent, _root) {
      this.__type = 'Unknown';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Unknown.prototype._read = function() {
      this._debug.body = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.body = this._io.readBytesFull();
      this._debug.body.end = this._io.pos;
    }

    return Unknown;
  })();

  var PlatVentAdvanceFrames = GloverLevel.PlatVentAdvanceFrames = (function() {
    function PlatVentAdvanceFrames(_io, _parent, _root) {
      this.__type = 'PlatVentAdvanceFrames';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatVentAdvanceFrames.prototype._read = function() {
      this._debug.numFrames = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.numFrames = this._io.readU2be();
      this._debug.numFrames.end = this._io.pos;
    }

    return PlatVentAdvanceFrames;
  })();

  var PuzzleCondPlatformPathAtPoint2 = GloverLevel.PuzzleCondPlatformPathAtPoint2 = (function() {
    function PuzzleCondPlatformPathAtPoint2(_io, _parent, _root) {
      this.__type = 'PuzzleCondPlatformPathAtPoint2';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondPlatformPathAtPoint2.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.arg2 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.arg2 = this._io.readS2be();
      this._debug.arg2.end = this._io.pos;
    }

    return PuzzleCondPlatformPathAtPoint2;
  })();

  var SetExit = GloverLevel.SetExit = (function() {
    SetExit.ExitType = Object.freeze({
      LOADING_ZONE: 0,
      SOLID_PLATFORM: 1,

      0: "LOADING_ZONE",
      1: "SOLID_PLATFORM",
    });

    function SetExit(_io, _parent, _root) {
      this.__type = 'SetExit';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    SetExit.prototype._read = function() {
      this._debug.behavior = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.behavior = this._io.readU2be();
      this._debug.behavior.end = this._io.pos;
      this._debug.type = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.SetExit.ExitType" };
      this.type = this._io.readS2be();
      this._debug.type.end = this._io.pos;
    }

    return SetExit;
  })();

  var PuzzleActionSetPlatformVelocity = GloverLevel.PuzzleActionSetPlatformVelocity = (function() {
    function PuzzleActionSetPlatformVelocity(_io, _parent, _root) {
      this.__type = 'PuzzleActionSetPlatformVelocity';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionSetPlatformVelocity.prototype._read = function() {
      this._debug.velX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velX = this._io.readF4be();
      this._debug.velX.end = this._io.pos;
      this._debug.velY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velY = this._io.readF4be();
      this._debug.velY.end = this._io.pos;
      this._debug.velZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velZ = this._io.readF4be();
      this._debug.velZ.end = this._io.pos;
      this._debug.reserved = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.reserved = this._io.readU4be();
      this._debug.reserved.end = this._io.pos;
      this._debug.puzzleTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.puzzleTag = this._io.readU2be();
      this._debug.puzzleTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.PlatformMovementFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionSetPlatformVelocity;
  })();

  var PlatSound0xc1 = GloverLevel.PlatSound0xc1 = (function() {
    function PlatSound0xc1(_io, _parent, _root) {
      this.__type = 'PlatSound0xc1';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSound0xc1.prototype._read = function() {
      this._debug.soundId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.soundId = this._io.readU2be();
      this._debug.soundId.end = this._io.pos;
      this._debug.volume = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.volume = this._io.readU2be();
      this._debug.volume.end = this._io.pos;
      this._debug.pitch = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.pitch = this._io.readU2be();
      this._debug.pitch.end = this._io.pos;
    }

    return PlatSound0xc1;
  })();

  var PlatActorEnableWaterAnimation = GloverLevel.PlatActorEnableWaterAnimation = (function() {
    function PlatActorEnableWaterAnimation(_io, _parent, _root) {
      this.__type = 'PlatActorEnableWaterAnimation';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatActorEnableWaterAnimation.prototype._read = function() {
    }

    return PlatActorEnableWaterAnimation;
  })();

  var EnemyInstructionC = GloverLevel.EnemyInstructionC = (function() {
    function EnemyInstructionC(_io, _parent, _root) {
      this.__type = 'EnemyInstructionC';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyInstructionC.prototype._read = function() {
      this._debug.u320x02 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x02 = this._io.readU4be();
      this._debug.u320x02.end = this._io.pos;
      this._debug.u320x0e = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x0e = this._io.readU4be();
      this._debug.u320x0e.end = this._io.pos;
    }

    return EnemyInstructionC;
  })();

  var PuzzleActionRegSub = GloverLevel.PuzzleActionRegSub = (function() {
    function PuzzleActionRegSub(_io, _parent, _root) {
      this.__type = 'PuzzleActionRegSub';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionRegSub.prototype._read = function() {
      this._debug.immValOrSrcReg = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.immValOrSrcReg = this._io.readF4be();
      this._debug.immValOrSrcReg.end = this._io.pos;
      this._debug.dstReg = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.dstReg = this._io.readU2be();
      this._debug.dstReg.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.RegisterFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionRegSub;
  })();

  var PuzzleAnd = GloverLevel.PuzzleAnd = (function() {
    function PuzzleAnd(_io, _parent, _root) {
      this.__type = 'PuzzleAnd';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleAnd.prototype._read = function() {
    }

    return PuzzleAnd;
  })();

  var PuzzleActionCameraSetDistance = GloverLevel.PuzzleActionCameraSetDistance = (function() {
    function PuzzleActionCameraSetDistance(_io, _parent, _root) {
      this.__type = 'PuzzleActionCameraSetDistance';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionCameraSetDistance.prototype._read = function() {
      this._debug.distance = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.distance = this._io.readF4be();
      this._debug.distance.end = this._io.pos;
      this._debug.reserved = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.reserved = this._io.readU2be();
      this._debug.reserved.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.CameraFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionCameraSetDistance;
  })();

  var PuzzleCondGloverPlatform2Todo = GloverLevel.PuzzleCondGloverPlatform2Todo = (function() {
    function PuzzleCondGloverPlatform2Todo(_io, _parent, _root) {
      this.__type = 'PuzzleCondGloverPlatform2Todo';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondGloverPlatform2Todo.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.arg2 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.arg2 = this._io.readS2be();
      this._debug.arg2.end = this._io.pos;
    }

    return PuzzleCondGloverPlatform2Todo;
  })();

  var PlatSpecial0xc7 = GloverLevel.PlatSpecial0xc7 = (function() {
    function PlatSpecial0xc7(_io, _parent, _root) {
      this.__type = 'PlatSpecial0xc7';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSpecial0xc7.prototype._read = function() {
      this._debug.u160x2a = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x2a = this._io.readU2be();
      this._debug.u160x2a.end = this._io.pos;
      this._debug.u160x1cAnd0x24 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x1cAnd0x24 = this._io.readU2be();
      this._debug.u160x1cAnd0x24.end = this._io.pos;
      this._debug.u160x28 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x28 = this._io.readU2be();
      this._debug.u160x28.end = this._io.pos;
    }

    return PlatSpecial0xc7;
  })();

  var PuzzleCondBallWithinVolume = GloverLevel.PuzzleCondBallWithinVolume = (function() {
    function PuzzleCondBallWithinVolume(_io, _parent, _root) {
      this.__type = 'PuzzleCondBallWithinVolume';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondBallWithinVolume.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.l = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.l = this._io.readF4be();
      this._debug.l.end = this._io.pos;
      this._debug.w = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.w = this._io.readF4be();
      this._debug.w.end = this._io.pos;
      this._debug.h = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.h = this._io.readF4be();
      this._debug.h.end = this._io.pos;
    }

    return PuzzleCondBallWithinVolume;
  })();

  var PuzzleActionTogglePlatformPhysics = GloverLevel.PuzzleActionTogglePlatformPhysics = (function() {
    function PuzzleActionTogglePlatformPhysics(_io, _parent, _root) {
      this.__type = 'PuzzleActionTogglePlatformPhysics';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionTogglePlatformPhysics.prototype._read = function() {
      this._debug.physicsEnabled = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.physicsEnabled = this._io.readU4be();
      this._debug.physicsEnabled.end = this._io.pos;
      this._debug.platformTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platformTag = this._io.readS2be();
      this._debug.platformTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.GenericFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionTogglePlatformPhysics;
  })();

  var NullPlatform = GloverLevel.NullPlatform = (function() {
    function NullPlatform(_io, _parent, _root) {
      this.__type = 'NullPlatform';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    NullPlatform.prototype._read = function() {
    }

    return NullPlatform;
  })();

  var Powerup = GloverLevel.Powerup = (function() {
    function Powerup(_io, _parent, _root) {
      this.__type = 'Powerup';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Powerup.prototype._read = function() {
      this._debug.type = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.type = this._io.readU2be();
      this._debug.type.end = this._io.pos;
      this._debug.u160x02 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x02 = this._io.readU2be();
      this._debug.u160x02.end = this._io.pos;
      this._debug.u160x04 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x04 = this._io.readU2be();
      this._debug.u160x04.end = this._io.pos;
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
    }

    return Powerup;
  })();

  var PlatformConveyor = GloverLevel.PlatformConveyor = (function() {
    function PlatformConveyor(_io, _parent, _root) {
      this.__type = 'PlatformConveyor';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatformConveyor.prototype._read = function() {
      this._debug.velX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velX = this._io.readF4be();
      this._debug.velX.end = this._io.pos;
      this._debug.velY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velY = this._io.readF4be();
      this._debug.velY.end = this._io.pos;
      this._debug.velZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velZ = this._io.readF4be();
      this._debug.velZ.end = this._io.pos;
    }

    return PlatformConveyor;
  })();

  var SetTeleport = GloverLevel.SetTeleport = (function() {
    function SetTeleport(_io, _parent, _root) {
      this.__type = 'SetTeleport';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    SetTeleport.prototype._read = function() {
      this._debug.targetTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.targetTag = this._io.readU2be();
      this._debug.targetTag.end = this._io.pos;
      this._debug.outFramecount = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.outFramecount = this._io.readU2be();
      this._debug.outFramecount.end = this._io.pos;
      this._debug.inFramecount = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.inFramecount = this._io.readU2be();
      this._debug.inFramecount.end = this._io.pos;
      this._debug.u160x12 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x12 = this._io.readU2be();
      this._debug.u160x12.end = this._io.pos;
      this._debug.u320x00 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x00 = this._io.readU4be();
      this._debug.u320x00.end = this._io.pos;
      this._debug.u320x04 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x04 = this._io.readU4be();
      this._debug.u320x04.end = this._io.pos;
      this._debug.u320x08 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x08 = this._io.readU4be();
      this._debug.u320x08.end = this._io.pos;
    }

    return SetTeleport;
  })();

  var PlatCheckpoint = GloverLevel.PlatCheckpoint = (function() {
    function PlatCheckpoint(_io, _parent, _root) {
      this.__type = 'PlatCheckpoint';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatCheckpoint.prototype._read = function() {
      this._debug.u160x17 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x17 = this._io.readU2be();
      this._debug.u160x17.end = this._io.pos;
      this._debug.theta = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.theta = this._io.readF4be();
      this._debug.theta.end = this._io.pos;
    }

    return PlatCheckpoint;
  })();

  var BallSpawnPoint = GloverLevel.BallSpawnPoint = (function() {
    function BallSpawnPoint(_io, _parent, _root) {
      this.__type = 'BallSpawnPoint';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    BallSpawnPoint.prototype._read = function() {
      this._debug.type = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.type = this._io.readU2be();
      this._debug.type.end = this._io.pos;
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
    }

    return BallSpawnPoint;
  })();

  var PlatSetParent = GloverLevel.PlatSetParent = (function() {
    function PlatSetParent(_io, _parent, _root) {
      this.__type = 'PlatSetParent';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSetParent.prototype._read = function() {
      this._debug.tag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.tag = this._io.readU2be();
      this._debug.tag.end = this._io.pos;
    }

    return PlatSetParent;
  })();

  var PuzzleOr = GloverLevel.PuzzleOr = (function() {
    function PuzzleOr(_io, _parent, _root) {
      this.__type = 'PuzzleOr';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleOr.prototype._read = function() {
    }

    return PuzzleOr;
  })();

  var Cmd = GloverLevel.Cmd = (function() {
    function Cmd(_io, _parent, _root) {
      this.__type = 'Cmd';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Cmd.prototype._read = function() {
      this._debug.typeCode = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.typeCode = this._io.readU2be();
      this._debug.typeCode.end = this._io.pos;
      this._debug.params = { start: this._io.pos, ioOffset: this._io.byteOffset };
      switch (this.typeCode) {
      case 120:
        this.params = new Plat0x78(this._io, this, this._root);
        break;
      case 141:
        this.params = new Rope(this._io, this, this._root);
        break;
      case 93:
        this.params = new NullPlatform(this._io, this, this._root);
        break;
      case 118:
        this.params = new PlatOrbitPause(this._io, this, this._root);
        break;
      case 159:
        this.params = new Plat0x9f(this._io, this, this._root);
        break;
      case 194:
        this.params = new PlatSound0xc2(this._io, this, this._root);
        break;
      case 184:
        this.params = new PlatSpecial0xb8(this._io, this, this._root);
        break;
      case 105:
        this.params = new PlatCat0x69(this._io, this, this._root);
        break;
      case 142:
        this.params = new PlatCauseDamage(this._io, this, this._root);
        break;
      case 112:
        this.params = new PlatRocking(this._io, this, this._root);
        break;
      case 163:
        this.params = new VentDutyCycle(this._io, this, this._root);
        break;
      case 131:
        this.params = new Enemy(this._io, this, this._root);
        break;
      case 0:
        this.params = new Noop(this._io, this, this._root);
        break;
      case 167:
        this.params = new PlatPos0xa7(this._io, this, this._root);
        break;
      case 146:
        this.params = new LandActor(this._io, this, this._root);
        break;
      case 4:
        this.params = new Puzzle(this._io, this, this._root);
        break;
      case 169:
        this.params = new SetGravity(this._io, this, this._root);
        break;
      case 162:
        this.params = new Vent(this._io, this, this._root);
        break;
      case 116:
        this.params = new PlatMvspn0x74(this._io, this, this._root);
        break;
      case 119:
        this.params = new PlatOrbitFlip0x77(this._io, this, this._root);
        break;
      case 6:
        this.params = new PuzzleOr(this._io, this, this._root);
        break;
      case 7:
        this.params = new PuzzleNumtimes(this._io, this, this._root);
        break;
      case 113:
        this.params = new PlatSetParent(this._io, this, this._root);
        break;
      case 121:
        this.params = new PlatScale(this._io, this, this._root);
        break;
      case 96:
        this.params = new LookAtHand0x60(this._io, this, this._root);
        break;
      case 191:
        this.params = new Actor0xbf(this._io, this, this._root);
        break;
      case 1:
        this.params = new GloverSpawnPoint(this._io, this, this._root);
        break;
      case 150:
        this.params = new PuzzleAction(this._io, this, this._root);
        break;
      case 97:
        this.params = new LookAtBall0x61(this._io, this, this._root);
        break;
      case 106:
        this.params = new PlatActorSurfaceType(this._io, this, this._root);
        break;
      case 145:
        this.params = new BackgroundActor(this._io, this, this._root);
        break;
      case 101:
        this.params = new PlatDestructible(this._io, this, this._root);
        break;
      case 144:
        this.params = new PlatSine(this._io, this, this._root);
        break;
      case 127:
        this.params = new PlatConstantSpin(this._io, this, this._root);
        break;
      case 100:
        this.params = new PlatNoClip(this._io, this, this._root);
        break;
      case 149:
        this.params = new PuzzleCond(this._io, this, this._root);
        break;
      case 115:
        this.params = new PlatMvspn0x73(this._io, this, this._root);
        break;
      case 91:
        this.params = new PlatPush0x5b(this._io, this, this._root);
        break;
      case 107:
        this.params = new PlatPathPoint(this._io, this, this._root);
        break;
      case 143:
        this.params = new PlatOrbit(this._io, this, this._root);
        break;
      case 89:
        this.params = new PlatMvspn0x59(this._io, this, this._root);
        break;
      case 104:
        this.params = new PlatformConveyor(this._io, this, this._root);
        break;
      case 98:
        this.params = new Platform(this._io, this, this._root);
        break;
      case 197:
        this.params = new PlatSpinSound0xc5(this._io, this, this._root);
        break;
      case 95:
        this.params = new PlatGoForwards0x5f(this._io, this, this._root);
        break;
      case 137:
        this.params = new SetTeleport(this._io, this, this._root);
        break;
      case 88:
        this.params = new PlatMvspn0x58(this._io, this, this._root);
        break;
      case 161:
        this.params = new EnemySetAttentionBbox(this._io, this, this._root);
        break;
      case 138:
        this.params = new PlatFan0x8a(this._io, this, this._root);
        break;
      case 3:
        this.params = new CameraSpawnPoint(this._io, this, this._root);
        break;
      case 192:
        this.params = new PlatPlayObjectAnimation(this._io, this, this._root);
        break;
      case 126:
        this.params = new Plat0x7e(this._io, this, this._root);
        break;
      case 165:
        this.params = new FogConfiguration(this._io, this, this._root);
        break;
      case 5:
        this.params = new PuzzleAnd(this._io, this, this._root);
        break;
      case 103:
        this.params = new PlatCrumb0x67(this._io, this, this._root);
        break;
      case 99:
        this.params = new PlatCheckpoint(this._io, this, this._root);
        break;
      case 185:
        this.params = new PlatSpecial0xb9(this._io, this, this._root);
        break;
      case 180:
        this.params = new SetObjectSparkle(this._io, this, this._root);
        break;
      case 156:
        this.params = new EnemyAttackInstruction(this._io, this, this._root);
        break;
      case 125:
        this.params = new PlatSpinFlip(this._io, this, this._root);
        break;
      case 186:
        this.params = new Enemy0xba(this._io, this, this._root);
        break;
      case 188:
        this.params = new AnimatedBackgroundActor(this._io, this, this._root);
        break;
      case 153:
        this.params = new Backdrop(this._io, this, this._root);
        break;
      case 123:
        this.params = new PlatCopySpinFromParent(this._io, this, this._root);
        break;
      case 160:
        this.params = new Water(this._io, this, this._root);
        break;
      case 8:
        this.params = new PuzzleAny(this._io, this, this._root);
        break;
      case 166:
        this.params = new PlatSetInitialPos(this._io, this, this._root);
        break;
      case 114:
        this.params = new PlatConfBoundaryVolume(this._io, this, this._root);
        break;
      case 181:
        this.params = new Buzzer(this._io, this, this._root);
        break;
      case 148:
        this.params = new SetActorScale(this._io, this, this._root);
        break;
      case 158:
        this.params = new PlatSpecial0x9e(this._io, this, this._root);
        break;
      case 117:
        this.params = new PlatOrbitAroundPoint(this._io, this, this._root);
        break;
      case 152:
        this.params = new AmbientLight(this._io, this, this._root);
        break;
      case 94:
        this.params = new PlatTurnTowardsPathPoint(this._io, this, this._root);
        break;
      case 109:
        this.params = new PlatPathAcceleration(this._io, this, this._root);
        break;
      case 32000:
        this.params = new EndLevelData(this._io, this, this._root);
        break;
      case 140:
        this.params = new Wind(this._io, this, this._root);
        break;
      case 122:
        this.params = new PlatStr0x7a(this._io, this, this._root);
        break;
      case 179:
        this.params = new PlatActorEnableWaterAnimation(this._io, this, this._root);
        break;
      case 195:
        this.params = new Plat0xc3(this._io, this, this._root);
        break;
      case 130:
        this.params = new PlatSpike(this._io, this, this._root);
        break;
      case 187:
        this.params = new MrTip(this._io, this, this._root);
        break;
      case 170:
        this.params = new Cameo(this._io, this, this._root);
        break;
      case 199:
        this.params = new PlatSpecial0xc7(this._io, this, this._root);
        break;
      case 164:
        this.params = new Plat0xa4(this._io, this, this._root);
        break;
      case 182:
        this.params = new BuzzerDutyCycle(this._io, this, this._root);
        break;
      case 108:
        this.params = new PlatMaxVelocity(this._io, this, this._root);
        break;
      case 189:
        this.params = new AmbientSound(this._io, this, this._root);
        break;
      case 168:
        this.params = new SetExit(this._io, this, this._root);
        break;
      case 171:
        this.params = new CameoInst(this._io, this, this._root);
        break;
      case 193:
        this.params = new PlatSound0xc1(this._io, this, this._root);
        break;
      case 133:
        this.params = new GaribGroup(this._io, this, this._root);
        break;
      case 129:
        this.params = new PlatTopple0x81(this._io, this, this._root);
        break;
      case 151:
        this.params = new DiffuseLight(this._io, this, this._root);
        break;
      case 157:
        this.params = new Plat0x9d(this._io, this, this._root);
        break;
      case 147:
        this.params = new SetActorRotation(this._io, this, this._root);
        break;
      case 134:
        this.params = new Garib(this._io, this, this._root);
        break;
      case 102:
        this.params = new PlatReverseAtEndsOfPath(this._io, this, this._root);
        break;
      case 110:
        this.params = new PlatSpecial0x6e(this._io, this, this._root);
        break;
      case 139:
        this.params = new PlatMagnet0x8b(this._io, this, this._root);
        break;
      case 155:
        this.params = new EnemyConditionalInstruction(this._io, this, this._root);
        break;
      case 2:
        this.params = new BallSpawnPoint(this._io, this, this._root);
        break;
      case 135:
        this.params = new Powerup(this._io, this, this._root);
        break;
      case 124:
        this.params = new PlatSpinPause0x7c(this._io, this, this._root);
        break;
      case 200:
        this.params = new PlatDestructibleSound(this._io, this, this._root);
        break;
      case 132:
        this.params = new EnemyFinalize(this._io, this, this._root);
        break;
      case 92:
        this.params = new PlatVentAdvanceFrames(this._io, this, this._root);
        break;
      case 198:
        this.params = new Plat0xc6(this._io, this, this._root);
        break;
      case 111:
        this.params = new PlatSetTag(this._io, this, this._root);
        break;
      case 190:
        this.params = new AmbientSoundAtPoint(this._io, this, this._root);
        break;
      case 196:
        this.params = new PlatOrbitSound0xc4(this._io, this, this._root);
        break;
      case 183:
        this.params = new SetGlobal0xb7(this._io, this, this._root);
        break;
      case 128:
        this.params = new PlatSpin0x80(this._io, this, this._root);
        break;
      case 90:
        this.params = new PlatMvspn0x5a(this._io, this, this._root);
        break;
      case 154:
        this.params = new EnemyNormalInstruction(this._io, this, this._root);
        break;
      default:
        this.params = new Unknown(this._io, this, this._root);
        break;
      }
      this._debug.params.end = this._io.pos;
    }

    return Cmd;
  })();

  var Plat0xc6 = GloverLevel.Plat0xc6 = (function() {
    function Plat0xc6(_io, _parent, _root) {
      this.__type = 'Plat0xc6';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Plat0xc6.prototype._read = function() {
      this._debug.u160x4a = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x4a = this._io.readU2be();
      this._debug.u160x4a.end = this._io.pos;
      this._debug.u160x44 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x44 = this._io.readU2be();
      this._debug.u160x44.end = this._io.pos;
      this._debug.u160x48 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x48 = this._io.readU2be();
      this._debug.u160x48.end = this._io.pos;
    }

    return Plat0xc6;
  })();

  var PuzzleCondEnemyChangedTouchingPlatform = GloverLevel.PuzzleCondEnemyChangedTouchingPlatform = (function() {
    function PuzzleCondEnemyChangedTouchingPlatform(_io, _parent, _root) {
      this.__type = 'PuzzleCondEnemyChangedTouchingPlatform';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondEnemyChangedTouchingPlatform.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.startedOrStopped = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.startedOrStopped = this._io.readS2be();
      this._debug.startedOrStopped.end = this._io.pos;
    }

    return PuzzleCondEnemyChangedTouchingPlatform;
  })();

  var Wind = GloverLevel.Wind = (function() {
    function Wind(_io, _parent, _root) {
      this.__type = 'Wind';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Wind.prototype._read = function() {
      this._debug.left = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.left = this._io.readF4be();
      this._debug.left.end = this._io.pos;
      this._debug.top = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.top = this._io.readF4be();
      this._debug.top.end = this._io.pos;
      this._debug.front = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.front = this._io.readF4be();
      this._debug.front.end = this._io.pos;
      this._debug.width = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.width = this._io.readF4be();
      this._debug.width.end = this._io.pos;
      this._debug.height = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.height = this._io.readF4be();
      this._debug.height.end = this._io.pos;
      this._debug.depth = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.depth = this._io.readF4be();
      this._debug.depth.end = this._io.pos;
      this._debug.velX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velX = this._io.readF4be();
      this._debug.velX.end = this._io.pos;
      this._debug.velY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velY = this._io.readF4be();
      this._debug.velY.end = this._io.pos;
      this._debug.velZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velZ = this._io.readF4be();
      this._debug.velZ.end = this._io.pos;
      this._debug.turbulence = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.turbulence = this._io.readF4be();
      this._debug.turbulence.end = this._io.pos;
      this._debug.unknown0x2c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.unknown0x2c = this._io.readU4be();
      this._debug.unknown0x2c.end = this._io.pos;
      this._debug.active = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.active = this._io.readU4be();
      this._debug.active.end = this._io.pos;
      this._debug.tag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.tag = this._io.readU4be();
      this._debug.tag.end = this._io.pos;
    }

    return Wind;
  })();

  var Puzzle = GloverLevel.Puzzle = (function() {
    function Puzzle(_io, _parent, _root) {
      this.__type = 'Puzzle';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Puzzle.prototype._read = function() {
    }

    return Puzzle;
  })();

  var PlatPush0x5b = GloverLevel.PlatPush0x5b = (function() {
    function PlatPush0x5b(_io, _parent, _root) {
      this.__type = 'PlatPush0x5b';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatPush0x5b.prototype._read = function() {
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.flags = this._io.readU2be();
      this._debug.flags.end = this._io.pos;
      this._debug.u320x04 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x04 = this._io.readU4be();
      this._debug.u320x04.end = this._io.pos;
      this._debug.actorF0x70 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.actorF0x70 = this._io.readF4be();
      this._debug.actorF0x70.end = this._io.pos;
      this._debug.u320x1c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x1c = this._io.readU4be();
      this._debug.u320x1c.end = this._io.pos;
    }

    return PlatPush0x5b;
  })();

  var PlatMvspn0x58 = GloverLevel.PlatMvspn0x58 = (function() {
    function PlatMvspn0x58(_io, _parent, _root) {
      this.__type = 'PlatMvspn0x58';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatMvspn0x58.prototype._read = function() {
      this._debug.u160x14 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x14 = this._io.readU2be();
      this._debug.u160x14.end = this._io.pos;
      this._debug.u320x10 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x10 = this._io.readU4be();
      this._debug.u320x10.end = this._io.pos;
    }

    return PlatMvspn0x58;
  })();

  var PuzzleCond0x22 = GloverLevel.PuzzleCond0x22 = (function() {
    function PuzzleCond0x22(_io, _parent, _root) {
      this.__type = 'PuzzleCond0x22';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCond0x22.prototype._read = function() {
      this._debug.i0x00 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.i0x00 = this._io.readU4be();
      this._debug.i0x00.end = this._io.pos;
      this._debug.i0x04 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.i0x04 = this._io.readU4be();
      this._debug.i0x04.end = this._io.pos;
      this._debug.i0x08 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.i0x08 = this._io.readU4be();
      this._debug.i0x08.end = this._io.pos;
      this._debug.i0x0c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.i0x0c = this._io.readU4be();
      this._debug.i0x0c.end = this._io.pos;
      this._debug.i0x10 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.i0x10 = this._io.readU4be();
      this._debug.i0x10.end = this._io.pos;
      this._debug.i0x14 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.i0x14 = this._io.readU4be();
      this._debug.i0x14.end = this._io.pos;
      this._debug.i0x18 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.i0x18 = this._io.readU4be();
      this._debug.i0x18.end = this._io.pos;
    }

    return PuzzleCond0x22;
  })();

  var PlatDestructible = GloverLevel.PlatDestructible = (function() {
    PlatDestructible.DestructibleFlags = Object.freeze({
      SPAWN_PARTICLES_ON_DESTRUCTION: 4,

      4: "SPAWN_PARTICLES_ON_DESTRUCTION",
    });

    function PlatDestructible(_io, _parent, _root) {
      this.__type = 'PlatDestructible';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatDestructible.prototype._read = function() {
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PlatDestructible.DestructibleFlags" };
      this.flags = this._io.readU2be();
      this._debug.flags.end = this._io.pos;
      this._debug.numFragments = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.numFragments = this._io.readU4be();
      this._debug.numFragments.end = this._io.pos;
      this._debug.fragmentObjectId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.fragmentObjectId = this._io.readU4be();
      this._debug.fragmentObjectId.end = this._io.pos;
      this._debug.name = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.name = KaitaiStream.bytesToStr(this._io.readBytes(8), "ASCII");
      this._debug.name.end = this._io.pos;
    }

    return PlatDestructible;
  })();

  var PuzzleAction = GloverLevel.PuzzleAction = (function() {
    PuzzleAction.GenericFlags = Object.freeze({
      PUZZLE_ACTION_RANDOM_ACTIVATION_DELAY: 512,

      512: "PUZZLE_ACTION_RANDOM_ACTIVATION_DELAY",
    });

    PuzzleAction.CameraFlags = Object.freeze({
      PUZZLE_CAMERA_FREEZE_PLAYER: 1,
      PUZZLE_CAMERA_FREEZE_PARTICLES: 2,
      PUZZLE_CAMERA_FREEZE_ENEMIES: 4,
      PUZZLE_ACTION_RANDOM_ACTIVATION_DELAY: 512,

      1: "PUZZLE_CAMERA_FREEZE_PLAYER",
      2: "PUZZLE_CAMERA_FREEZE_PARTICLES",
      4: "PUZZLE_CAMERA_FREEZE_ENEMIES",
      512: "PUZZLE_ACTION_RANDOM_ACTIVATION_DELAY",
    });

    PuzzleAction.PlatformMovementFlags = Object.freeze({
      PUZZLE_PLATFORM_HALT_AT_END_OF_FIRST_SEGMENT_ONLY: 1,
      PUZZLE_PLATFORM_HALT_AT_SEGMENT_END: 2,
      PUZZLE_PLATFORM_CLIP_CURRENT_VELOCITY: 4,
      PUZZLE_ACTION_RANDOM_ACTIVATION_DELAY: 512,

      1: "PUZZLE_PLATFORM_HALT_AT_END_OF_FIRST_SEGMENT_ONLY",
      2: "PUZZLE_PLATFORM_HALT_AT_SEGMENT_END",
      4: "PUZZLE_PLATFORM_CLIP_CURRENT_VELOCITY",
      512: "PUZZLE_ACTION_RANDOM_ACTIVATION_DELAY",
    });

    PuzzleAction.PlatformToggleFlags = Object.freeze({
      PUZZLE_ACTION_INCLUDE_FANS_AND_MAGNETS: 8,
      PUZZLE_ACTION_INCLUDE_TELEPORTS: 16,
      PUZZLE_ACTION_INCLUDE_CATAPULTS: 32,
      PUZZLE_ACTION_INCLUDE_DAMAGE_PLATFORMS: 64,
      PUZZLE_ACTION_INCLUDE_VENTS: 256,
      PUZZLE_ACTION_RANDOM_ACTIVATION_DELAY: 512,
      PUZZLE_ACTION_INCLUDE_BUZZERS: 1024,

      8: "PUZZLE_ACTION_INCLUDE_FANS_AND_MAGNETS",
      16: "PUZZLE_ACTION_INCLUDE_TELEPORTS",
      32: "PUZZLE_ACTION_INCLUDE_CATAPULTS",
      64: "PUZZLE_ACTION_INCLUDE_DAMAGE_PLATFORMS",
      256: "PUZZLE_ACTION_INCLUDE_VENTS",
      512: "PUZZLE_ACTION_RANDOM_ACTIVATION_DELAY",
      1024: "PUZZLE_ACTION_INCLUDE_BUZZERS",
    });

    PuzzleAction.RegisterFlags = Object.freeze({
      PUZZLE_REGISTER_INDIRECT_ARGUMENT: 128,

      128: "PUZZLE_REGISTER_INDIRECT_ARGUMENT",
    });

    function PuzzleAction(_io, _parent, _root) {
      this.__type = 'PuzzleAction';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleAction.prototype._read = function() {
      this._debug.actionType = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.actionType = this._io.readU2be();
      this._debug.actionType.end = this._io.pos;
      this._debug.body = { start: this._io.pos, ioOffset: this._io.byteOffset };
      switch (this.actionType) {
      case 61:
        this.body = new PuzzleActionSetPlatformVelocity(this._io, this, this._root);
        break;
      case 47:
        this.body = new PuzzleActionPlatformConfigOrbit(this._io, this, this._root);
        break;
      case 73:
        this.body = new PuzzleActionCameraFlyTowardsPoint(this._io, this, this._root);
        break;
      case 46:
        this.body = new PuzzleActionPlatformConfigSpin(this._io, this, this._root);
        break;
      case 81:
        this.body = new PuzzleActionStartCameo(this._io, this, this._root);
        break;
      case 60:
        this.body = new PuzzleActionSpawnEnemy(this._io, this, this._root);
        break;
      case 62:
        this.body = new PuzzleActionCameraLookAtPlatform(this._io, this, this._root);
        break;
      case 55:
        this.body = new PuzzleActionTogglePlatformPhysics(this._io, this, this._root);
        break;
      case 77:
        this.body = new PuzzleActionCameraFlyTowardsPointRelativeToGlover(this._io, this, this._root);
        break;
      case 52:
        this.body = new PuzzleActionControlActiveElements(this._io, this, this._root);
        break;
      case 56:
        this.body = new PuzzleActionRegSet(this._io, this, this._root);
        break;
      case 45:
        this.body = new PuzzleActionPlatformNudge(this._io, this, this._root);
        break;
      case 85:
        this.body = new PuzzleActionSetBackground(this._io, this, this._root);
        break;
      case 67:
        this.body = new PuzzleActionEnemySetAiInstruction(this._io, this, this._root);
        break;
      case 69:
        this.body = new PuzzleActionSpawnGaribGroup(this._io, this, this._root);
        break;
      case 59:
        this.body = new PuzzleActionSpawnPowerup(this._io, this, this._root);
        break;
      case 58:
        this.body = new PuzzleActionRegSub(this._io, this, this._root);
        break;
      case 82:
        this.body = new PuzzleActionSetPlatformPathDirection(this._io, this, this._root);
        break;
      case 86:
        this.body = new PuzzleActionSetFog(this._io, this, this._root);
        break;
      case 84:
        this.body = new PuzzleAction0x54(this._io, this, this._root);
        break;
      case 63:
        this.body = new PuzzleActionCameraLookAtPoint2(this._io, this, this._root);
        break;
      case 51:
        this.body = new PuzzleActionPlatformSpinAlongAxis(this._io, this, this._root);
        break;
      case 83:
        this.body = new PuzzleActionMakeBallInteractive(this._io, this, this._root);
        break;
      case 48:
        this.body = new PuzzleActionPlatformMoveToPointIdxMinusOne(this._io, this, this._root);
        break;
      case 78:
        this.body = new PuzzleActionChangeWaterHeight(this._io, this, this._root);
        break;
      case 53:
        this.body = new PuzzleActionSetConveyor(this._io, this, this._root);
        break;
      case 64:
        this.body = new PuzzleActionCameraLookAtPoint1(this._io, this, this._root);
        break;
      case 65:
        this.body = new PuzzleActionCameraSetDistance(this._io, this, this._root);
        break;
      case 76:
        this.body = new PuzzleAction0x4b0x4c(this._io, this, this._root);
        break;
      case 79:
        this.body = new PuzzleAction0x4f(this._io, this, this._root);
        break;
      case 57:
        this.body = new PuzzleActionRegAdd(this._io, this, this._root);
        break;
      case 72:
        this.body = new PuzzleActionCameraTurnTowardsFocus(this._io, this, this._root);
        break;
      case 71:
        this.body = new PuzzleActionCameraTweenDistance(this._io, this, this._root);
        break;
      case 70:
        this.body = new PuzzleActionCameraTweenYAdjust(this._io, this, this._root);
        break;
      case 74:
        this.body = new PuzzleActionCameraLookAtGlover(this._io, this, this._root);
        break;
      case 80:
        this.body = new PuzzleActionSetGravity(this._io, this, this._root);
        break;
      case 68:
        this.body = new PuzzleActionToggleWind(this._io, this, this._root);
        break;
      case 54:
        this.body = new PuzzleActionHidePlatform(this._io, this, this._root);
        break;
      case 75:
        this.body = new PuzzleAction0x4b0x4c(this._io, this, this._root);
        break;
      default:
        this.body = new PuzzleActionDefault(this._io, this, this._root);
        break;
      }
      this._debug.body.end = this._io.pos;
    }

    return PuzzleAction;
  })();

  var PuzzleActionSpawnPowerup = GloverLevel.PuzzleActionSpawnPowerup = (function() {
    function PuzzleActionSpawnPowerup(_io, _parent, _root) {
      this.__type = 'PuzzleActionSpawnPowerup';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionSpawnPowerup.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.u320x10 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x10 = this._io.readF4be();
      this._debug.u320x10.end = this._io.pos;
      this._debug.type = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.type = this._io.readU2be();
      this._debug.type.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.u320x20 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x20 = this._io.readU4be();
      this._debug.u320x20.end = this._io.pos;
    }

    return PuzzleActionSpawnPowerup;
  })();

  var Noop = GloverLevel.Noop = (function() {
    function Noop(_io, _parent, _root) {
      this.__type = 'Noop';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Noop.prototype._read = function() {
    }

    return Noop;
  })();

  var Water = GloverLevel.Water = (function() {
    function Water(_io, _parent, _root) {
      this.__type = 'Water';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Water.prototype._read = function() {
      this._debug.left = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.left = this._io.readF4be();
      this._debug.left.end = this._io.pos;
      this._debug.top = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.top = this._io.readF4be();
      this._debug.top.end = this._io.pos;
      this._debug.front = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.front = this._io.readF4be();
      this._debug.front.end = this._io.pos;
      this._debug.width = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.width = this._io.readF4be();
      this._debug.width.end = this._io.pos;
      this._debug.bottom = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.bottom = this._io.readF4be();
      this._debug.bottom.end = this._io.pos;
      this._debug.depth = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.depth = this._io.readF4be();
      this._debug.depth.end = this._io.pos;
      this._debug.surfaceY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.surfaceY = this._io.readF4be();
      this._debug.surfaceY.end = this._io.pos;
      this._debug.currentX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.currentX = this._io.readF4be();
      this._debug.currentX.end = this._io.pos;
      this._debug.currentZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.currentZ = this._io.readF4be();
      this._debug.currentZ.end = this._io.pos;
      this._debug.puzzleTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.puzzleTag = this._io.readU2be();
      this._debug.puzzleTag.end = this._io.pos;
      this._debug.objectId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.objectId = this._io.readU4be();
      this._debug.objectId.end = this._io.pos;
      this._debug.name = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.name = KaitaiStream.bytesToStr(this._io.readBytes(8), "ASCII");
      this._debug.name.end = this._io.pos;
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
    }

    return Water;
  })();

  var PuzzleActionSpawnEnemy = GloverLevel.PuzzleActionSpawnEnemy = (function() {
    function PuzzleActionSpawnEnemy(_io, _parent, _root) {
      this.__type = 'PuzzleActionSpawnEnemy';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionSpawnEnemy.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.reserved = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.reserved = this._io.readU4be();
      this._debug.reserved.end = this._io.pos;
      this._debug.puzzleTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.puzzleTag = this._io.readU2be();
      this._debug.puzzleTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.GenericFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionSpawnEnemy;
  })();

  var PuzzleAction0x4f = GloverLevel.PuzzleAction0x4f = (function() {
    function PuzzleAction0x4f(_io, _parent, _root) {
      this.__type = 'PuzzleAction0x4f';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleAction0x4f.prototype._read = function() {
      this._debug.u320x14 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x14 = this._io.readU4be();
      this._debug.u320x14.end = this._io.pos;
      this._debug.u320x18 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x18 = this._io.readU4be();
      this._debug.u320x18.end = this._io.pos;
      this._debug.u320x10 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x10 = this._io.readU4be();
      this._debug.u320x10.end = this._io.pos;
      this._debug.u160x0e = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x0e = this._io.readU2be();
      this._debug.u160x0e.end = this._io.pos;
      this._debug.u160x0a = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x0a = this._io.readU2be();
      this._debug.u160x0a.end = this._io.pos;
      this._debug.u320x20 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x20 = this._io.readU4be();
      this._debug.u320x20.end = this._io.pos;
    }

    return PuzzleAction0x4f;
  })();

  var PlatNoClip = GloverLevel.PlatNoClip = (function() {
    function PlatNoClip(_io, _parent, _root) {
      this.__type = 'PlatNoClip';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatNoClip.prototype._read = function() {
    }

    return PlatNoClip;
  })();

  var PlatScale = GloverLevel.PlatScale = (function() {
    function PlatScale(_io, _parent, _root) {
      this.__type = 'PlatScale';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatScale.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
    }

    return PlatScale;
  })();

  var PuzzleAction0x4b0x4c = GloverLevel.PuzzleAction0x4b0x4c = (function() {
    function PuzzleAction0x4b0x4c(_io, _parent, _root) {
      this.__type = 'PuzzleAction0x4b0x4c';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleAction0x4b0x4c.prototype._read = function() {
      this._debug.u160x0a = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x0a = this._io.readU2be();
      this._debug.u160x0a.end = this._io.pos;
    }

    return PuzzleAction0x4b0x4c;
  })();

  var SetActorScale = GloverLevel.SetActorScale = (function() {
    function SetActorScale(_io, _parent, _root) {
      this.__type = 'SetActorScale';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    SetActorScale.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
    }

    return SetActorScale;
  })();

  var PuzzleActionSetBackground = GloverLevel.PuzzleActionSetBackground = (function() {
    function PuzzleActionSetBackground(_io, _parent, _root) {
      this.__type = 'PuzzleActionSetBackground';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionSetBackground.prototype._read = function() {
      this._debug.textureId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.textureId = this._io.readU4be();
      this._debug.textureId.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
    }

    return PuzzleActionSetBackground;
  })();

  var PlatSpecial0xb8 = GloverLevel.PlatSpecial0xb8 = (function() {
    function PlatSpecial0xb8(_io, _parent, _root) {
      this.__type = 'PlatSpecial0xb8';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSpecial0xb8.prototype._read = function() {
    }

    return PlatSpecial0xb8;
  })();

  var PlatOrbitSound0xc4 = GloverLevel.PlatOrbitSound0xc4 = (function() {
    function PlatOrbitSound0xc4(_io, _parent, _root) {
      this.__type = 'PlatOrbitSound0xc4';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatOrbitSound0xc4.prototype._read = function() {
      this._debug.u160x3a = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x3a = this._io.readU2be();
      this._debug.u160x3a.end = this._io.pos;
      this._debug.u160x2cAnd0x34 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x2cAnd0x34 = this._io.readU2be();
      this._debug.u160x2cAnd0x34.end = this._io.pos;
      this._debug.u160x38 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x38 = this._io.readU2be();
      this._debug.u160x38.end = this._io.pos;
    }

    return PlatOrbitSound0xc4;
  })();

  var PuzzleCondBallIsTouchingPlatform = GloverLevel.PuzzleCondBallIsTouchingPlatform = (function() {
    function PuzzleCondBallIsTouchingPlatform(_io, _parent, _root) {
      this.__type = 'PuzzleCondBallIsTouchingPlatform';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondBallIsTouchingPlatform.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.invertResult = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.invertResult = this._io.readS2be();
      this._debug.invertResult.end = this._io.pos;
    }

    return PuzzleCondBallIsTouchingPlatform;
  })();

  var CameoGrabTodo = GloverLevel.CameoGrabTodo = (function() {
    function CameoGrabTodo(_io, _parent, _root) {
      this.__type = 'CameoGrabTodo';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    CameoGrabTodo.prototype._read = function() {
      this._debug.grabbingEnemyIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.grabbingEnemyIdx = this._io.readU2be();
      this._debug.grabbingEnemyIdx.end = this._io.pos;
      this._debug.grabbedEnemyIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.grabbedEnemyIdx = this._io.readU2be();
      this._debug.grabbedEnemyIdx.end = this._io.pos;
      this._debug.linkagePointIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.linkagePointIdx = this._io.readU2be();
      this._debug.linkagePointIdx.end = this._io.pos;
      this._debug.frameCount = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.frameCount = this._io.readS2be();
      this._debug.frameCount.end = this._io.pos;
      this._debug.precedingInstrIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.precedingInstrIdx = this._io.readS2be();
      this._debug.precedingInstrIdx.end = this._io.pos;
    }

    return CameoGrabTodo;
  })();

  var PlatOrbitFlip0x77 = GloverLevel.PlatOrbitFlip0x77 = (function() {
    function PlatOrbitFlip0x77(_io, _parent, _root) {
      this.__type = 'PlatOrbitFlip0x77';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatOrbitFlip0x77.prototype._read = function() {
      this._debug.u160x08 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x08 = this._io.readU2be();
      this._debug.u160x08.end = this._io.pos;
      this._debug.u160x10 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x10 = this._io.readU2be();
      this._debug.u160x10.end = this._io.pos;
    }

    return PlatOrbitFlip0x77;
  })();

  var PlatDestructibleSound = GloverLevel.PlatDestructibleSound = (function() {
    function PlatDestructibleSound(_io, _parent, _root) {
      this.__type = 'PlatDestructibleSound';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatDestructibleSound.prototype._read = function() {
      this._debug.soundId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.soundId = this._io.readU2be();
      this._debug.soundId.end = this._io.pos;
      this._debug.volume = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.volume = this._io.readU2be();
      this._debug.volume.end = this._io.pos;
      this._debug.pitch = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.pitch = this._io.readU2be();
      this._debug.pitch.end = this._io.pos;
    }

    return PlatDestructibleSound;
  })();

  var AmbientLight = GloverLevel.AmbientLight = (function() {
    function AmbientLight(_io, _parent, _root) {
      this.__type = 'AmbientLight';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    AmbientLight.prototype._read = function() {
      this._debug.r = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.r = this._io.readU2be();
      this._debug.r.end = this._io.pos;
      this._debug.g = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.g = this._io.readU2be();
      this._debug.g.end = this._io.pos;
      this._debug.b = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.b = this._io.readU2be();
      this._debug.b.end = this._io.pos;
    }

    return AmbientLight;
  })();

  var Enemy = GloverLevel.Enemy = (function() {
    Enemy.EnemyType = Object.freeze({
      BOVVA: 7,
      CANNON: 8,
      SAMTEX: 9,
      MALLET: 10,
      GENERALW: 11,
      LIONFISH: 12,
      CHESTER: 13,
      KEG: 14,
      REGGIE: 15,
      SWISH: 16,
      THRICE: 17,
      ROBES: 18,
      FUMBLE: 19,
      MIKE: 20,
      RAPTOR: 21,
      CRUMPET: 22,
      TRACEY: 23,
      YOOFOW: 24,
      OPEC: 25,
      CYMON: 26,
      SUCKER: 27,
      BUGLE: 28,
      DENNIS: 29,
      CHUCK: 30,
      HUBCHICKEN1: 31,
      FRANKIE2: 32,
      KLOSET: 33,
      WILLY: 34,
      JOFF: 35,
      CANCER: 36,
      KIRK: 37,
      ROBOT: 38,
      EVILROBOT: 39,
      SPANK: 40,
      BABYSPK2: 41,
      EVILGLOVE: 42,
      DIBBER: 43,
      BRUNDLE: 44,
      MALCOM: 45,
      SPOTTY: 46,
      GORDON: 47,
      SIDNEY: 48,
      WEEVIL: 49,
      CHOPSTIK: 50,
      BUTTERFLY: 51,
      SPIDER: 52,
      BAT: 53,
      FROG: 54,
      DRAGFLY: 55,
      BOXTHING: 56,
      BUG: 57,
      NMEFROG: 58,

      7: "BOVVA",
      8: "CANNON",
      9: "SAMTEX",
      10: "MALLET",
      11: "GENERALW",
      12: "LIONFISH",
      13: "CHESTER",
      14: "KEG",
      15: "REGGIE",
      16: "SWISH",
      17: "THRICE",
      18: "ROBES",
      19: "FUMBLE",
      20: "MIKE",
      21: "RAPTOR",
      22: "CRUMPET",
      23: "TRACEY",
      24: "YOOFOW",
      25: "OPEC",
      26: "CYMON",
      27: "SUCKER",
      28: "BUGLE",
      29: "DENNIS",
      30: "CHUCK",
      31: "HUBCHICKEN1",
      32: "FRANKIE2",
      33: "KLOSET",
      34: "WILLY",
      35: "JOFF",
      36: "CANCER",
      37: "KIRK",
      38: "ROBOT",
      39: "EVILROBOT",
      40: "SPANK",
      41: "BABYSPK2",
      42: "EVILGLOVE",
      43: "DIBBER",
      44: "BRUNDLE",
      45: "MALCOM",
      46: "SPOTTY",
      47: "GORDON",
      48: "SIDNEY",
      49: "WEEVIL",
      50: "CHOPSTIK",
      51: "BUTTERFLY",
      52: "SPIDER",
      53: "BAT",
      54: "FROG",
      55: "DRAGFLY",
      56: "BOXTHING",
      57: "BUG",
      58: "NMEFROG",
    });

    function Enemy(_io, _parent, _root) {
      this.__type = 'Enemy';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Enemy.prototype._read = function() {
      this._debug.type = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.Enemy.EnemyType" };
      this.type = this._io.readU2be();
      this._debug.type.end = this._io.pos;
      this._debug.puzzleTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.puzzleTag = this._io.readU2be();
      this._debug.puzzleTag.end = this._io.pos;
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.yRotation = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.yRotation = this._io.readF4be();
      this._debug.yRotation.end = this._io.pos;
    }

    return Enemy;
  })();

  var PuzzleCondPlatformOrbit2Todo = GloverLevel.PuzzleCondPlatformOrbit2Todo = (function() {
    function PuzzleCondPlatformOrbit2Todo(_io, _parent, _root) {
      this.__type = 'PuzzleCondPlatformOrbit2Todo';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondPlatformOrbit2Todo.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.arg2 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.arg2 = this._io.readS2be();
      this._debug.arg2.end = this._io.pos;
    }

    return PuzzleCondPlatformOrbit2Todo;
  })();

  var Plat0xa4 = GloverLevel.Plat0xa4 = (function() {
    function Plat0xa4(_io, _parent, _root) {
      this.__type = 'Plat0xa4';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Plat0xa4.prototype._read = function() {
    }

    return Plat0xa4;
  })();

  var PlatOrbitPause = GloverLevel.PlatOrbitPause = (function() {
    function PlatOrbitPause(_io, _parent, _root) {
      this.__type = 'PlatOrbitPause';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatOrbitPause.prototype._read = function() {
      this._debug.numFrames = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.numFrames = this._io.readU2be();
      this._debug.numFrames.end = this._io.pos;
      this._debug.numPauses = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.numPauses = this._io.readU2be();
      this._debug.numPauses.end = this._io.pos;
    }

    return PlatOrbitPause;
  })();

  var PlatCrumb0x67 = GloverLevel.PlatCrumb0x67 = (function() {
    function PlatCrumb0x67(_io, _parent, _root) {
      this.__type = 'PlatCrumb0x67';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatCrumb0x67.prototype._read = function() {
      this._debug.u160x02 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x02 = this._io.readU2be();
      this._debug.u160x02.end = this._io.pos;
      this._debug.u160x04 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x04 = this._io.readU2be();
      this._debug.u160x04.end = this._io.pos;
      this._debug.u160x08 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x08 = this._io.readU4be();
      this._debug.u160x08.end = this._io.pos;
    }

    return PlatCrumb0x67;
  })();

  var PuzzleActionDefault = GloverLevel.PuzzleActionDefault = (function() {
    function PuzzleActionDefault(_io, _parent, _root) {
      this.__type = 'PuzzleActionDefault';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionDefault.prototype._read = function() {
      this._debug.field0 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.field0 = this._io.readU4be();
      this._debug.field0.end = this._io.pos;
      this._debug.field1 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.field1 = this._io.readS2be();
      this._debug.field1.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.GenericFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionDefault;
  })();

  var AmbientSound = GloverLevel.AmbientSound = (function() {
    function AmbientSound(_io, _parent, _root) {
      this.__type = 'AmbientSound';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    AmbientSound.prototype._read = function() {
      this._debug.soundId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.soundId = this._io.readU2be();
      this._debug.soundId.end = this._io.pos;
      this._debug.volume = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.volume = this._io.readU2be();
      this._debug.volume.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.flags = this._io.readU2be();
      this._debug.flags.end = this._io.pos;
    }

    return AmbientSound;
  })();

  var Garib = GloverLevel.Garib = (function() {
    Garib.GaribType = Object.freeze({
      GARIB: 0,
      BANG_500PT: 1,
      EXTRA_LIFE: 2,
      MAD_GARIB: 3,

      0: "GARIB",
      1: "BANG_500PT",
      2: "EXTRA_LIFE",
      3: "MAD_GARIB",
    });

    function Garib(_io, _parent, _root) {
      this.__type = 'Garib';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Garib.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.type = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.Garib.GaribType" };
      this.type = this._io.readU2be();
      this._debug.type.end = this._io.pos;
      this._debug.dynamicShadow = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.dynamicShadow = this._io.readU2be();
      this._debug.dynamicShadow.end = this._io.pos;
    }

    return Garib;
  })();

  var PlatCauseDamage = GloverLevel.PlatCauseDamage = (function() {
    function PlatCauseDamage(_io, _parent, _root) {
      this.__type = 'PlatCauseDamage';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatCauseDamage.prototype._read = function() {
      this._debug.enable = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.enable = this._io.readU2be();
      this._debug.enable.end = this._io.pos;
    }

    return PlatCauseDamage;
  })();

  var GaribGroup = GloverLevel.GaribGroup = (function() {
    function GaribGroup(_io, _parent, _root) {
      this.__type = 'GaribGroup';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    GaribGroup.prototype._read = function() {
      this._debug.groupId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.groupId = this._io.readU2be();
      this._debug.groupId.end = this._io.pos;
      this._debug.initialState = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.initialState = this._io.readS2be();
      this._debug.initialState.end = this._io.pos;
    }

    return GaribGroup;
  })();

  var AnimatedBackgroundActor = GloverLevel.AnimatedBackgroundActor = (function() {
    function AnimatedBackgroundActor(_io, _parent, _root) {
      this.__type = 'AnimatedBackgroundActor';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    AnimatedBackgroundActor.prototype._read = function() {
      this._debug.objectId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.objectId = this._io.readU4be();
      this._debug.objectId.end = this._io.pos;
      this._debug.name = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.name = KaitaiStream.bytesToStr(this._io.readBytes(8), "ASCII");
      this._debug.name.end = this._io.pos;
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
    }

    return AnimatedBackgroundActor;
  })();

  var PuzzleActionMakeBallInteractive = GloverLevel.PuzzleActionMakeBallInteractive = (function() {
    function PuzzleActionMakeBallInteractive(_io, _parent, _root) {
      this.__type = 'PuzzleActionMakeBallInteractive';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionMakeBallInteractive.prototype._read = function() {
      this._debug.reserved = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.reserved = this._io.readU4be();
      this._debug.reserved.end = this._io.pos;
      this._debug.reserved2 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.reserved2 = this._io.readU2be();
      this._debug.reserved2.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.GenericFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionMakeBallInteractive;
  })();

  var BackgroundActor = GloverLevel.BackgroundActor = (function() {
    function BackgroundActor(_io, _parent, _root) {
      this.__type = 'BackgroundActor';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    BackgroundActor.prototype._read = function() {
      this._debug.objectId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.objectId = this._io.readU4be();
      this._debug.objectId.end = this._io.pos;
      this._debug.name = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.name = KaitaiStream.bytesToStr(this._io.readBytes(8), "ASCII");
      this._debug.name.end = this._io.pos;
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
    }

    return BackgroundActor;
  })();

  var EnemyInstructionMove = GloverLevel.EnemyInstructionMove = (function() {
    function EnemyInstructionMove(_io, _parent, _root) {
      this.__type = 'EnemyInstructionMove';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyInstructionMove.prototype._read = function() {
      this._debug.destinationX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.destinationX = this._io.readF4be();
      this._debug.destinationX.end = this._io.pos;
      this._debug.destinationY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.destinationY = this._io.readF4be();
      this._debug.destinationY.end = this._io.pos;
      this._debug.destinationZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.destinationZ = this._io.readF4be();
      this._debug.destinationZ.end = this._io.pos;
      this._debug.velMagnitude = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velMagnitude = this._io.readF4be();
      this._debug.velMagnitude.end = this._io.pos;
    }

    return EnemyInstructionMove;
  })();

  var PlatPathPoint = GloverLevel.PlatPathPoint = (function() {
    function PlatPathPoint(_io, _parent, _root) {
      this.__type = 'PlatPathPoint';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatPathPoint.prototype._read = function() {
      this._debug.duration = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.duration = this._io.readS2be();
      this._debug.duration.end = this._io.pos;
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
    }

    return PlatPathPoint;
  })();

  var Plat0x78 = GloverLevel.Plat0x78 = (function() {
    function Plat0x78(_io, _parent, _root) {
      this.__type = 'Plat0x78';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Plat0x78.prototype._read = function() {
      this._debug.u160x08 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x08 = this._io.readU2be();
      this._debug.u160x08.end = this._io.pos;
    }

    return Plat0x78;
  })();

  var Enemy0xba = GloverLevel.Enemy0xba = (function() {
    function Enemy0xba(_io, _parent, _root) {
      this.__type = 'Enemy0xba';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Enemy0xba.prototype._read = function() {
    }

    return Enemy0xba;
  })();

  var CameoSpin = GloverLevel.CameoSpin = (function() {
    function CameoSpin(_io, _parent, _root) {
      this.__type = 'CameoSpin';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    CameoSpin.prototype._read = function() {
      this._debug.enemyIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.enemyIdx = this._io.readU2be();
      this._debug.enemyIdx.end = this._io.pos;
      this._debug.speed = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.speed = this._io.readF4be();
      this._debug.speed.end = this._io.pos;
      this._debug.frameCount = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.frameCount = this._io.readS2be();
      this._debug.frameCount.end = this._io.pos;
      this._debug.precedingInstrIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.precedingInstrIdx = this._io.readS2be();
      this._debug.precedingInstrIdx.end = this._io.pos;
    }

    return CameoSpin;
  })();

  var PlatSine = GloverLevel.PlatSine = (function() {
    function PlatSine(_io, _parent, _root) {
      this.__type = 'PlatSine';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSine.prototype._read = function() {
      this._debug.u32Count = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u32Count = this._io.readU4be();
      this._debug.u32Count.end = this._io.pos;
      this._debug.u32116 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u32116 = this._io.readU4be();
      this._debug.u32116.end = this._io.pos;
      this._debug.name = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.name = KaitaiStream.bytesToStr(this._io.readBytes(8), "ASCII");
      this._debug.name.end = this._io.pos;
      this._debug.f108 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f108 = this._io.readF4be();
      this._debug.f108.end = this._io.pos;
      this._debug.f104 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f104 = this._io.readF4be();
      this._debug.f104.end = this._io.pos;
      this._debug.f100 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f100 = this._io.readF4be();
      this._debug.f100.end = this._io.pos;
      this._debug.f96 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f96 = this._io.readF4be();
      this._debug.f96.end = this._io.pos;
      this._debug.f92 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f92 = this._io.readF4be();
      this._debug.f92.end = this._io.pos;
      this._debug.f88 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f88 = this._io.readF4be();
      this._debug.f88.end = this._io.pos;
      this._debug.f84 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f84 = this._io.readF4be();
      this._debug.f84.end = this._io.pos;
      this._debug.f80 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f80 = this._io.readF4be();
      this._debug.f80.end = this._io.pos;
      this._debug.u32176 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u32176 = this._io.readU4be();
      this._debug.u32176.end = this._io.pos;
      this._debug.u32172 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u32172 = this._io.readU4be();
      this._debug.u32172.end = this._io.pos;
    }

    return PlatSine;
  })();

  var PlatCat0x69 = GloverLevel.PlatCat0x69 = (function() {
    function PlatCat0x69(_io, _parent, _root) {
      this.__type = 'PlatCat0x69';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatCat0x69.prototype._read = function() {
      this._debug.u160x20 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x20 = this._io.readU2be();
      this._debug.u160x20.end = this._io.pos;
      this._debug.u320x00 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x00 = this._io.readU4be();
      this._debug.u320x00.end = this._io.pos;
      this._debug.u320x04 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x04 = this._io.readU4be();
      this._debug.u320x04.end = this._io.pos;
      this._debug.u320x08 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x08 = this._io.readU4be();
      this._debug.u320x08.end = this._io.pos;
      this._debug.u320x0c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x0c = this._io.readU4be();
      this._debug.u320x0c.end = this._io.pos;
      this._debug.u320x10 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x10 = this._io.readU4be();
      this._debug.u320x10.end = this._io.pos;
      this._debug.u320x1c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x1c = this._io.readU4be();
      this._debug.u320x1c.end = this._io.pos;
    }

    return PlatCat0x69;
  })();

  var PuzzleActionToggleWind = GloverLevel.PuzzleActionToggleWind = (function() {
    function PuzzleActionToggleWind(_io, _parent, _root) {
      this.__type = 'PuzzleActionToggleWind';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionToggleWind.prototype._read = function() {
      this._debug.enabled = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.enabled = this._io.readU4be();
      this._debug.enabled.end = this._io.pos;
      this._debug.puzzleTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.puzzleTag = this._io.readS2be();
      this._debug.puzzleTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.GenericFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionToggleWind;
  })();

  var PuzzleNumtimes = GloverLevel.PuzzleNumtimes = (function() {
    function PuzzleNumtimes(_io, _parent, _root) {
      this.__type = 'PuzzleNumtimes';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleNumtimes.prototype._read = function() {
      this._debug.n = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.n = this._io.readU2be();
      this._debug.n.end = this._io.pos;
    }

    return PuzzleNumtimes;
  })();

  var PlatSpin0x80 = GloverLevel.PlatSpin0x80 = (function() {
    function PlatSpin0x80(_io, _parent, _root) {
      this.__type = 'PlatSpin0x80';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSpin0x80.prototype._read = function() {
      this._debug.idx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.idx = this._io.readU2be();
      this._debug.idx.end = this._io.pos;
      this._debug.f0x1c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f0x1c = this._io.readF4be();
      this._debug.f0x1c.end = this._io.pos;
      this._debug.u320x28 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x28 = this._io.readU4be();
      this._debug.u320x28.end = this._io.pos;
      this._debug.u32Ustack56 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u32Ustack56 = this._io.readU4be();
      this._debug.u32Ustack56.end = this._io.pos;
      this._debug.u320x2c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x2c = this._io.readU4be();
      this._debug.u320x2c.end = this._io.pos;
      this._debug.f0x6c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f0x6c = this._io.readF4be();
      this._debug.f0x6c.end = this._io.pos;
      this._debug.f0x70 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f0x70 = this._io.readU2be();
      this._debug.f0x70.end = this._io.pos;
    }

    return PlatSpin0x80;
  })();

  var PuzzleCondGloverIsTouchingPlatform = GloverLevel.PuzzleCondGloverIsTouchingPlatform = (function() {
    function PuzzleCondGloverIsTouchingPlatform(_io, _parent, _root) {
      this.__type = 'PuzzleCondGloverIsTouchingPlatform';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondGloverIsTouchingPlatform.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.invertResult = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.invertResult = this._io.readS2be();
      this._debug.invertResult.end = this._io.pos;
    }

    return PuzzleCondGloverIsTouchingPlatform;
  })();

  var PlatRocking = GloverLevel.PlatRocking = (function() {
    function PlatRocking(_io, _parent, _root) {
      this.__type = 'PlatRocking';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatRocking.prototype._read = function() {
      this._debug.axis = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.axis = this._io.readU2be();
      this._debug.axis.end = this._io.pos;
      this._debug.theta = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.theta = this._io.readF4be();
      this._debug.theta.end = this._io.pos;
      this._debug.deceleration = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.deceleration = this._io.readF4be();
      this._debug.deceleration.end = this._io.pos;
      this._debug.blurHeight = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.blurHeight = this._io.readF4be();
      this._debug.blurHeight.end = this._io.pos;
      this._debug.frameAdvance = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.frameAdvance = this._io.readU2be();
      this._debug.frameAdvance.end = this._io.pos;
    }

    return PlatRocking;
  })();

  var Plat0x7e = GloverLevel.Plat0x7e = (function() {
    function Plat0x7e(_io, _parent, _root) {
      this.__type = 'Plat0x7e';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Plat0x7e.prototype._read = function() {
      this._debug.u320x28 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x28 = this._io.readU4be();
      this._debug.u320x28.end = this._io.pos;
    }

    return Plat0x7e;
  })();

  var PuzzleActionControlActiveElements = GloverLevel.PuzzleActionControlActiveElements = (function() {
    function PuzzleActionControlActiveElements(_io, _parent, _root) {
      this.__type = 'PuzzleActionControlActiveElements';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionControlActiveElements.prototype._read = function() {
      this._debug.value = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.value = this._io.readF4be();
      this._debug.value.end = this._io.pos;
      this._debug.puzzleTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.puzzleTag = this._io.readU2be();
      this._debug.puzzleTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.PlatformToggleFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionControlActiveElements;
  })();

  var GloverSpawnPoint = GloverLevel.GloverSpawnPoint = (function() {
    function GloverSpawnPoint(_io, _parent, _root) {
      this.__type = 'GloverSpawnPoint';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    GloverSpawnPoint.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
    }

    return GloverSpawnPoint;
  })();

  var Plat0x9d = GloverLevel.Plat0x9d = (function() {
    function Plat0x9d(_io, _parent, _root) {
      this.__type = 'Plat0x9d';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Plat0x9d.prototype._read = function() {
    }

    return Plat0x9d;
  })();

  var EnemyNormalInstruction = GloverLevel.EnemyNormalInstruction = (function() {
    function EnemyNormalInstruction(_io, _parent, _root) {
      this.__type = 'EnemyNormalInstruction';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyNormalInstruction.prototype._read = function() {
      this._debug.instr = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.instr = new EnemyInstruction(this._io, this, this._root);
      this._debug.instr.end = this._io.pos;
    }

    return EnemyNormalInstruction;
  })();

  var FogConfiguration = GloverLevel.FogConfiguration = (function() {
    function FogConfiguration(_io, _parent, _root) {
      this.__type = 'FogConfiguration';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    FogConfiguration.prototype._read = function() {
      this._debug.fogEnabled = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.fogEnabled = this._io.readU1();
      this._debug.fogEnabled.end = this._io.pos;
      this._debug.r = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.r = this._io.readU1();
      this._debug.r.end = this._io.pos;
      this._debug.g = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.g = this._io.readU1();
      this._debug.g.end = this._io.pos;
      this._debug.b = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.b = this._io.readU1();
      this._debug.b.end = this._io.pos;
      this._debug.fogDistance = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.fogDistance = this._io.readU2be();
      this._debug.fogDistance.end = this._io.pos;
      this._debug.nearClip = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.nearClip = this._io.readU2be();
      this._debug.nearClip.end = this._io.pos;
    }

    return FogConfiguration;
  })();

  var BuzzerDutyCycle = GloverLevel.BuzzerDutyCycle = (function() {
    function BuzzerDutyCycle(_io, _parent, _root) {
      this.__type = 'BuzzerDutyCycle';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    BuzzerDutyCycle.prototype._read = function() {
      this._debug.framesOff = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.framesOff = this._io.readU2be();
      this._debug.framesOff.end = this._io.pos;
      this._debug.framesOn = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.framesOn = this._io.readU2be();
      this._debug.framesOn.end = this._io.pos;
    }

    return BuzzerDutyCycle;
  })();

  var CameoPlayAnimation = GloverLevel.CameoPlayAnimation = (function() {
    function CameoPlayAnimation(_io, _parent, _root) {
      this.__type = 'CameoPlayAnimation';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    CameoPlayAnimation.prototype._read = function() {
      this._debug.enemyIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.enemyIdx = this._io.readU2be();
      this._debug.enemyIdx.end = this._io.pos;
      this._debug.animIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.animIdx = this._io.readU2be();
      this._debug.animIdx.end = this._io.pos;
      this._debug.startPlaying = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.startPlaying = this._io.readU2be();
      this._debug.startPlaying.end = this._io.pos;
      this._debug.playbackSpeed = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.playbackSpeed = this._io.readF4be();
      this._debug.playbackSpeed.end = this._io.pos;
      this._debug.frameCount = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.frameCount = this._io.readS2be();
      this._debug.frameCount.end = this._io.pos;
      this._debug.precedingInstrIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.precedingInstrIdx = this._io.readS2be();
      this._debug.precedingInstrIdx.end = this._io.pos;
    }

    return CameoPlayAnimation;
  })();

  var PuzzleActionSetConveyor = GloverLevel.PuzzleActionSetConveyor = (function() {
    function PuzzleActionSetConveyor(_io, _parent, _root) {
      this.__type = 'PuzzleActionSetConveyor';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionSetConveyor.prototype._read = function() {
      this._debug.velX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velX = this._io.readF4be();
      this._debug.velX.end = this._io.pos;
      this._debug.velY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velY = this._io.readF4be();
      this._debug.velY.end = this._io.pos;
      this._debug.velZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.velZ = this._io.readF4be();
      this._debug.velZ.end = this._io.pos;
      this._debug.reserved = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.reserved = this._io.readU4be();
      this._debug.reserved.end = this._io.pos;
      this._debug.puzzleTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.puzzleTag = this._io.readU2be();
      this._debug.puzzleTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.CameraFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionSetConveyor;
  })();

  var PlatPlayObjectAnimation = GloverLevel.PlatPlayObjectAnimation = (function() {
    function PlatPlayObjectAnimation(_io, _parent, _root) {
      this.__type = 'PlatPlayObjectAnimation';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatPlayObjectAnimation.prototype._read = function() {
    }

    return PlatPlayObjectAnimation;
  })();

  var PuzzleCondGloverWithinVolume = GloverLevel.PuzzleCondGloverWithinVolume = (function() {
    function PuzzleCondGloverWithinVolume(_io, _parent, _root) {
      this.__type = 'PuzzleCondGloverWithinVolume';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondGloverWithinVolume.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.l = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.l = this._io.readF4be();
      this._debug.l.end = this._io.pos;
      this._debug.w = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.w = this._io.readF4be();
      this._debug.w.end = this._io.pos;
      this._debug.h = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.h = this._io.readF4be();
      this._debug.h.end = this._io.pos;
    }

    return PuzzleCondGloverWithinVolume;
  })();

  var PlatTopple0x81 = GloverLevel.PlatTopple0x81 = (function() {
    function PlatTopple0x81(_io, _parent, _root) {
      this.__type = 'PlatTopple0x81';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatTopple0x81.prototype._read = function() {
      this._debug.idx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.idx = this._io.readU2be();
      this._debug.idx.end = this._io.pos;
      this._debug.f0x1c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f0x1c = this._io.readF4be();
      this._debug.f0x1c.end = this._io.pos;
      this._debug.f0x28 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f0x28 = this._io.readF4be();
      this._debug.f0x28.end = this._io.pos;
      this._debug.f0x24 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f0x24 = this._io.readF4be();
      this._debug.f0x24.end = this._io.pos;
      this._debug.f0x2c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f0x2c = this._io.readF4be();
      this._debug.f0x2c.end = this._io.pos;
      this._debug.f0x6c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f0x6c = this._io.readF4be();
      this._debug.f0x6c.end = this._io.pos;
      this._debug.f0x70PivotHeight = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.f0x70PivotHeight = this._io.readF4be();
      this._debug.f0x70PivotHeight.end = this._io.pos;
      this._debug.u160x10 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x10 = this._io.readU2be();
      this._debug.u160x10.end = this._io.pos;
    }

    return PlatTopple0x81;
  })();

  var EnemyInstructionPlayAnimation = GloverLevel.EnemyInstructionPlayAnimation = (function() {
    function EnemyInstructionPlayAnimation(_io, _parent, _root) {
      this.__type = 'EnemyInstructionPlayAnimation';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyInstructionPlayAnimation.prototype._read = function() {
      this._debug.animIdx1 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.animIdx1 = this._io.readS4be();
      this._debug.animIdx1.end = this._io.pos;
      this._debug.animIdx2 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.animIdx2 = this._io.readS4be();
      this._debug.animIdx2.end = this._io.pos;
    }

    return EnemyInstructionPlayAnimation;
  })();

  var EnemyInstructionRandomWalk = GloverLevel.EnemyInstructionRandomWalk = (function() {
    function EnemyInstructionRandomWalk(_io, _parent, _root) {
      this.__type = 'EnemyInstructionRandomWalk';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyInstructionRandomWalk.prototype._read = function() {
      this._debug.homeX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.homeX = this._io.readF4be();
      this._debug.homeX.end = this._io.pos;
      this._debug.homeY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.homeY = this._io.readF4be();
      this._debug.homeY.end = this._io.pos;
      this._debug.homeZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.homeZ = this._io.readF4be();
      this._debug.homeZ.end = this._io.pos;
      this._debug.extentX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.extentX = this._io.readF4be();
      this._debug.extentX.end = this._io.pos;
      this._debug.extentY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.extentY = this._io.readF4be();
      this._debug.extentY.end = this._io.pos;
      this._debug.extentZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.extentZ = this._io.readF4be();
      this._debug.extentZ.end = this._io.pos;
      this._debug.minTravelDistance = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.minTravelDistance = this._io.readF4be();
      this._debug.minTravelDistance.end = this._io.pos;
    }

    return EnemyInstructionRandomWalk;
  })();

  var PlatGoForwards0x5f = GloverLevel.PlatGoForwards0x5f = (function() {
    function PlatGoForwards0x5f(_io, _parent, _root) {
      this.__type = 'PlatGoForwards0x5f';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatGoForwards0x5f.prototype._read = function() {
      this._debug.u320x2c0x6c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x2c0x6c = this._io.readU4be();
      this._debug.u320x2c0x6c.end = this._io.pos;
      this._debug.u320x2c0x1c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x2c0x1c = this._io.readU4be();
      this._debug.u320x2c0x1c.end = this._io.pos;
      this._debug.u320xf0 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320xf0 = this._io.readU4be();
      this._debug.u320xf0.end = this._io.pos;
      this._debug.u320x2c0x34 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x2c0x34 = this._io.readU4be();
      this._debug.u320x2c0x34.end = this._io.pos;
    }

    return PlatGoForwards0x5f;
  })();

  var PuzzlePlatformTouchingConfBoundaryEdge = GloverLevel.PuzzlePlatformTouchingConfBoundaryEdge = (function() {
    PuzzlePlatformTouchingConfBoundaryEdge.EdgeType = Object.freeze({
      X: 0,
      Y: 1,
      Z: 2,
      X_PLUS_W: 3,
      Y_PLUS_H: 4,
      Z_PLUS_D: 5,

      0: "X",
      1: "Y",
      2: "Z",
      3: "X_PLUS_W",
      4: "Y_PLUS_H",
      5: "Z_PLUS_D",
    });

    function PuzzlePlatformTouchingConfBoundaryEdge(_io, _parent, _root) {
      this.__type = 'PuzzlePlatformTouchingConfBoundaryEdge';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzlePlatformTouchingConfBoundaryEdge.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.edge = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzlePlatformTouchingConfBoundaryEdge.EdgeType" };
      this.edge = this._io.readU2be();
      this._debug.edge.end = this._io.pos;
    }

    return PuzzlePlatformTouchingConfBoundaryEdge;
  })();

  var PlatSpecial0x9e = GloverLevel.PlatSpecial0x9e = (function() {
    function PlatSpecial0x9e(_io, _parent, _root) {
      this.__type = 'PlatSpecial0x9e';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSpecial0x9e.prototype._read = function() {
      this._debug.u320x5c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x5c = this._io.readU4be();
      this._debug.u320x5c.end = this._io.pos;
      this._debug.u320x60 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x60 = this._io.readU4be();
      this._debug.u320x60.end = this._io.pos;
      this._debug.u320x65 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x65 = this._io.readU4be();
      this._debug.u320x65.end = this._io.pos;
      this._debug.u320x68 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x68 = this._io.readU4be();
      this._debug.u320x68.end = this._io.pos;
    }

    return PlatSpecial0x9e;
  })();

  var EnemyInstruction = GloverLevel.EnemyInstruction = (function() {
    EnemyInstruction.ExecutionConditionType = Object.freeze({
      BALL_WITHIN_RANGE: 0,
      BALL_WITHIN_GROUND_RANGE: 1,
      GLOVER_WITHIN_RANGE: 2,
      GLOVER_WITHIN_GROUND_RANGE: 3,
      BALL_OR_GLOVER_WITHIN_RANGE: 4,
      BALL_OR_GLOVER_WITHIN_GROUND_RANGE: 5,
      BALL_WITHIN_ANGLE_OF_VIEW: 6,
      GLOVER_WITHIN_ANGLE_OF_VIEW: 7,
      BALL_OR_GLOVER_WITHIN_ANGLE_OF_VIEW: 8,
      PERIODIC: 9,
      ROLL_ANGLE_WITHIN_RANGE_AND_PERIODIC: 10,
      GLOVER_HOLDING_BALL: 11,
      GLOVER_NOT_HOLDING_BALL: 12,
      ENEMY_HOLDING_BALL: 13,
      ENEMY_NOT_HOLDING_BALL: 14,
      GLOVER_HOLDING_ENEMY: 15,
      GLOVER_NOT_HOLDING_ENEMY: 16,
      ON_BALL: 17,
      ON_GLOVER: 18,
      ENEMY_WITHIN_ATTENTION_BBOX: 19,
      ALWAYS: 20,
      NEVER: 21,
      RANDOM_CHANCE_PARAM_A_OVER_1000: 22,

      0: "BALL_WITHIN_RANGE",
      1: "BALL_WITHIN_GROUND_RANGE",
      2: "GLOVER_WITHIN_RANGE",
      3: "GLOVER_WITHIN_GROUND_RANGE",
      4: "BALL_OR_GLOVER_WITHIN_RANGE",
      5: "BALL_OR_GLOVER_WITHIN_GROUND_RANGE",
      6: "BALL_WITHIN_ANGLE_OF_VIEW",
      7: "GLOVER_WITHIN_ANGLE_OF_VIEW",
      8: "BALL_OR_GLOVER_WITHIN_ANGLE_OF_VIEW",
      9: "PERIODIC",
      10: "ROLL_ANGLE_WITHIN_RANGE_AND_PERIODIC",
      11: "GLOVER_HOLDING_BALL",
      12: "GLOVER_NOT_HOLDING_BALL",
      13: "ENEMY_HOLDING_BALL",
      14: "ENEMY_NOT_HOLDING_BALL",
      15: "GLOVER_HOLDING_ENEMY",
      16: "GLOVER_NOT_HOLDING_ENEMY",
      17: "ON_BALL",
      18: "ON_GLOVER",
      19: "ENEMY_WITHIN_ATTENTION_BBOX",
      20: "ALWAYS",
      21: "NEVER",
      22: "RANDOM_CHANCE_PARAM_A_OVER_1000",
    });

    EnemyInstruction.InstructionFlags = Object.freeze({
      FACE_PLAYER: 1048576,
      FACE_BALL: 2097152,
      FACE_CLOSER_OF_PLAYER_OR_BALL: 4194304,

      1048576: "FACE_PLAYER",
      2097152: "FACE_BALL",
      4194304: "FACE_CLOSER_OF_PLAYER_OR_BALL",
    });

    function EnemyInstruction(_io, _parent, _root) {
      this.__type = 'EnemyInstruction';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyInstruction.prototype._read = function() {
      this._debug.instrType = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.instrType = this._io.readU2be();
      this._debug.instrType.end = this._io.pos;
      this._debug.lifetime = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.lifetime = this._io.readS2be();
      this._debug.lifetime.end = this._io.pos;
      this._debug.params = { start: this._io.pos, ioOffset: this._io.byteOffset };
      switch (this.instrType) {
      case 14:
        this.params = new EnemyInstructionC(this._io, this, this._root);
        break;
      case 10:
        this.params = new EnemyInstructionA(this._io, this, this._root);
        break;
      case 17:
        this.params = new EnemyInstructionC(this._io, this, this._root);
        break;
      case 0:
        this.params = new EnemyInstructionMove(this._io, this, this._root);
        break;
      case 4:
        this.params = new EnemyInstructionRest(this._io, this, this._root);
        break;
      case 24:
        this.params = new EnemyInstructionC(this._io, this, this._root);
        break;
      case 6:
        this.params = new EnemyInstructionC(this._io, this, this._root);
        break;
      case 20:
        this.params = new EnemyInstructionC(this._io, this, this._root);
        break;
      case 7:
        this.params = new EnemyInstructionPlayAnimation(this._io, this, this._root);
        break;
      case 1:
        this.params = new EnemyInstructionDash(this._io, this, this._root);
        break;
      case 13:
        this.params = new EnemyInstructionA(this._io, this, this._root);
        break;
      case 11:
        this.params = new EnemyInstructionA(this._io, this, this._root);
        break;
      case 12:
        this.params = new EnemyInstructionC(this._io, this, this._root);
        break;
      case 3:
        this.params = new EnemyInstructionRandomWalk(this._io, this, this._root);
        break;
      case 5:
        this.params = new EnemyInstructionC(this._io, this, this._root);
        break;
      case 19:
        this.params = new EnemyInstructionC(this._io, this, this._root);
        break;
      case 23:
        this.params = new EnemyInstructionA(this._io, this, this._root);
        break;
      case 15:
        this.params = new EnemyInstructionAttack(this._io, this, this._root);
        break;
      case 8:
        this.params = new EnemyInstructionC(this._io, this, this._root);
        break;
      case 9:
        this.params = new EnemyInstructionA(this._io, this, this._root);
        break;
      case 21:
        this.params = new EnemyInstructionC(this._io, this, this._root);
        break;
      case 16:
        this.params = new EnemyInstructionC(this._io, this, this._root);
        break;
      case 18:
        this.params = new EnemyInstructionGoto(this._io, this, this._root);
        break;
      case 2:
        this.params = new EnemyInstructionTurn(this._io, this, this._root);
        break;
      case 22:
        this.params = new EnemyInstructionA(this._io, this, this._root);
        break;
      default:
        this.params = new EnemyInstructionError(this._io, this, this._root);
        break;
      }
      this._debug.params.end = this._io.pos;
      this._debug.executionConditionParamA = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.executionConditionParamA = this._io.readF4be();
      this._debug.executionConditionParamA.end = this._io.pos;
      this._debug.executionConditionParamB = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.executionConditionParamB = this._io.readF4be();
      this._debug.executionConditionParamB.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.EnemyInstruction.InstructionFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
      this._debug.executionCondition = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.EnemyInstruction.ExecutionConditionType" };
      this.executionCondition = this._io.readU2be();
      this._debug.executionCondition.end = this._io.pos;
    }

    return EnemyInstruction;
  })();

  var PuzzleCondPlatformSpinTodo = GloverLevel.PuzzleCondPlatformSpinTodo = (function() {
    function PuzzleCondPlatformSpinTodo(_io, _parent, _root) {
      this.__type = 'PuzzleCondPlatformSpinTodo';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondPlatformSpinTodo.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.idx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.idx = this._io.readS2be();
      this._debug.idx.end = this._io.pos;
    }

    return PuzzleCondPlatformSpinTodo;
  })();

  var SetGlobal0xb7 = GloverLevel.SetGlobal0xb7 = (function() {
    function SetGlobal0xb7(_io, _parent, _root) {
      this.__type = 'SetGlobal0xb7';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    SetGlobal0xb7.prototype._read = function() {
      this._debug.value = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.value = this._io.readU4be();
      this._debug.value.end = this._io.pos;
    }

    return SetGlobal0xb7;
  })();

  var PuzzleActionCameraTweenYAdjust = GloverLevel.PuzzleActionCameraTweenYAdjust = (function() {
    function PuzzleActionCameraTweenYAdjust(_io, _parent, _root) {
      this.__type = 'PuzzleActionCameraTweenYAdjust';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionCameraTweenYAdjust.prototype._read = function() {
      this._debug.yAdjust = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.yAdjust = this._io.readF4be();
      this._debug.yAdjust.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
    }

    return PuzzleActionCameraTweenYAdjust;
  })();

  var Platform = GloverLevel.Platform = (function() {
    function Platform(_io, _parent, _root) {
      this.__type = 'Platform';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Platform.prototype._read = function() {
      this._debug.objectId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.objectId = this._io.readU4be();
      this._debug.objectId.end = this._io.pos;
      this._debug.name = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.name = KaitaiStream.bytesToStr(this._io.readBytes(8), "ASCII");
      this._debug.name.end = this._io.pos;
    }

    return Platform;
  })();

  var PuzzleActionCameraLookAtPlatform = GloverLevel.PuzzleActionCameraLookAtPlatform = (function() {
    function PuzzleActionCameraLookAtPlatform(_io, _parent, _root) {
      this.__type = 'PuzzleActionCameraLookAtPlatform';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionCameraLookAtPlatform.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.duration = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.duration = this._io.readF4be();
      this._debug.duration.end = this._io.pos;
      this._debug.platformTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platformTag = this._io.readU2be();
      this._debug.platformTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.CameraFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionCameraLookAtPlatform;
  })();

  var PlatPos0xa7 = GloverLevel.PlatPos0xa7 = (function() {
    function PlatPos0xa7(_io, _parent, _root) {
      this.__type = 'PlatPos0xa7';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatPos0xa7.prototype._read = function() {
      this._debug.u8Idx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u8Idx = this._io.readU2be();
      this._debug.u8Idx.end = this._io.pos;
    }

    return PlatPos0xa7;
  })();

  var PlatConfBoundaryVolume = GloverLevel.PlatConfBoundaryVolume = (function() {
    function PlatConfBoundaryVolume(_io, _parent, _root) {
      this.__type = 'PlatConfBoundaryVolume';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatConfBoundaryVolume.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.w = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.w = this._io.readF4be();
      this._debug.w.end = this._io.pos;
      this._debug.h = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.h = this._io.readF4be();
      this._debug.h.end = this._io.pos;
      this._debug.d = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.d = this._io.readF4be();
      this._debug.d.end = this._io.pos;
    }

    return PlatConfBoundaryVolume;
  })();

  var PuzzleActionSpawnGaribGroup = GloverLevel.PuzzleActionSpawnGaribGroup = (function() {
    function PuzzleActionSpawnGaribGroup(_io, _parent, _root) {
      this.__type = 'PuzzleActionSpawnGaribGroup';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionSpawnGaribGroup.prototype._read = function() {
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.groupId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.groupId = this._io.readS2be();
      this._debug.groupId.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.numSpawns = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.numSpawns = this._io.readS4be();
      this._debug.numSpawns.end = this._io.pos;
    }

    return PuzzleActionSpawnGaribGroup;
  })();

  var PuzzleActionSetGravity = GloverLevel.PuzzleActionSetGravity = (function() {
    function PuzzleActionSetGravity(_io, _parent, _root) {
      this.__type = 'PuzzleActionSetGravity';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionSetGravity.prototype._read = function() {
      this._debug.value = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.value = this._io.readF4be();
      this._debug.value.end = this._io.pos;
      this._debug.reserved = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.reserved = this._io.readU2be();
      this._debug.reserved.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.GenericFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionSetGravity;
  })();

  var PlatSpecial0x6e = GloverLevel.PlatSpecial0x6e = (function() {
    function PlatSpecial0x6e(_io, _parent, _root) {
      this.__type = 'PlatSpecial0x6e';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSpecial0x6e.prototype._read = function() {
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.flags = this._io.readU2be();
      this._debug.flags.end = this._io.pos;
      this._debug.u320x70 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x70 = this._io.readU4be();
      this._debug.u320x70.end = this._io.pos;
    }

    return PlatSpecial0x6e;
  })();

  var PuzzleCondCameraWithinRangeOfPoint = GloverLevel.PuzzleCondCameraWithinRangeOfPoint = (function() {
    function PuzzleCondCameraWithinRangeOfPoint(_io, _parent, _root) {
      this.__type = 'PuzzleCondCameraWithinRangeOfPoint';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondCameraWithinRangeOfPoint.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.range = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.range = this._io.readF4be();
      this._debug.range.end = this._io.pos;
    }

    return PuzzleCondCameraWithinRangeOfPoint;
  })();

  var PuzzleCondBallPlatform2Todo = GloverLevel.PuzzleCondBallPlatform2Todo = (function() {
    function PuzzleCondBallPlatform2Todo(_io, _parent, _root) {
      this.__type = 'PuzzleCondBallPlatform2Todo';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondBallPlatform2Todo.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.arg2 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.arg2 = this._io.readS2be();
      this._debug.arg2.end = this._io.pos;
    }

    return PuzzleCondBallPlatform2Todo;
  })();

  var CameoInstDefault = GloverLevel.CameoInstDefault = (function() {
    function CameoInstDefault(_io, _parent, _root) {
      this.__type = 'CameoInstDefault';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    CameoInstDefault.prototype._read = function() {
      this._debug.h0x00 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.h0x00 = this._io.readU2be();
      this._debug.h0x00.end = this._io.pos;
      this._debug.h0x02 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.h0x02 = this._io.readU2be();
      this._debug.h0x02.end = this._io.pos;
    }

    return CameoInstDefault;
  })();

  var PuzzleCondPlatformPathAtPointAtRest = GloverLevel.PuzzleCondPlatformPathAtPointAtRest = (function() {
    function PuzzleCondPlatformPathAtPointAtRest(_io, _parent, _root) {
      this.__type = 'PuzzleCondPlatformPathAtPointAtRest';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondPlatformPathAtPointAtRest.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.pathPointIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.pathPointIdx = this._io.readS2be();
      this._debug.pathPointIdx.end = this._io.pos;
    }

    return PuzzleCondPlatformPathAtPointAtRest;
  })();

  var PlatOrbitAroundPoint = GloverLevel.PlatOrbitAroundPoint = (function() {
    function PlatOrbitAroundPoint(_io, _parent, _root) {
      this.__type = 'PlatOrbitAroundPoint';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatOrbitAroundPoint.prototype._read = function() {
      this._debug.axis = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.axis = this._io.readU2be();
      this._debug.axis.end = this._io.pos;
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.speed = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.speed = this._io.readF4be();
      this._debug.speed.end = this._io.pos;
    }

    return PlatOrbitAroundPoint;
  })();

  var Rope = GloverLevel.Rope = (function() {
    function Rope(_io, _parent, _root) {
      this.__type = 'Rope';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    Rope.prototype._read = function() {
      this._debug.numComponents = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.numComponents = this._io.readU4be();
      this._debug.numComponents.end = this._io.pos;
      this._debug.wiggleAxis = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.wiggleAxis = this._io.readU2be();
      this._debug.wiggleAxis.end = this._io.pos;
      this._debug.componentObjId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.componentObjId = this._io.readU4be();
      this._debug.componentObjId.end = this._io.pos;
      this._debug.name = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.name = KaitaiStream.bytesToStr(this._io.readBytes(8), "ASCII");
      this._debug.name.end = this._io.pos;
      this._debug.puzzleUnknown1 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.puzzleUnknown1 = this._io.readF4be();
      this._debug.puzzleUnknown1.end = this._io.pos;
      this._debug.swayUnknown1 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.swayUnknown1 = this._io.readF4be();
      this._debug.swayUnknown1.end = this._io.pos;
      this._debug.swayUnknown2 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.swayUnknown2 = this._io.readF4be();
      this._debug.swayUnknown2.end = this._io.pos;
      this._debug.swayUnknown3 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.swayUnknown3 = this._io.readF4be();
      this._debug.swayUnknown3.end = this._io.pos;
      this._debug.swayRockingTheta = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.swayRockingTheta = this._io.readU4be();
      this._debug.swayRockingTheta.end = this._io.pos;
      this._debug.swayUnknown4 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.swayUnknown4 = this._io.readU4be();
      this._debug.swayUnknown4.end = this._io.pos;
      this._debug.swayUnknown5 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.swayUnknown5 = this._io.readF4be();
      this._debug.swayUnknown5.end = this._io.pos;
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.componentW = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.componentW = this._io.readF4be();
      this._debug.componentW.end = this._io.pos;
      this._debug.componentH = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.componentH = this._io.readF4be();
      this._debug.componentH.end = this._io.pos;
      this._debug.componentD = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.componentD = this._io.readF4be();
      this._debug.componentD.end = this._io.pos;
    }

    return Rope;
  })();

  var PlatStr0x7a = GloverLevel.PlatStr0x7a = (function() {
    function PlatStr0x7a(_io, _parent, _root) {
      this.__type = 'PlatStr0x7a';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatStr0x7a.prototype._read = function() {
      this._debug.u320x0c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x0c = this._io.readU4be();
      this._debug.u320x0c.end = this._io.pos;
      this._debug.u320x10 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x10 = this._io.readU4be();
      this._debug.u320x10.end = this._io.pos;
      this._debug.u320x14 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x14 = this._io.readU4be();
      this._debug.u320x14.end = this._io.pos;
      this._debug.u160x18 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x18 = this._io.readU2be();
      this._debug.u160x18.end = this._io.pos;
      this._debug.u160x1c = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u160x1c = this._io.readU2be();
      this._debug.u160x1c.end = this._io.pos;
    }

    return PlatStr0x7a;
  })();

  var EnemyInstructionGoto = GloverLevel.EnemyInstructionGoto = (function() {
    function EnemyInstructionGoto(_io, _parent, _root) {
      this.__type = 'EnemyInstructionGoto';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyInstructionGoto.prototype._read = function() {
      this._debug.instrIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.instrIdx = this._io.readU4be();
      this._debug.instrIdx.end = this._io.pos;
      this._debug.unused = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.unused = this._io.readU4be();
      this._debug.unused.end = this._io.pos;
    }

    return EnemyInstructionGoto;
  })();

  var PuzzleCondGloverStandingOnPlatform = GloverLevel.PuzzleCondGloverStandingOnPlatform = (function() {
    function PuzzleCondGloverStandingOnPlatform(_io, _parent, _root) {
      this.__type = 'PuzzleCondGloverStandingOnPlatform';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondGloverStandingOnPlatform.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.invertResult = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.invertResult = this._io.readS2be();
      this._debug.invertResult.end = this._io.pos;
    }

    return PuzzleCondGloverStandingOnPlatform;
  })();

  var PuzzleCondGloverWithinRangeOfPoint = GloverLevel.PuzzleCondGloverWithinRangeOfPoint = (function() {
    function PuzzleCondGloverWithinRangeOfPoint(_io, _parent, _root) {
      this.__type = 'PuzzleCondGloverWithinRangeOfPoint';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondGloverWithinRangeOfPoint.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.range = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.range = this._io.readF4be();
      this._debug.range.end = this._io.pos;
    }

    return PuzzleCondGloverWithinRangeOfPoint;
  })();

  var EnemyInstructionA = GloverLevel.EnemyInstructionA = (function() {
    function EnemyInstructionA(_io, _parent, _root) {
      this.__type = 'EnemyInstructionA';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyInstructionA.prototype._read = function() {
      this._debug.u320x02 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x02 = this._io.readU4be();
      this._debug.u320x02.end = this._io.pos;
      this._debug.u320x06 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x06 = this._io.readU4be();
      this._debug.u320x06.end = this._io.pos;
      this._debug.u320x0a = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x0a = this._io.readU4be();
      this._debug.u320x0a.end = this._io.pos;
      this._debug.u320x0e = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.u320x0e = this._io.readU4be();
      this._debug.u320x0e.end = this._io.pos;
    }

    return EnemyInstructionA;
  })();

  var PlatSpecial0xb9 = GloverLevel.PlatSpecial0xb9 = (function() {
    function PlatSpecial0xb9(_io, _parent, _root) {
      this.__type = 'PlatSpecial0xb9';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSpecial0xb9.prototype._read = function() {
    }

    return PlatSpecial0xb9;
  })();

  var PuzzleCondBallPlatformTodo = GloverLevel.PuzzleCondBallPlatformTodo = (function() {
    function PuzzleCondBallPlatformTodo(_io, _parent, _root) {
      this.__type = 'PuzzleCondBallPlatformTodo';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleCondBallPlatformTodo.prototype._read = function() {
      this._debug.platTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.platTag = this._io.readU2be();
      this._debug.platTag.end = this._io.pos;
      this._debug.invertResult = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.invertResult = this._io.readS2be();
      this._debug.invertResult.end = this._io.pos;
    }

    return PuzzleCondBallPlatformTodo;
  })();

  var EnemyAttackInstruction = GloverLevel.EnemyAttackInstruction = (function() {
    function EnemyAttackInstruction(_io, _parent, _root) {
      this.__type = 'EnemyAttackInstruction';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemyAttackInstruction.prototype._read = function() {
      this._debug.instr = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.instr = new EnemyInstruction(this._io, this, this._root);
      this._debug.instr.end = this._io.pos;
    }

    return EnemyAttackInstruction;
  })();

  var CameoSetCameraAttention = GloverLevel.CameoSetCameraAttention = (function() {
    function CameoSetCameraAttention(_io, _parent, _root) {
      this.__type = 'CameoSetCameraAttention';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    CameoSetCameraAttention.prototype._read = function() {
      this._debug.enemyIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.enemyIdx = this._io.readU2be();
      this._debug.enemyIdx.end = this._io.pos;
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.frameCount = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.frameCount = this._io.readS2be();
      this._debug.frameCount.end = this._io.pos;
      this._debug.precedingInstrIdx = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.precedingInstrIdx = this._io.readS2be();
      this._debug.precedingInstrIdx.end = this._io.pos;
    }

    return CameoSetCameraAttention;
  })();

  var LandActor = GloverLevel.LandActor = (function() {
    function LandActor(_io, _parent, _root) {
      this.__type = 'LandActor';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    LandActor.prototype._read = function() {
      this._debug.objectId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.objectId = this._io.readU4be();
      this._debug.objectId.end = this._io.pos;
      this._debug.name = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.name = KaitaiStream.bytesToStr(this._io.readBytes(8), "ASCII");
      this._debug.name.end = this._io.pos;
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
    }

    return LandActor;
  })();

  var MrTip = GloverLevel.MrTip = (function() {
    function MrTip(_io, _parent, _root) {
      this.__type = 'MrTip';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    MrTip.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.messageId = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.messageId = this._io.readU2be();
      this._debug.messageId.end = this._io.pos;
    }

    return MrTip;
  })();

  var CameraSpawnPoint = GloverLevel.CameraSpawnPoint = (function() {
    function CameraSpawnPoint(_io, _parent, _root) {
      this.__type = 'CameraSpawnPoint';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    CameraSpawnPoint.prototype._read = function() {
      this._debug.x = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.x = this._io.readF4be();
      this._debug.x.end = this._io.pos;
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.z = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.z = this._io.readF4be();
      this._debug.z.end = this._io.pos;
      this._debug.pitch = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.pitch = this._io.readF4be();
      this._debug.pitch.end = this._io.pos;
      this._debug.yaw = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.yaw = this._io.readF4be();
      this._debug.yaw.end = this._io.pos;
    }

    return CameraSpawnPoint;
  })();

  var PuzzleActionChangeWaterHeight = GloverLevel.PuzzleActionChangeWaterHeight = (function() {
    function PuzzleActionChangeWaterHeight(_io, _parent, _root) {
      this.__type = 'PuzzleActionChangeWaterHeight';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionChangeWaterHeight.prototype._read = function() {
      this._debug.y = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.y = this._io.readF4be();
      this._debug.y.end = this._io.pos;
      this._debug.puzzleTag = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.puzzleTag = this._io.readS2be();
      this._debug.puzzleTag.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.GenericFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionChangeWaterHeight;
  })();

  var PlatSpinFlip = GloverLevel.PlatSpinFlip = (function() {
    function PlatSpinFlip(_io, _parent, _root) {
      this.__type = 'PlatSpinFlip';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PlatSpinFlip.prototype._read = function() {
      this._debug.cooldownTimer = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.cooldownTimer = this._io.readU2be();
      this._debug.cooldownTimer.end = this._io.pos;
      this._debug.theta = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.theta = this._io.readF4be();
      this._debug.theta.end = this._io.pos;
    }

    return PlatSpinFlip;
  })();

  var EnemySetAttentionBbox = GloverLevel.EnemySetAttentionBbox = (function() {
    function EnemySetAttentionBbox(_io, _parent, _root) {
      this.__type = 'EnemySetAttentionBbox';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    EnemySetAttentionBbox.prototype._read = function() {
      this._debug.left = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.left = this._io.readF4be();
      this._debug.left.end = this._io.pos;
      this._debug.top = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.top = this._io.readF4be();
      this._debug.top.end = this._io.pos;
      this._debug.front = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.front = this._io.readF4be();
      this._debug.front.end = this._io.pos;
      this._debug.width = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.width = this._io.readF4be();
      this._debug.width.end = this._io.pos;
      this._debug.height = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.height = this._io.readF4be();
      this._debug.height.end = this._io.pos;
      this._debug.depth = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.depth = this._io.readF4be();
      this._debug.depth.end = this._io.pos;
    }

    return EnemySetAttentionBbox;
  })();

  var PuzzleActionCameraLookAtPoint1 = GloverLevel.PuzzleActionCameraLookAtPoint1 = (function() {
    function PuzzleActionCameraLookAtPoint1(_io, _parent, _root) {
      this.__type = 'PuzzleActionCameraLookAtPoint1';
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this._debug = {};

      this._read();
    }
    PuzzleActionCameraLookAtPoint1.prototype._read = function() {
      this._debug.camX = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.camX = this._io.readF4be();
      this._debug.camX.end = this._io.pos;
      this._debug.camY = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.camY = this._io.readF4be();
      this._debug.camY.end = this._io.pos;
      this._debug.camZ = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.camZ = this._io.readF4be();
      this._debug.camZ.end = this._io.pos;
      this._debug.reserved = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.reserved = this._io.readU4be();
      this._debug.reserved.end = this._io.pos;
      this._debug.reserved2 = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.reserved2 = this._io.readU2be();
      this._debug.reserved2.end = this._io.pos;
      this._debug.activationDelay = { start: this._io.pos, ioOffset: this._io.byteOffset };
      this.activationDelay = this._io.readU2be();
      this._debug.activationDelay.end = this._io.pos;
      this._debug.flags = { start: this._io.pos, ioOffset: this._io.byteOffset, enumName: "GloverLevel.PuzzleAction.CameraFlags" };
      this.flags = this._io.readU4be();
      this._debug.flags.end = this._io.pos;
    }

    return PuzzleActionCameraLookAtPoint1;
  })();

  return GloverLevel;
})();
return GloverLevel;
}));
