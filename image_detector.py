import cv2
face_cascade=cv2.CascadeClassifier("C:/Users/DELL/AppData/Local/Programs/Python/Python310/Lib/site-packages/tk/Face.xml")
img=cv2.imread("G://tkinter and face//dataset//Snapchat-1805703730.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,4)
print(faces)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow("img",img)
cv2.waitKey() 