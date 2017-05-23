# -*- coding: utf-8 -*-


import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    "build_exe": {
        "includes" : "atexit",
        "packages": ["time", "datetime", "email", "smtplib", "re", "six"]
    }
}

executables = [
    Executable('main.py', base=base)
]

setup(name='py_mail',
      version='0.1',
      description='Sample mail client',
      options=options,
      executables=executables
      )
