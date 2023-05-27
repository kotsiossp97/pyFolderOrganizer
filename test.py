import pyFolderOrganizer
path = "./testFolder"
path2 = "./testFolder2"

# Files organized on initialization
organizer = pyFolderOrganizer.FolderOrganizer(path)

# If directory is changed, call .organize() method to organize the new path
organizer.directory = path2
organizer.organize()