from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('300x200')
root.title("prime number ")
root.config(bg="yellow")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
         if n %i ==0:
              return False
    return True

def action():
        number = int(entry.get())
        if is_prime(number):
            messagebox.showinfo('Prime Number', f'{number} is a prime number')
        else:
            messagebox.showwarning('Not Prime Number', f'{number} is not a prime number')
    

msg = Label(root, text='Enter a number')
msg.grid(row=0, column=0, padx=10, pady=10)

entry = Entry(root)
entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

button1 = Button(root, text="Check Prime", command=action)
button1.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
