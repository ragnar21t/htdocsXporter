import os
import sys
import shutil

htdocsPath = "C:/xampp/htdocs/" # htdocs Folder Path
destinationPath = os.getcwd(); # The folder where the .exe is executed.

# Ask what folder from htdocs you want to copy
input_FolderToCopy = input() 

# The final destinationPath, which is the current folder + the folder that's copied name
destinationPath = destinationPath + "/" + input_FolderToCopy

# Full path of the folder you want to copy
folderToCopyPath = htdocsPath + input_FolderToCopy

# Copying content from               source    >    destination
copiedContent = shutil.copytree(folderToCopyPath, destinationPath)