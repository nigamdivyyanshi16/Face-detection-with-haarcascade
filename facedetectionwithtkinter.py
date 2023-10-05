
from tkinter import *
#python image library


root=Tk()
root.title("LIVE FACE DETECTION")
root.geometry('700x540')
#a black background 
root.configure(bg='black')
Label(root,text="Divyanshi live cam",font=("times new roman",30,"bold"),bg="black",fg="red").pack()
f1=LabelFrame(root,bg='red')
f1.pack()
#to get the image inside the frame 
L1=Label(f1,bg='white')
L1.pack()

Button(root,text='CAPTURE',font=('Aerial 30 bold italic'),bg="black",fg="yellow").pack(fill=X,expand=True)

#whether our  camera is working or not
#open the webcam
   
   #if camera is reading image then continue for infinte time till q is pressed
    
        
        #closing the camera
root.update()
        
root.mainloop()
             
        