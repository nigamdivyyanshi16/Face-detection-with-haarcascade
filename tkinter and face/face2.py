import cv2
#cascade fucntion is trained from lot of positive and negative images
#to capture face classifier is used
#,.xml stands for extensible markup language which stores the data and forr transportation
#classifier is going to detect face based on xml file i.e data set loaded 
face_cap=cv2.CascadeClassifier("C:/Users/user/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
#whether our  camera is working or not
#open the webcam and enabling the video
#it take 0 or 1 as an arguement
cap=cv2.VideoCapture(0)
#if camera is reading image then continue for infinte time till c is pressed
while True:
    #capture the image frame by frame
    #cap.read return boolean value
    ret,frame=cap.read()
    #it will open te image in grayscale mode cvt color is for changing one color space to another
    col=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #covering the face structures
    faces=face_cap.detectMultiScale(col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
        )
    for (x,y,w,h) in faces:
        #rectangle creates square around face
        #sqaure bracket should be applied around frame 
        #2 is the width
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    if ret==False:
        continue
    #if camera is reading then show the title of frame as well as the frame
    cv2.imshow("LIVE VIDEO FACE RECOGNITION",frame)
    #if currrently pressed key matches with this or not
    #waitkey helps to pause the image or video for certain period of time
    #wait key helps to play video from a file and time must be appropriate if the time is high video will be slow else very fast
    #waikey when waitkey() is wating for the key to b pressed 
    #but after 1 then after every milliseconds frame will be changed
    key_pressed=cv2.waitKey(1) & 0xFF
    #if q will be entered then only camera will be closed
    if key_pressed==ord('c'):
        break
   #closing the camera 
cap.release()
cv2.destroyAllWindows()
