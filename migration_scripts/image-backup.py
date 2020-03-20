import os
import glob
from PIL import Image
from resizeimage import resizeimage
import re
import shutil

#regex = r".*thumbs.*|.*dynamic.*\n"
regex = r"^((?!dynamic|thumbs).)*$"


# Get width x hight of all images in directory


for folders in glob.glob('C:/Users/Nate/Documents/elevationUpgrade/gallery/**/', recursive=True):
    if folders:
#        im = Image.open(files)
#        width, height = im.size
#        print(files, ":", width, "x", height)
        
        matches = re.sub(regex, "", folders, 0, re.MULTILINE)
        if os.path.exists(matches):
         # remove if exists
         shutil.rmtree(matches)
#         print(matches)
        else:
         # throw your exception to handle this special scenario
            print ("Directory not found")

