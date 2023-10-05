import cv2
import random
print("\t\t\tPHOTODETECTION ON IMAGE\n")
face_cascade= cv2.CascadeClassifier("C:/Users/user/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/Face.xml")
print(face_cascade)
img=cv2.imread("C:/Users/user/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/DSC_0479.JPG")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,4)
print(faces)
for (x,y,w,h) in faces:
    a=random.randint(0,255)
    b=random.randint(0,255)
    c=random.randint(0,255)
    cv2.rectangle(img,(x,y),(x+w,y+h),(a,b,c),2)
cv2.imshow('img',img)
cv2.waitKey()
print("\t\t\tLIVE WEB CAM PHOTODETECTION\n")
face_cascade= cv2.CascadeClassifier("G:\tkinter and face\dataset")
print(face_cascade)
cap=cv2.VideoCapture(0)
while True:
    img= cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,3)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(234,72,45),2)
    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()
print("\t\t\tPHOTODETECTION ON VIDEO\n")
face_cascade= cv2.CascadeClassifier("C:/Users/user/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/Face.xml")
print(face_cascade)
cap=cv2.VideoCapture("C:/Users/user/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/face_detection data/video2.mp4")
while True:
    _,img= cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,3)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(234,72,45),2)
    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()