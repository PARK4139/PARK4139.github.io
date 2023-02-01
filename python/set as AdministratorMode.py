# -*- coding: utf-8 -*-
import sys
import win32com.shell.shell as shell
import os
import subprocess

# ____________________________________________
if sys.argv[-1] != 'asadmin':
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + ['asadmin'])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    # sys.exit(0)