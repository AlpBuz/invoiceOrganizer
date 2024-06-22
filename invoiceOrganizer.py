import shutil
import os
import tkinter as tk
from tkinter import filedialog

def getFolder(messagePrompt):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.update()
    # Open the folder selection dialog
    folderPath  = filedialog.askdirectory(title= messagePrompt)
    root.destroy()
    return folderPath 
    



def checkFolderExists(destination):
    if os.path.exists(destination):
        return True

    return False



def moveFile(oldpath, destination):
    try:
        shutil.move(oldpath, destination)
        print(f"File moved successfully from '{oldpath}' to '{destination}'.") 
    except Exception as e:
        print(f"Error moving file: {e}")



def getDestination(file): #Organize the files to folders based on the users first letter in the first or last name. goes by last name first.
    fileNameSplit = file.split()

    if len(fileNameSplit) == 1:
        reval = fileNameSplit[0][0]
        reval = reval.upper()
        return reval
    else:
        reval = fileNameSplit[-1][0]
        reval = reval.upper()
        return reval
    

def subFolders(parentFolder):

    return False





def main():
    #have user enter the path to the file
    directory = getFolder("Choice the folder that has the files you want to move")
    items = os.listdir(directory)
    destination = getFolder("Choice the folder that you want the files to be moved to")
    
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith('.pdf'):
                # Full path to the PDF file
                source_file_path = os.path.join(dirpath, filename)
                
                # Determine destination folder based on file name (placeholder function)
                file_destination_name = getDestination(filename)
                file_destination_path = os.path.join(destination, file_destination_name)
                
                # Ensure the destination folder exists, create it if not
                if not checkFolderExists(file_destination_path):
                    os.makedirs(file_destination_path)
                
                # Move the file to the destination folder
                moveFile(source_file_path, file_destination_path)
                print(f"Moved file: {filename} to {file_destination_path}")



        

    print("File Movement completed")



if __name__ == "__main__":
    main()
