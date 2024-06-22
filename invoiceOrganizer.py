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





def main():
    #have user enter the path to the file
    directory = getFolder("Choice the folder that has the files you want to move")
    pdf_Files = os.listdir(directory)
    destination = getFolder("Choice the folder that you want the files to be moved to")
    

    for file in pdf_Files:
        fileDestinationName = getDestination(file) #get the destination of where the file will be stored based on the name of the file
        oldFilePath = directory + "\\" + file
        fileDestinationPath = destination + "\\" + fileDestinationName #create the path for where the file will be stored

        if not checkFolderExists(fileDestinationPath):
            os.makedirs(fileDestinationPath)
        


        moveFile(oldFilePath, fileDestinationPath)


        

    print("File Movement completed")



if __name__ == "__main__":
    main()
