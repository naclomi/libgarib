# -*- mode: python ; coding: utf-8 -*-
import os.path

from PyInstaller.utils.hooks import collect_all

datas = []
binaries = []
hiddenimports = []

for lib in ('libgarib', 'capstone', 'unicorn', 'keystone'):
    tmp_ret = collect_all(lib)
    datas += tmp_ret[0]
    binaries += tmp_ret[1]
    hiddenimports += tmp_ret[2]

tool_scripts = [
    "checksum.py",
    "fla2.py",
    "hash.py",
    "level-tool.py",
    "objbank-tool.py",
    "quick-patcher.py",
    "rom-asset-tool.py",
    "texbank-tool.py",
    "tip-tool.py",
]

all_exes = []

a = Analysis(
    tool_scripts,
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

for tool_script in tool_scripts:
    exe_name = os.path.splitext(os.path.basename(tool_script))[0]
    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name=exe_name,
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=True,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
    )
    all_exes.append(exe)

coll = COLLECT(
    *all_exes,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='tools',
)
