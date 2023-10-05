import cv2
#to capture face
face_cap=cv2.CascadeClassifier("G:/tkinter and face/haarcascade_frontalface_default.xml")
#whether our  camera is working or not
#open the webcam
#cascade function is trained from lot of positive and negative images
#to capture face classifier is used
#,.xml stands for extensible markup language which stores the data and forr transportation
#classifier is going to detect face based on xml file i.e data set loaded 
#we pass training data to detect face 
#video is a set of multiple frame
cap=cv2.VideoCapture(0)
#if camera is reading image then continue for infinte time till q is pressed
while True:
    ret,frame=cap.read()
    #image ko black and white krna pdhega
    col=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #covering the face structures
    faces=face_cap.detectMultiScale(col,
        #how much the image size is reduced at each image scale
        scaleFactor=1.1,
        #how many neighbors each candidate rectangle should have to retain it.
        minNeighbors=5,
        #minimum object size
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
        )
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    if ret==False:
        continue
    #if camera is reading then
    cv2.imshow("LIVE VIDEO FACE RECOGNITION",frame)
    #if currrently pressed key matches with this or not
    key_pressed=cv2.waitKey(1)
    #if q will be entered then only camera will be closed
    if key_pressed==ord('c'):
        break
   #closing the camera 
cap.release()
cv2.destroyAllWindows()
