"""
THIS CODE IS HELP YOU TO UNDERSTAND SOME OF THE OPENCV TOPICS .. THANK U NOW ENJOY..
"""

import cv2 as cv

#importing libraries

img = cv.imread(filename="")
"""
TIP:- You can check about cv.imread() function in readingimg.py  . Thank You.
"""

#we will do transformation on image in future

cv.imwrite(filename="", img)
"""
cv.imwrite() function is use to save an image , It takes to params one is filename i.e the name of the file or image
which shows up in file directory after saving the image and the image which you want to save.
It returns Boolean output. If file is saved it return True and if not it return False.
"""
