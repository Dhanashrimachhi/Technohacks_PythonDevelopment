from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root=Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#120E1C")
root.resizable(False,False)

mixer.init()

# Create a function to open a file
def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)


def playMusic():
    Music_Name = playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()


#icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

Top=PhotoImage(file="10.png")
Label(root,image=Top,bg="#0f1a2b").pack()

#button
play_button=PhotoImage(file="play.png")
Button(root, image=play_button,bg="#120E1C",bd=0,command=playMusic).place(x=100,y=400)

stop_button=PhotoImage(file="stop.png")
Button(root, image=stop_button,bg="#120E1C",bd=0,command=mixer.music.stop).place(x=30,y=500)

resume_button=PhotoImage(file="resume.png")
Button(root, image=resume_button,bg="#120E1C",bd=0,command=mixer.music.unpause).place(x=115,y=500)

pause_button=PhotoImage(file="pause.png")
Button(root, image=pause_button,bg="#120E1C",bd=0,command=mixer.music.pause).place(x=200,y=500)

#music
Menu=PhotoImage(file="menu.png")
Label(root, image=Menu,bg="#120E1C").pack(padx=10,pady=50,side=RIGHT)

music_frame= Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=330,y=350,width=560,height=200)

Button(root,text="Open Folder",width=15,height=2,font=("arial",10,"bold"),fg="white",bg="#21b3de",command=AddMusic).place(x=330,y=300)

scroll = Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,font=("arial", 14),bg="#313131",fg="grey",selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT,fill=BOTH)

root.mainloop()