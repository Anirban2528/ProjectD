from tkinter import *
from pytube import YouTube
from pathlib import Path
root=Tk()
var=StringVar()
root.title('YouTube Video Downloader')
root.geometry("240x250")

def savevid():
  link=txt1.get()
  try:
    yob=YouTube(link)
    video=yob.streams.filter(res=var.get(),file_extension='mp4').first()
  except:
    lab2=Label(root,text="Invalid url or Bad Connection")
    lab2.pack()
    return
  
  try:
    video.download(str(Path.home()/'Downloads'))
  except:
    lab5=Label(root,text="Download Error!")
    lab5.pack()
    return
  lab6=Label(root,text="File Downloaded Successfully!")
  lab6.pack()

lab1=Label(root,text="Enter video url:")
lab1.pack()

txt1=Entry(root,width=30)
txt1.pack()

lab4=Label(root,text="Select resolution:")
lab4.pack()

R1=Radiobutton(root,text='360p',variable=var,value='360p',tristatevalue='360p')
R1.pack()
R2=Radiobutton(root,text='720p',variable=var,value='720p',tristatevalue='720p')
R2.pack()

btn1=Button(root,text='Download',command=savevid,bg='red',fg='white')
btn1.pack()

root.mainloop()