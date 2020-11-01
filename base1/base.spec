# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Base.py'],
             pathex=['C:\\Users\\t_koga\\Desktop\\Base\\base1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          Tree('resources',prefix='resources'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Base',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
