#we are installing opencv python
#now,haarcascade
import cv2
import numpy as np
#just open the webcam
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("G:\tkinter and face\haarcascade_frontal_face_alt.xml")
skip=0
#array this is a list where we have stored our data
face_data=[]
dataset_path="G:\tkinter and face\dataset"
file_name=input("enter the name of the person")
while True:
    #ret is basically boolean variable checks camera is open or not
    #frame defines the camera
    ret,frame=cap.read()
    #initally image will b  color image i.e rgb(bgr) and we are converting to gray image
    #cv2.Color(frame(camera feed),and then rgb to gray)
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #if camera is not working then 
    if ret==False:
        continue
    #we just created gray frame so parameters are framename,scaling factor,k(no.of neighbors)
    #it returns the coordinates of face wherein faces is the list
    #multiscale returns coordinates of the rectangle on the face with x,y top left and w as width and h as height of the rectangle box enclosed

    faces=face_cascade.detectMultiScale(gray_frame,1.3,5)
    if len(faces)==0:
        continue
    k=1
    #if you have multiple no. of face in frame so we are sorting the faces
    #here we are passing the faces list of array faces=[x,y,w,h]=[0,1,2,3]
    #area=width*h
    #area=faces[2]*face[3]
    #image with larger area will come first in descending and vice versa
    #lambda function shows the faces
    #x[2]*x[3] ar area of image
    #reverse =true means descending order
    faces=sorted(faces,key=lambda:x[2]*x[3],reverse=True)
    #when we start recording face
    #after every second faces will be reocrd
    #so when we reach 10th second we will calculate evry 10th second face 
    #we will store it  
    skip+=1
    #iterate every face till end [:1]
    for face in faces[:1]:
        #coordinates of every face will come in face
        x,y,w,h=face
        #offet is padding the space/gap
        #padding is gap between face rectangle and outerbox is 5
        #here we are extracting the section of paper so we are subtracting the padding/offset
        #and calculating particulare section of paper
        offset=5
        face_offset=frame[y-offset:y+offset,x-offset:x+w+offset]
        #resizing the face to 100*100
        face_selection=cv2.resize(face_offset,(100,100))
        #here,after every 10th face ,  will be recording each 10th face  into array so that we dont have many faces in array at the same time good feeded face  
        if skip%10==0:
            face_data.append(face_selection)
            print(len(face_data))
        cv2.imshow(str(k),face_selection)
        k+=1
        #creating a rectangle around the face
        #rgb=255,0,0 so red is given 255
        #a red color box will appear

        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("faces",frame)
    key_pressed=cv2.waitkey(1) & 0xFF
    if key_pressed==ord('q'):
        break
    #now we need to implement KNN 
    #for this we need numpy data
    #so we converting our list of faces to numpy by np.array also for faster 
    face_data=np.array(face_data)
    face_data=face_data.reshape((face_data.shape[0],-1))
    #printing the shape of face rightnow
    print(face_data.shape)
    np.save(dataset_path+file_name,face_data)
    #we are saving data in folder and displaying path
    
    print("Dataset saved at: {}".format(dataset_path+file_name+'.npy'))
    #releasing the camera
    cap.release()
    #destroying all the windows
    cv2.destroyAllWindows()