# pyFolderOrganizer
 Python package to organize a folder in sub-directories based on file types.

#
## Documentation
To-Do
#
## Setup
You can install this package from:

From GitHub:

```bash
pip install git+https://github.com/kotsiossp97/pyFolderOrganizer.git@latest
```

From PIP:

```bash
pip install pyFolderOrganizer
```

#
## Usage
### Basic Example
```python
import pyFolderOrganizer

path = "path/to/be/organized"
organizer = pyFolderOrganizer.FolderOrganizer(path)
```

### Observer Mode
Package offers "Observer Mode" that listens for any file created in the directory that the organizer is set to. Creates a thread and when a new file is detected, is automatically moved to the corresponding folder depending of the file extension.
```python
organizer = pyFolderOrganizer.FolderOrganizer(path, observe=True)
```

### Enable/Disable Windows Toasts
Set the `notifications` argument to True to enable windows notifications on startup and when a file gets organized.
Clicking the notification opens an explorer window to the corresponding path. This is turned off by default.
```python
organizer = pyFolderOrganizer.FolderOrganizer(path, notifications=True)
```

### Enable/Disable Console Printing
By default, the package prints messages on the console, equivalent to the notifications. This can be turned off by setting the `printing` argument:
```python
organizer = pyFolderOrganizer.FolderOrganizer(path, printing=False)
```

#
## Available Extensions
These are the folders that will contain the files with the provided extensions. Folders are auto created, so no need to create any of them.

| Folder Name   | Extensions                                            |
| ------------- | ----------------------------------------------------- |
| PDF           | .pdf                                                  |
| CodeFiles     | .py, .c, .cpp, .java, .h, .html, .php, .js, .tsx      |
| OfficeFiles   | .txt, .doc, .docx, .xls, .xlsx, .accdb, .ppt, .pptx   |
| MusicFiles    | .mp3, .wav, .flac                                     |
| ImageFiles    | .jpg, .jpeg, .png, .gif, .dds                         |
| Compressed    | .zip, .rar, .7z, .gz                                  |
| Executables   | .exe, .msi                                            |
| General       | All other file extensions                             |

### Add custom folder/extension
To-do