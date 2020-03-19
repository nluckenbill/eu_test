# Create directories script from a list of files
import os
import re
import glob
import shutil

# Search directory for markdown files and new directories
dir = "C:\\test"
# remove dashes and numbers in fron of the text
regex = r"^[-\d\s]+"

# Set working directory
os.chdir(dir)

# Collect md file names and cleanb= up name
def createDirectories():
    for files in glob.glob("*.md"):
        global regex
        new_md_name = re.sub(regex, "", files, 0, re.MULTILINE)
    #    print(new_md_name)

    # Make directories from md file names
        dir = "C:\\test\\"
        regex = r"(.md)"
        path = dir + new_md_name
        path = re.sub(regex, "", path, 0, re.MULTILINE)
     #   print(path)
        os.mkdir(path)



def moveMdFiles():
    for files in glob.glob("*.md"):
        
        # Get folder name by cleaning up file names
        regex = r"^[-\d\s]+"
        folder_name = re.sub(regex, "", files, 0, re.MULTILINE)
        regex = r"(.md)"
        folder_name = re.sub(regex, "", folder_name, 0, re.MULTILINE)
        print(folder_name)
        
        # Set dir directory
        dir = "C:\\test\\"
       
       # Destination Directory
        dest_dir = dir + folder_name
        print(dest_dir)
       
       # Move files into folder
        shutil.move(f"{dir}{files}", f"{dest_dir}\\index.md")


def main():
    createDirectories()
    moveMdFiles()

if __name__ == "__main__":
    main()