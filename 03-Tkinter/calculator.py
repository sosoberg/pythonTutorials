from tkinter import *

# needs to happen before anything else in Tkinter
root = Tk()

# creating a label widget
myLabel = Label(root, text="Hello World")
myLabel2 = Label(root, text="My Name is Sam Oberg")

myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

def myClick():
    myLabel3 = Label(root, text="Look! I clicked")
    myLabel3.grid(row=2, column=0)


myButton = Button(root, text="Click Me", padx=11, pady=7, command=myClick)

myButton.grid(row=2, column=0)

root.mainloop()