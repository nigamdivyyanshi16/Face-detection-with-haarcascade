import cv2
#from random import randrange as r
#cascade fucntion is trained from lot of positive and negative images
#to capture face classifier is used
#,.xml stands for extensible markup language which stores the data and forr transportation
#classifier is going to detect face based on xml file i.e data set loaded 
face_cascade=cv2.CascadeClassifier("G:\\tkinter and face\\lowerbody.xml")
#choose the image
img=cv2.imread("G:\\tkinter and face\\dataset\\Snapchat-1805703730.jpg")
#it will open te image in grayscale mode cvt color is for changing one color space to another
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#detectMultiscale detects objects of different size no matter what the scale is
#detectmultiscale detects every possibilty of detecting face returning the coordintes of the rectangle
#coordinates are returned as a list 
faces=face_cascade.detectMultiScale(gray,1.1,4)
#face_cascade is equal to trained data stored
#2 is rectangle thickness and of rec color  
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    #r(0,256),r(0,256),r(0,256)
#show the image
cv2.imshow("image detection",img)
#paused the execution of the program until key is pressed
cv2.waitKey()