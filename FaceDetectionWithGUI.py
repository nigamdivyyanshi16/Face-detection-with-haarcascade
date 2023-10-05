import tkinter as tk
import numpy as np
# numpy is needed bcoz The computer processes images in the form of a matrix for which NumPy is used and  OpenCV uses it in the background
from tkinter import messagebox as mess
import pandas as pd
from tkinter import ttk
import tkinter.simpledialog as tsd
# import PIL as Image
import PIL.Image
import csv
import cv2
import datetime
import time
import random
import os


# 1.Face Detection and Data Gathering
# 2.Train the Recognizer
# 3. Face Recognition


def checkFileExistence(filepath):
    dir = os.path.dirname(filepath)
    if not os.path.exists(dir):
        os.makedirs(dir)

#################################################################


def savePassword():
    checkFileExistence("TrainingImageFolder/")
    existpsswrd = os.path.exists("TrainingImageFolder/password.txt")
    if existpsswrd:
        readpssd = open("TrainingImageFolder/password.txt", "r")
        key = readpssd.read()

    else:
        new_pass = tsd.askstring(
            "Not found old password", "Enter a new pssword", show="*")
        if new_pass == None:
            mess._show(title="NO Password",
                       message="Password not set!Try again")
        else:
            tf = open("TrainingImageFolder/password.txt", "w")
            tf.write(new_pass)
            mess._show(title="Successfull",
                       message="Password saved successfully!")
            return
    enterpsswrd = tsd.askstring("Password", "Enter your password", show="*")
    if enterpsswrd == key:
        TrainImage()
    elif enterpsswrd == None:
        pass
    else:
        mess._show(title="Wrong password",
                   message="Entered the wrong passowrd")

#######################################################


def TrainImage():
    check_haarcascadefile()
    checkFileExistence("TrainingImageFolder/")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    harcascadePath = "Face.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("TrainingAlgoImages")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='No Registrations',
                   message='Please Register someone first!!!')
        return
    recognizer.save("TrainingImageFolder\Imagetrainer.yml")
    res = "Profile Saved Successfully"
    message.configure(text=res)


##################################################
def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = PIL.Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')  # imageNp is a array
        # getting the Id from the image
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # os.path.split() method in Python is used to Split the path name into a pair head and tail. Here, tail is the last path name component and head is everything leading up to that
        # In ID, you will get 1,2,3, and so on till the number of pictures present in the folder.


        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids


#####################################################

def check_haarcascadefile():
    exists = os.path.isfile("Face.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing',
                   message='Please contact us for help')
        window.destroy()

#########################################################################


def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', 'ID', 'NAME', 'COURSE']
    checkFileExistence("YourInfo/")
    checkFileExistence("TrainingAlgoImages/")
    serial = 0
    exists = os.path.isfile("YourInfo/YourInfoDetails.csv")
    if exists:
        with open("YourInfo/YourInfoDetails.csv", "r") as csvFile1:
            reader = csv.reader(csvFile1)
            for row in reader:
                serial += 1
            # serial = (serial//2)
            csvFile1.close()
    else:
        with open("YourInfo/YourInfoDetails.csv", "a+") as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)  # writing the columns name
            serial = 1
        csvFile1.close()
    Id = (txt.get())
    name = (txt2.get())
    course = (txt3.get())
    # here we are checking wheher the name is valid or not.
    if name.isalpha() or ' ' in name:
        cam = cv2.VideoCapture(0)  # This is used for reading the video
        # cv2.VideoWriter(): write to a video
        harcascadePath = "Face.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        # ued in saving the image file and for braking the while loop.
        SampleNum = 0
        # using while loop bcoz we want to capture all frames not a single frame in that time.
        while(True):
            # read video, it returns the object (img) which we can use to display the that video.
            success, img = cam.read()

            # converting it into grayscale:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # returns the coordinates of the faces detected in the form of nested list.
            faces = detector.detectMultiScale(gray)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (random.randint(34, 200),
                              random.randint(56, 228), random.randint(90, 234)), 3)
                SampleNum += 1  # incrementing sampleNum
                # writing that images to dataset :
                cv2.imwrite("TrainingAlgoImages\\"+name+"."+str(serial) +
                            "."+Id+"."+str(SampleNum)+".jpg", gray[y:y + h, x:x + w])
                # displaying the frame
                cv2.imshow("Taking Images", img)
            # wait for 100ms:
            # if cv2.waitKey(100) and 0xFF== ord('q'):
            #     break
            if cv2.waitKey(1) == ord('q'):
                break
            elif SampleNum > 100:
                break
        cam.release()
        # destroy all windows, it doesn't accept and doesn't return anything.
        cv2.destroyAllWindows()
        row = [serial, Id, name, course]
        with open("YourInfo/YourInfoDetails.csv", "a") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
    else:
        if not name.isalpha():
            res = "Enter the correct name"
            message.configure(text=res)


################################


def TrackImage():
    check_haarcascadefile()
    checkFileExistence("YourInfo/")
    i = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    exist3 = os.path.isfile("TrainingImageFolder/ImageTrainer.yml")
    if exist3:
        recognizer.read("TrainingImageFolder/ImageTrainer.yml")
    else:
        mess._show(title="Data Missing",
                   message="click save profile to reset data")
        return
    harcascadePath = "Face.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # Some of font types are FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN etc. in cv2.
    exist1 = os.path.isfile("YourInfo/YourInfoDetails.csv")
    if exist1:
        df = pd.read_csv("YourInfo/YourInfoDetails.csv")
        # pd.read_csv(filepath as string, separator(by default (,)) is used to read csv files.
        # Above function will return the DataFrame(it is like a 2D array).
    else:
        mess._show(title="Missing Details", message="some details are missing")
        cam.release()  # close the video file or capturing device
        cv2.destroyAllWindows()  # close all the GUI opened
        window.destroy()
    
    while True:  # using for capturing all the frames of video through webcam.
        ret, image = cam.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (random.randint(34, 200),
                          random.randint(56, 228), random.randint(90, 234)), 3)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if conf < 50:
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                # # in aa, it will return the NAME where serial no. is equal to serial.

                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                ID = str(ID)
                bb = ""
                # converting the name to string from list:
                for k in aa:
                    bb+=k
            else:
                aa = "Unknown"
                bb = str(aa)
            cv2.putText(image, str(bb), (x, y + h), font, 2, (random.randint(0,
                        240), random.randint(0, 140), random.randint(120, 245)), 2)
            cv2.imshow("Recognizing Face", image)
        if cv2.waitKey(0) == ord('q'):
            break
    # deleting the previous records if
    for item in tv.get_children():
        tv.delete(item)
    # Inserting details into treeview:
    with open("YourInfo/YourInfoDetails.csv", "r") as csvFile1:
        # reads every row and put it in a list of string
        reader1 = csv.reader(csvFile1)
        for row in reader1:
            # we do this bcoz we want to read rows from second line not the first one in which column are present.
            i = i+1
            if i > 1:
                if i % 2 == 0:
                    iidd = str(row[0]) + '   '
                    tv.insert('', 0, text=iidd, values=(
                        row[1], row[2], row[3]))

    csvFile1.close()
    
    cam.release()
    

    cv2.destroyAllWindows()

##################### GUI Front End ###############################
window = tk.Tk()
window.geometry("1280x720")
window.resizable(True, False)
window.title("Face Detection&Recognition")
window.configure(background='#262523')

frame1 = tk.Frame(window, bg="#00aeff")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#00aeff")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="Face Recognition And Detection System",
                    fg="white", bg="#262526", width=55, height=1, font=('times', 29, ' bold '))
message3.place(x=10, y=10)

frame3 = tk.Frame(window, bg="#c4c6ce")


head2 = tk.Label(frame2, text="                       For New Registrations                       ",
                 fg="black", bg="#03F2FA", font=('times', 17, ' bold '))
head2.grid(row=0, column=0)

head1 = tk.Label(frame1, text="                       For Already Registered                       ",
                 fg="black", bg="#03F2FA", font=('times', 17, ' bold '))
head1.place(x=0, y=0)

lbl = tk.Label(frame2, text="Enter ID", width=20, height=1,
               fg="black", bg="#00aeff", font=('times', 17, ' bold '))
lbl.place(x=80, y=55)

txt = tk.Entry(frame2, width=32, fg="black", font=('times', 15, ' bold '))
txt.place(x=30, y=88)

lbl2 = tk.Label(frame2, text="Enter Name", width=20, fg="black",
                bg="#00aeff", font=('times', 17, ' bold '))
lbl2.place(x=80, y=140)

txt2 = tk.Entry(frame2, width=32, fg="black", font=('times', 15, ' bold '))
txt2.place(x=30, y=173)

lbl3 = tk.Label(frame2, text="Enter Course", width=20, height=1,
                fg="black", bg="#00aeff", font=('times', 17, ' bold '))
lbl3.place(x=80, y=235)

txt3 = tk.Entry(frame2, width=32, fg="black", font=('times', 15, ' bold '))
txt3.place(x=30, y=264)

message = tk.Label(frame2, text="", bg="#00aeff", fg="black", width=39,
                   height=1, activebackground="yellow", font=('times', 16, ' bold '))
message.place(x=7, y=450)

lbl3 = tk.Label(frame1, text="CheckInfo", width=20, fg="black",
                bg="#00aeff", height=1, font=('times', 17, ' bold '))
lbl3.place(x=100, y=115)

takeImg = tk.Button(frame2, text="Take Images", command=TakeImages, fg="black", bg="#F5FD03",width=34, height=1, activebackground="white", font=('times', 15, ' bold '))
takeImg.place(x=30, y=310)

trainImg = tk.Button(frame2, text="Save Profile", command=savePassword,  fg="black",bg="#F5FD03", width=34, height=1, activebackground="white", font=('times', 15, ' bold '))
trainImg.place(x=30, y=390)

trackImg = tk.Button(frame1, text="Check Details", command=TrackImage, fg="black",
bg="#1AFD03", width=35, height=1, activebackground="white", font=('times', 15, ' bold '))
trackImg.place(x=30, y=50)

#######################TreeView for showing details##############################

tv = ttk.Treeview(frame1, height=13, columns=("ID","Name", "Course"))
# giving width to columns
tv.column('#0', width=40)
tv.column('ID',width=150)
tv.column("Name", width=150)
tv.column("Course", width=150)
tv.grid(row=2, column=0, padx=(0, 0), pady=(150, 0), columnspan=4)
# giving the column name
tv.heading("#0", text="S.NO")
tv.heading("ID",text="ID")
tv.heading("Name", text="NAME")
tv.heading("Course", text="COURSE")

################ Scroll bar in treeview#######################
scroll = ttk.Scrollbar(frame1, orient='vertical', command=tv.yview)
scroll.grid(row=2, column=4, padx=(0, 100), pady=(150, 0), sticky='ns')
tv.configure(yscrollcommand=scroll.set)


window.mainloop()

#####################################

global key
key = ''
