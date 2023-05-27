from win11toast import toast
import os, subprocess
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

path = "./testFolder"
realPath= os.path.realpath(path)
print(realPath)

openPath = lambda x: subprocess.run([FILEBROWSER_PATH, realPath])
toast('Hello Python', 'Click to open url', on_click=openPath, on_dismissed=lambda x: None )