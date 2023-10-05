"""           Steps to train algorithm

step 1: collect tons of faces.
step 2: make them black and white.
step 3: Train the algorithm to detect faces.

(Reasons known will be later)


To make this project, we use openCV(open source Computer Vision Library of python). It is easy to use and simple function.

"""




import random #for giving different colors to all rectangles

import cv2 # For importing openCV , we write cv2

"""So, we follow the above steps: we take a image and make it black and white and send it to algorithm and find out the coordinates of ractangle nad then draw it."""

# dataset load
trainedData=cv2.CascadeClassifier("F:\\python\\FaceDetectionProject\\lowerBody.xml") #It will classify the face in the image.
# trainedData=cv2.CascadeClassifier("Eyes.xml") #It will classify the eyes in the image.


# Choose the image.

img = cv2.imread("F:\\python\\FaceDetectionProject\\imageFolder\\img\\allcerti.jpg")
# img = cv2.imread("C:\\Users\\sanka\\OneDrive\\Desktop\\python\\FaceDetectionProject\\imageFolder\\img\\chaiWithsimanshi.jpg")


# Now, if that algorithm will detect an face then what will it return. We know, an image is an matric of bunch pixels with numbers bits.
grayimage= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #it will convert img to grayscale. BGR is nothing but an RGB sequence,, in openCV, it BGR not RGB.

# faceCoordinate = trainedData.detectMultiScale(img)

faceCoordinate= trainedData.detectMultiScale(grayimage) #this function returns the coordinates of faces detected.
print(faceCoordinate) #printing face coordinates
# you will get: [[653 146 346 346]], this is a nested list and you get only one list inside it, bcoz in that image only one face is present , if there are multiple faces then more list present in it.

# In that list, in a list, 4 values are present, in that first two values are the (x,y)=>(653,146) ,and other two values width and height.

# Object are detected and returned as list of rectangles coordinates.

# x,y,w,h= faceCoordinate[0] #unpacking the values of the first list present in the list.
# Now we get the points.

# Now we have to draw rectangle, ANd now that rectangle i want on the main image not on the grayscale.

# For drawing rectangle, we have:
# cv2.rectangle(img,(x,y),(x+w,y+h),(25,184,56),2)
# In the above function, we first provide on which image I want to draw rectangle and then give the starting coordinates, then (x+w,y+h) manages other coordinates, then provide the rgb vales for the color of ractangle and then the thickness of ractangle.

for i in faceCoordinate:
      x,y,w,h=i
      # cv2.rectangle(img, (x, y), (x+w, y+h), (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 2)
      center = (x + w//2, y + h//2)
      cv2.ellipse(img, center, (w//2, h//2), 0, 0, 360, (random.randint(0,
                  255), random.randint(0, 255), random.randint(0, 255)), 2)

# displaying the choosen the image.

cv2.imshow('SingleImage',img) # It takes 2 argument, first one is the name of window in which it will appear bad second is the choosen image variable.

# Here, a window will appear and gets disappear instantly , so we have to handle that situation, we can place a condition that it will nor disappear until we pressed any key.

cv2.waitKey() #screen will not disappear until we do not press any key.
# waitKey(): it will stops the program execution.

# Next steps is to convert into grayscale bcoz openCV works on grayscale image only.

# cvtColor() will convert the color

# displaying that grayscale image:
# cv2.imshow('Singleimage',grayimage)
# cv2.waitKey()

# cv2.namedWindow("SingleImage",cv2.WND_PROP_FULLSCREEN)



print("End of program")
