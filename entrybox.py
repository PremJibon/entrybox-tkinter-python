from tkinter import *

def submit():
    user_name = entry.get()
    label = Label(root,text="Hello "+entry.get())
    label.pack()
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)
    entry.config(state=EXTENDED)
   
def backspace():
    entry.delete(len(entry.get())-1,END)

root = Tk()
entry = Entry(root,show='@',font=('Arial',50),fg="green",bg='black')
entry.insert(0,"Spongbob")
entry.pack(side=LEFT)

submit_button = Button(root,text='submit',command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(root,text='delete',command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(root,text="backspace",command=backspace)
backspace_button.pack(side=RIGHT)


root.mainloop()