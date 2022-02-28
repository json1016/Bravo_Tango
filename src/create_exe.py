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
exe_path = "..\\exe"
if os.path.exists(exe_path):
    shutil.rmtree(exe_path)
os.mkdir(exe_path)
PyInstaller.__main__.run([
    "main.py",
    "--onefile",
    "--noconsole"
])
for f in files:
    os.replace(f, f"{exe_path}\\{f}")
