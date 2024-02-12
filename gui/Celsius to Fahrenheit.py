from tkinter import *
from tkinter import messagebox
root=Tk()
def action():
    cel=int(entry1.get())
    feh=(cel*(9/5))+32
    messagebox.showinfo('temp in Fahrenheit is',f'{feh}')

label1 = Label(root,text="Celsius to Fahrenheit")
label1.grid(row=0,column=5)

entry1 =Entry(root)
entry1.grid(row=3,column=5)

button1 = Button(root,text="convert to fahrenheit",command=action)
button1.grid(row=6,column=5)

root.mainloop()
