import os, sys, time, subprocess, threading
from win11toast import notify, toast
from watchdog.observers import Observer
from .Internal.FileHandler import FileHandler

class FolderOrganizer:
    
    def __init__(self, directory:str, observe:bool=False, printing:bool=True, notifications:bool=False):
        """Organizes the files in the given folder in sub folders by file types.

        :param directory: Path of the folder to be organized, can be full or relative path.
        :type directory: str
        :param observe: Tracks the folder for changes and automatically organizes files. Defaults to False.
        :type observe: bool
        :param printing: If true, prints messages to the console. Defaults to True.
        :type printing: bool
        :param notifications: If true, creates windows toast messages. Defaults to False.
        :type notifications: bool
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
        opener = ['explorer']
        if (sys.platform != 'win32'):
            opener = ['open']
            
        subprocess.run(opener + [self.directory])
    
    # Private Class Methods
    def __notify(self, title:str, message:str, callbackOnClick=None):
        if(self.notifications):
            # notify(title, message, on_click=callbackOnClick)
            toast(title, message, on_click=lambda x: callbackOnClick())
            
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
        

    # Property Class Methods
    @property
    def directory(self):
        """Get or Set the folder directory to be organized. Any existing path will be accepted.
        """
        return self._directory
    
    @property
    def observe(self):
        """Enable or disable observer mode, boolean value is accepted."""
        return self._observe
    
    @property
    def printing(self):
        """Enable or disable console printing, boolean value is accepted."""
        return self._printing
    
    @property
    def notifications(self):
        """Enable or disable windows notifications, boolean value is accepted."""
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
