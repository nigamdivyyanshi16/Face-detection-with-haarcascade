import cv2
import random

trainedData= cv2.CascadeClassifier("Face.xml")
print(trainedData)
# Staring the webcam
webcam= cv2.VideoCapture(0) #It enable the webcam
# In the above function,VideoCapture(), wehave given 0 when we want to open the webcam, and when we want to open any video file then we have to give the file name instead of 0.

# video is simply picture frame which is moving so fast that it seems like it is a video. So from that initiallly we have to capture a single frame.

# success,img=webcam.read()

# So, read function capture the webcam and read() function gives two values in output that we have taken in those 2 variables. It gives success or failure(True or False)  as first nad secondly it give that image which will captured at that particular moment.

# cv2.imshow("webcamimg",img)

# Now we get that single frame image but we want all the frame, so to capture all frames, we ca use while loop.
while True:
      success, img = webcam.read()

      grayimage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert that captured image into grayscale.

      # now for drawing rectangle, we have to fing the face coordinates.

      faceCoordinate= trainedData.detectMultiScale(grayimage)
      for x,y,w,h in faceCoordinate:
            cv2.rectangle(img, (x, y), (x+w, y+h), (random.randint(0, 255),
                              random.randint(0, 255), random.randint(0, 255)),2)

      cv2.imshow("webcamImg",img)
      # cv2.waitKey() #It captues which key is pressed.
      #key= cv2.waitKey() #Now whichever the key is presssed, it will in key variable.
      # Here this function creates a problem that it will not changing the frame, for changing it we have to press the key other "q". So to deal with that problem, we pass a time in miliseconds, that after that ms, it will change the frame.

      key = cv2.waitKey(1)
      if (key==81 or key==113):
            break
# After getting outside of the loop, we have to close the webcam.
webcam.release()





