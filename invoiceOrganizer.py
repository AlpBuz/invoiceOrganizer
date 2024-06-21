import glob
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
    


def main():
    #have user enter the path to the file
    directory = get_directory()
    
    files = os.listdir(directory)
    print("files in folder: {files}")






    return None









if __name__ == "__main__":
    main()
