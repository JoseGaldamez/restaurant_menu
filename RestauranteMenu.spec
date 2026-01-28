# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew  # <--- 1. IMPORTANTE: Importar dependencias de Kivy

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    # 2. IMPORTANTE: Agregar los árboles de dependencias gráficas aquí
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    name='RestauranteMenu',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False, # <--- 3. Pon False para ocultar la terminal negra
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)