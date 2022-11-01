#ebic download manager
from tkinter import *
from tkinter import messagebox, filedialog
import os

dm = Tk()
dm.iconbitmap("302472257_480x360.ico")
url = StringVar()
def sex():
    return False

#widget geometry

dm.geometry("450x400")
dm.title("sexy download manager")
dm.resizable(False, False)

#top wrapper properties

wrap = LabelFrame(dm, text="url sex")
wrap.pack(fill="both", expand="yes", padx=10, pady=10)

labl = Label(wrap, text="url")
labl.grid(row=0, column=0, padx=10, pady=10)

txtinp = Entry(wrap, textvariable=url)
txtinp.grid(row=0, column=2, padx=5, pady=10)

click = Button(wrap, text="sex", command=sex)
click.grid(row=0, column=4, padx=10, pady=10)

#bottom wrapper properties

wrap_b = LabelFrame(dm, text="download uwu")
wrap_b.pack(fill="both", expand="yes", padx=10, pady=10)

label_b = Label(wrap_b, text="file rollin")
label_b.grid(row=0, column=2, padx=10, pady=10)

dm.mainloop()
