# Import the required libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import numpy as np
import os
# Create an instance of tkinter frame
win= Tk()
f = Frame(win,height=400,width=500,bg='yellow',cursor='cross')
f.pack()

# Set the size of the tkinter window
win.title('Live Face Recognition by Divyanshi Nigam')
win.geometry("700x350")
L1 = Label(win, text="Enter user Name")
L1.pack( side = LEFT)

E1 = Entry(win, bd =4)
E1.pack(side = LEFT)


blackbutton = Button(f, text="FACE RECOGNITION", fg="black")
blackbutton.pack( side = LEFT )

# Define a function to show the popup message
def show_msg():
   messagebox.showinfo("Message","Hey There! I hope you are doing well.")
   


# Add an optional Label widget and pack is used for This geometry manager organizes widgets in blocks before placing them in the parent widget.
Label(win, text= "Welcome Folks!", fg='blue',font= ('Aerial 30 bold italic')).pack(pady= 45)

#The Label widget is used to provide a single-line caption for other widgets. It can also contain images.
# Create a Button to display the message
b=Button(win, text= "Click Here",width=15,height=2,activebackground='green',activeforeground='white', command=show_msg).pack(pady= 3)
b=Button(f,fg='red')
b.pack()
win.mainloop()