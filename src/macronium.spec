from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path
import os
path = os.path.abspath(".")

if 'src' not in path:
    path = path + '\\\\src'
    
block_cipher = None


a = Analysis(['macronium.py'],
             pathex=[path],
             binaries=[],
             datas=[],
             hiddenimports=['pynput.keyboard._win32','pynput.mouse._win32'],
             hookspath=[kivymd_hooks_path],
             hooksconfig={},
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
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Macronium',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon = path + '\\ICON.ico',
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
