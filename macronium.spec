from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path
import os
path = os.path.abspath(".")

block_cipher = None


a = Analysis(['macronium.py'],
             pathex=[path],
             binaries=[],
             datas=[],
             hiddenimports=['pynput.keyboard._win32','pynput.mouse._win32','pypng'],
             hookspath=[kivymd_hooks_path],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='macronium',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
	  icon = path + '\\ICON.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='macronium')
