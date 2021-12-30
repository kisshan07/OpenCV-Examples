"""
THIS CODE IS HELP YOU TO UNDERSTAND SOME OF THE OPENCV TOPICS .. THANK U NOW ENJOY..
"""

import cv2 as cv

#importing libraries

img = cv.imread(filename="")
"""
TIP:- You can check about cv.imread() fuction in readingimg.py file . Thank You.
"""

cv.imshow(winname="", img)

"""
cv.imshow() function takes two parameter and bot are important.
* first one is winnname which is the window title in which your image going to show up.
* second one is the img which you want to display
"""

cv.waitKey(0) #this is very important if this command is not passed the image is appear for just fraction of second.
