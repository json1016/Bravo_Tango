import os
import shutil

import PyInstaller.__main__

files = ["build", "dist", "main.spec"]
for f in files:
    if os.path.exists(f):
        try:
            os.remove(f)
        except PermissionError:
            shutil.rmtree(f)
PyInstaller.__main__.run([
    "main.py"
])
exe_path = "..\\exe"
if os.path.exists(exe_path):
    for f in os.listdir(exe_path):
        os.remove(f)
else:
    os.mkdir(exe_path)
for f in files:
    os.replace(f, f"{exe_path}\\{f}")
