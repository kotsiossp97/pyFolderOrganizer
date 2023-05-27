from enum import Enum


class FileExtensions(Enum):
    PDF_FILES           = ("PDF", ['.pdf'])
    CODE_FILES          = ("CodeFiles", [ '.py', '.c', '.cpp', '.java', '.h', '.html', '.php', '.js', '.tsx'])
    OFFICE_FILES        = ("OfficeFiles", [ '.txt', '.doc', '.docx', '.xls' ,'.xlsx', '.accdb', '.ppt', '.pptx'])
    MUSIC_FILES         = ("MusicFiles", [ '.mp3', '.wav', '.flac'])
    IMAGE_FILES         = ("ImageFiles", [ '.jpg', '.jpeg', '.png', '.gif', '.dds'])
    COMPRESSED_FILES    = ("Compressed", [ '.zip', '.rar', '.7z', '.gz'])
    EXE_FILES           = ("Executables", [ '.exe', '.msi'])
    OTHER_FILES         = ("General", [])
    
    def __new__(cls, folderName, extensions):
        obj = object.__new__(cls)
        obj.folderName = folderName
        obj.extensions = extensions
        return obj
    
    @staticmethod
    def getByExtension(extension:str):
        for ext in FileExtensions:
            extArray = ext.extensions
            if(extension in extArray):
                return ext
        return FileExtensions.OTHER_FILES