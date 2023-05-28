from watchdog.events import FileSystemEventHandler
import os, subprocess, time
from .FileExtensions import FileExtensions

class FileHandler(FileSystemEventHandler):
    
    def __init__(self, folderPath:str, notifier=None):
        super().__init__()
        self.folderPath = folderPath
        self.__notify = notifier
        
    def on_modified(self, event):
        
        for fileName in os.listdir(self.folderPath):
            filePath = os.path.join(self.folderPath, fileName)
            fileExtension = os.path.splitext(filePath)[1]
            if os.path.isdir(filePath):
                continue
            
            newFolder = FileExtensions.getByExtension(fileExtension).folderName
            self.__createFolder(newFolder)
            newFilePath = self.__getNewFilePath(newFolder, fileName)
            try:
                FileHandler.waitForFileMovable(filePath)
                os.rename(filePath, newFilePath)
                self.__onFileMoved(fileName, newFolder, newFilePath)
            except Exception as e:
                print(e)
                
    def organize(self):
        self.on_modified(None)
        
    def __folderExists(self, folderName:str) -> bool:
        fullPath = os.path.join(self.folderPath, folderName)
        return os.path.exists(fullPath)
    
    def __createFolder(self, folderName:str):
        if not self.__folderExists(folderName):
            fullPath = os.path.join(self.folderPath, folderName)
            os.makedirs(fullPath)
            
    def __getNewFilePath(self, folderName:str, fileName:str):
        tempName = fileName
        newPath = os.path.join(self.folderPath, folderName, tempName )
        while os.path.exists(newPath):
            fileName = "Copy_" + tempName
            newPath = os.path.join(self.folderPath, folderName, tempName)
            
        return newPath
    
    def __onFileMoved(self, fileName:str, newFolder:str, newFilePath:str):
        msg = f"Successfully organized file {fileName} in folder {newFolder}."
        openFilePath = lambda: FileHandler.openDir(os.path.dirname(newFilePath))
        self.__notify("pyFolderOrganizer", msg, openFilePath)
        
    @staticmethod
    def openDir(directory:str):
        FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

        if os.path.exists(directory):
            subprocess.run([FILEBROWSER_PATH, directory])
    
    # Static Class Methods
    @staticmethod
    def isFileMovable(filePath):
        movable = False
        if(os.path.exists(filePath)):
            try:
                f = open(filePath,'a',8)
                if f:
                    movable = True
            except:
                movable = False
        else:
            raise Exception("File does not exist.")
        return movable

    @staticmethod
    def waitForFileMovable(filePath):
        while( not FileHandler.isFileMovable(filePath)):
            time.sleep(5)