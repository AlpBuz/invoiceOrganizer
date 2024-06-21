import shutil
import os

def get_directory():
    while True:
        # Prompt the user to enter the directory path
        directory = input("Please enter the directory path: ")

        # Validate if the entered path is a valid directory
        if os.path.isdir(directory):
            print(f"The entered directory is: {directory}")
            return directory
        else:
            print("Invalid directory path. Please try again.\n")
    

def destinationFolder():
    while True:
        # Prompt the user to enter the directory path
        Destination = input("Please enter the Destination path: ")

        # Validate if the entered path is a valid directory
        if os.path.isdir(Destination):
            print(f"The entered Destination is: {Destination}")
            return Destination
        else:
            print("Invalid Destination path. Please try again.\n")
    



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
    directory = get_directory()
    pdf_Files = os.listdir(directory)
    destination = destinationFolder()
    

    #start moving the files

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
