import os
from sys import executable
NAME="pyinstaller.exe"
SPLIT=b"#!"
ERROR=f"{NAME}'s struction to express python's path is changed somehow"
SCRIPTS_PATH=os.path.join(os.path.dirname(executable),'Scripts')
PYINST_PATH=os.path.join(SCRIPTS_PATH,NAME)