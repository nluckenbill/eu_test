import os
import glob
from PIL import Image
from resizeimage import resizeimage

# Variables


# Get width x hight of all images in directory


for files in glob.glob('./content/**/*.jpg', recursive=True):
    if files:
        im = Image.open(files)
        width, height = im.size
#        print(files, ":", width, "x", height)
        width = int(width)
        if width > 1600:
            fd_img = open(files, 'r')
            img = Image.open(fd_img)
            img = resizeimage.resize_width(img, 1600)
            img.save(files, img.format)
            fd_img.close()
            print(files, ":", width, "x", height)
