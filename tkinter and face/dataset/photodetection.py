import cv2
import random
print("\t\t\tPHOTODETECTION ON IMAGE\n")
face_cascade= cv2.CascadeClassifier("C:/Users/user/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/Face.xml")
print(face_cascade)
cap=cv2.VideoCapture(0)
while True:
    ret,frame= cap.read()
    col=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.imread("C:/Users/user/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/DSC_0479.JPG")
    col=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(col,1.1,4)
    print(faces)
    for (x,y,w,h) in faces:
        a=random.randint(0,255)
        b=random.randint(0,255)
        c=random.randint(0,255)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(a,b,c),2)
    cv2.waitKey()
    if ret==False:
        continue
    #if camera is reading then
    cv2.imshow("LIVE VIDEO FACE RECOGNITION",frame)
    #if currrently pressed key matches with this or not
    key_pressed=cv2.waitKey(1) & 0xFF
    #if q will be entered then only camera will be closed
    if key_pressed==ord('c'):
        break
cv2.waitKey()
cap.release()
cv2.destroyAllWindows()