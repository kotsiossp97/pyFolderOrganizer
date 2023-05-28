Quick Start Guide
=================

Overview of the package
-----------------------

pyFolderOrganizer organizes files in a given directory, in sub-folders, based on the extension of each file. The folder names and the corresponding extensions are described in the table below.

The package offers the ability to observe the directory for changes and when a file is detected, it is organized automatically.

Package setup
-------------

from PyPi::

    # install the last available version
    pip install pyFolderOrganizer
    # or upgrade from an older version
    pip install pyFolderOrganizer --upgrade

from GitHub::

    git clone https://github.com/kotsiossp97/pyFolderOrganizer.git
    cd pyFolderOrganizer
    python setup.py install

Basic Initialization
--------------------
Initalize module::

    import pyFolderOrganizer

    path = "path/to/be/organized"
    organizer = pyFolderOrganizer.FolderOrganizer(path)

Available Extensions
--------------------
+---------------+-------------------------------------------------------+
| Folder Name   | Extensions                                            |
+===============+=======================================================+
| PDF           | .pdf                                                  |
+---------------+-------------------------------------------------------+
| CodeFiles     | .py, .c, .cpp, .java, .h, .html, .php, .js, .tsx      |
+---------------+-------------------------------------------------------+
| OfficeFiles   | .txt, .doc, .docx, .xls, .xlsx, .accdb, .ppt, .pptx   |
+---------------+-------------------------------------------------------+
| MusicFiles    | .mp3, .wav, .flac                                     |
+---------------+-------------------------------------------------------+
| ImageFiles    | .jpg, .jpeg, .png, .gif, .dds                         |
+---------------+-------------------------------------------------------+
| Compressed    | .zip, .rar, .7z, .gz                                  |
+---------------+-------------------------------------------------------+
| Executables   | .exe, .msi                                            |
+---------------+-------------------------------------------------------+
| General       | All other file extensions                             |
+---------------+-------------------------------------------------------+