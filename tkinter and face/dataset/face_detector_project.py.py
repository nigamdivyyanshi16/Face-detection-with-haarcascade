import cv2
#to capture face
face_cap=cv2.CascadeClassifier("C:/Users/user/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
#whether our  camera is working or not
#open the webcam
cap=cv2.VideoCapture(0)
#if camera is reading image then continue for infinte time till q is pressed
while True:
    ret,frame=cap.read()
    #image ko black and white krna pdhega
    col=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #covering the face structures
    faces=face_cap.detectMultiScale(col,
        scaleFactor=1.1,
        minNeighbors=5,
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
    key_pressed=cv2.waitKey(1) & 0xFF
    #if q will be entered then only camera will be closed
    if key_pressed==ord('c'):
        break
   #closing the camera 
cap.release()
cv2.destroyAllWindows()
