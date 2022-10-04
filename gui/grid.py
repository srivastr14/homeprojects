from tkinter import *

root = Tk()

# Creating Label widget
myLabel1 = Label(root, text='Hey... Hey.. HEY...')
myLabel2 = Label(root, text='I love you')

# Remember, the grid is all relative
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)

root.mainloop()

