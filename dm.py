#ebic download manager
from tkinter import *
from tkinter import messagebox, filedialog
import os

#what the fuck

dm = Tk()
dm.iconbitmap("302472257_480x360.ico")
dm.geometry("450x400")
dm.title("sexy download manager")
dm.resizable(False, False)

#teh string variables

url = StringVar()
filename = "poopy"
brogress = "buttholes"
percemtage = "poopoo"

#teh functions

def sex():
    return False
def bye():
    return True

#horseshit

wrap = LabelFrame(dm, text="url sex")
wrap.pack(fill="both", expand="yes", padx=10, pady=10)

label = Label(wrap, text="url")
label.grid(row=0, column=0, padx=10, pady=10)

txtinp = Entry(wrap, textvariable=url)
txtinp.grid(row=0, column=2, padx=5, pady=10)

click = Button(wrap, text="sex download", command=sex)
click.grid(row=0, column=4, padx=10, pady=10)

#more horseshit

wrap2 = LabelFrame(dm, text="download uwu")
wrap2.pack(fill="both", expand="yes", padx=10, pady=10)

label2 = Label(wrap2, text="file rollin")
label2.grid(row=0, column=0, padx=10, pady=10)

label3 = Label(wrap2, textvariable=filename)
label3.grid(row=0, column=1, padx=10, pady=10)

label4 = Label(wrap2, text="brogress")
label4.grid(row=1, column=0, padx=10, pady=10)

label5 = Label(wrap2, textvariable=brogress)
label5.grid(row=1, column=1, padx=10, pady=10)

label6 = Label(wrap2, text="percemtage")
label6.grid(row=2, column=0, padx=10, pady=10)

label7 = Label(wrap2, textvariable=percemtage)
label7.grid(row=2, column=1, padx=10,pady=10)

exit = Button(wrap2, text="BYE", command=bye)
exit.grid(row=3, column=0, padx=10, pady=10)

dm.mainloop()
