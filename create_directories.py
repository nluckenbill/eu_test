# Create directories script from a list of files
import os
import re
import glob
import shutil
import colorama
from colorama import Fore

# Search directory for markdown files and new directories
dir = "C:\\Users\\Nate\\Documents\\WebSites\\eu_test\\content\\post"
# remove dashes and numbers in fron of the text


# Set working directory
os.chdir(dir)

# Collect md file names and cleanb= up name
def createDirectories():
    for files in glob.glob("*.md"):
        regex = r"^[-\d\s]+"
        new_md_name = re.sub(regex, "", files, 0, re.MULTILINE)

    # Make directories from md file names
        dir = "C:\\Users\\Nate\\Documents\\WebSites\\eu_test\\content\\post\\"
        regex = r".md"
        path = dir + new_md_name
        path = re.sub(regex, "", path, 0, re.MULTILINE)
        if not os.path.exists(path):
            os.mkdir(path)
            print("Directory ", path, " Created ")
        else:
            
            print("Directory ", path, " already exists ")




def moveMdFiles():
    for files in glob.glob("*.md"):
        
        # Get folder name by cleaning up file names
        regex = r"^[-\d\s]+"
        folder_name = re.sub(regex, "", files, 0, re.MULTILINE)
        regex = r"(.md)"
        folder_name = re.sub(regex, "", folder_name, 0)
        print(folder_name)
        
        # Set dir directory
        dir = "C:\\Users\\Nate\\Documents\\WebSites\\eu_test\\content\\post\\"
       
       # Destination Directory
        dest_dir = dir + folder_name
        print(dest_dir)
       
       # Move files into folder
        shutil.move(f"{dir}{files}", f"{dest_dir}\\index.md")


def main():
    createDirectories()
#    moveMdFiles()

if __name__ == "__main__":
    main()