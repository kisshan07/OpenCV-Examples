"""
THIS CODE IS HELP YOU TO UNDERSTAND SOME OF THE OPENCV TOPICS .. THANK U NOW ENJOY..
"""

import cv2 as cv

#importing opencv library

img = cv.imread(filename="")
"""
Here we are declaring a object named img which calls cv.imread() function.

* cv.imread() function take one parameter which is file path or image path which you want to read.
  It takes one more parameter i.e cv.IMREAD_COLOR this reads image in a color form i.e RGB form, this is the default 
  parameter which not really needs to pass.
  
  cv.IMREAD_UNCHANGED this reads image in RGBA form i.e it also read the transparency.
  cv.IMREAD_GRAYSCALE this reads image in Grey form i.e said to be black and white ig XD...

"""

print(img.shape)

"""
img.shape :- it return a tuple of integer which is in the forms (100,100,100) .
THIS TUPLE CONSIST OF THREE VALUES FIRST TWO ARE HEIGHT AND WIDHT AND LAST ONE IS FOR COLOUR CHANNEL.
"""