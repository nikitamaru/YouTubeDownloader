import youtube_dl
from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Easy Downloader")


def down():
    try:
        video=e1_value.get()
        yy=youtube_dl.YoutubeDL()
        yy.download([video])
    except Exception as e:
        messagebox.showinfo("Error!", "Enter Valid url")



lab=Label( window, text="YOUTUBE DOWNLOADER", relief=RAISED ,justify=CENTER)
lab.grid(row=0,columnspan=2)

lab2=Label(window,text="Enter Url:")
lab2.grid(row=1,column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=1,column=1)

b1=Button(window,text="download",command=down)
b1.grid(row=2,columnspan=2)




window.mainloop()
