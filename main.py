from tkinter import *
from pytube import YouTube


root = Tk()
link = StringVar()
root.geometry('400x400')
root.title('YouTube Downloader')
labelframe = Frame(root)
buttonframe = Frame(root)
labelframe.pack(side=TOP, fill=X)
buttonframe.pack(side=BOTTOM, fill=X)
Label(labelframe, text='Paste link here:', font='Arial 20').pack(side=TOP)
linkfield = Entry(labelframe, textvariable=link).pack(side=TOP, fill=X)
messege = StringVar()
messege.set('')
resoultlabel = Label(labelframe, textvariable=messege, font='Arial 15').pack(side=BOTTOM, fill=X)

def download():

    try:
        url = YouTube(str(link.get()))
        video = url.streams.first()
        messege.set('Downloading')
        video.download()
        messege.set('Downloaded')
    except:
        messege.set('Something gone wrong\ncheck the correctness:\n*link')

Button(buttonframe, text='Download', font='Arial 14', command=download).pack(fill=X)

root.mainloop()