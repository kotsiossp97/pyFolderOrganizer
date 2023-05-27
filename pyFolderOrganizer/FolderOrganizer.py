import os, time, subprocess, threading
from win11toast import notify
from watchdog.observers import Observer
from .Internal.FileHandler import FileHandler

class FolderOrganizer:
    FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
    
    def __init__(self, directory:str, observe:bool=False, printing:bool=True, notifications:bool=False):
        """Organizes the files in the given folder in sub folders by file types.

        Args:
            directory (str): Path of the folder to be organized, can be full or relative path.
            observe (bool, optional): Tracks the folder for changes and automatically organizes files. Defaults to False.
            printing (bool, optional): If true, prints messages to the console. Defaults to True.
            notifications (bool, optional): If true, creates windows toast messages. Defaults to False.
        """
        
        # private class properties
        self._directory = None
        self._observe = False
        self._printing = True
        self._notifications = False
        self.__observer = None
        # public properties
        self.directory = directory
        self.observe = observe
        self.notifications = notifications
        self.observer = Observer()

        self.__onInit()
        
    # Public Class Methods
    def organize(self):
        """Organizes the folder in sub-folders
        """
        toastTitle = "pyFolderOrganizer"
        toastMsg   = f"Folder Organizer started successfully!\n\nOrganizing directory: {self.directory}\n"
        self.__notify(toastTitle, toastMsg, self.openFolder)
        
        handler = FileHandler(self.directory, self.__notify)
        handler.organize()
        
    def openFolder(self):
        """Opens the folder that is organized in a new Explorer window.
        """
        subprocess.run([FolderOrganizer.FILEBROWSER_PATH, self.directory])
        
    # Private Class Methods
    def __notify(self, title:str, message:str, callbackOnClick=None):
        if(self.notifications):
            notify(title, message, on_click=lambda x: callbackOnClick())
            # self.__toaster.show_toast(title, message, duration=3, threaded=True, callback_on_click=callbackOnClick)
        elif self.printing:
            print(message)

    def __onInit(self):
        if self.observe:
            self.__observeThread = threading.Thread(target=self.__observeTarget)
            self.__observeThread.start()
            try:
                while True:
                    time.sleep(1)
            except (KeyboardInterrupt, SystemExit):
                return
        else:
            self.organize()
            
    def __observeTarget(self):
        if not self.observe:
            return
        
        toastTitle = "pyFolderOrganizer"
        toastMsg   = f"Folder Organizer started successfully!\n\nOrganizing directory: {self.directory}\n"

        self.observer.schedule(FileHandler(self.directory, self.__notify), self.directory, recursive=False)
        self.observer.start()
        
        self.__notify(toastTitle, toastMsg, self.openFolder)

        
    def __onFileMoved(self, filePath:str):
        toastTitle = "pyFolderOrganizer"
        fileName = ""
        toastMsg   = f"File {fileName} was organized."
        self.__notify(toastTitle, toastMsg)
    
    def __scanForFiles(self):
        for filename in os.listdir(self.directory):
            print(filename)
    # Property Class Methods
    @property
    def directory(self):
        return self._directory
    
    @property
    def observe(self):
        return self._observe
    
    @property
    def printing(self):
        return self._printing
    
    @property
    def notifications(self):
        return self._notifications

    @property
    def observer(self):
        return self.__observer
    
    # Property Setter Methods
    @directory.setter
    def directory(self, newDir:str):
        newDirectory = os.path.abspath(newDir)
        
        if(os.path.exists(newDirectory)):
            self._directory = newDirectory
            return
        raise ValueError("Directory does not exist.")
    
    @observe.setter
    def observe(self, value: bool):
        self._observe = value
    
    @printing.setter
    def printing(self, value:bool):
        self._printing = value
        
    @notifications.setter
    def notifications(self, notif:bool):
        self._notifications = notif
        
    @observer.setter
    def observer(self, value:Observer):
        if self.observe:
            self.__observer = Observer()
        else:
            self.__observer = None
    # Static Class Methods
    @staticmethod
    def isFileMovable(filePath):
        movable = False
        if(os.path.exists(filePath)):
            try:
                f = open(filePath,'a',8)
                movable = True
            except:
                movable = False
        else:
            raise Exception("File does not exist.")
        return movable

    @staticmethod
    def waitForFileMovable(filePath):
        while( not FolderOrganizer.isFileMovable(filePath)):
            time.sleep(5)
