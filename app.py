def musicurl():
    try:
        dd= filedialog.askopenfilename(initialdir="E:/Nitin/Mp3 Files",title="select audio",filetype=(("MP3","*.mp3"),("WAV","*.wav")))
    except:
        dd = filedialog.askopenfilename(  title="select audio",filetype=(("MP3", "*.mp3"), ("WAV", "*.wav")))
    audiotrack.set(dd)


def playmusic():
    ad=audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()
    audiostatuslabel.configure(text="playing......")
    progressbarlabel.grid()
    root.mutebutton.grid()
    progressbarvolumelabel.configure(text="{}%".format(int(mixer.music.get_volume()*100)))
    progressbarmusiclabel.grid()
    song=MP3(ad)
    TotalSongLength=int(song.info.length)
    ProgressbarMusic["maximum"]=TotalSongLength
    ProgressbarMusicEndTimeLabel.configure(text="{}".format(str(datetime.timedelta(seconds=TotalSongLength))))
    def musictick():
        CurrentSongLength = mixer.music.get_pos() // 1000
        ProgressbarMusicStartTimeLabel.configure(text="{}".format(str(datetime.timedelta(seconds=CurrentSongLength))))
        ProgressbarMusic["value"]=CurrentSongLength
        ProgressbarMusic.after(1,musictick)
    musictick()



def pausemusic():
    mixer.music.pause()
    root.pausebutton.grid_remove()
    root.resumebutton.grid()
    audiostatuslabel.configure(text="paused.....")

def stopmusic():
    mixer.music.stop()
    audiostatuslabel.configure(text="stopped.....")

def resumemusic():
    root.resumebutton.grid_remove()
    root.pausebutton.grid()
    mixer.music.unpause()
    audiostatuslabel.configure(text="playing.....")

def volumedown():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol-0.05)
    progressbarvolumelabel.configure(text="{}%".format(int(mixer.music.get_volume() * 100)))
    progressbarvolume["value"] = mixer.music.get_volume() * 100

def volumeup():
    root.mutebutton.grid()
    root.unmutebutton.grid_remove()
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol + 0.05)
    progressbarvolumelabel.configure(text="{}%".format(int(mixer.music.get_volume()*100)))
    progressbarvolume["value"]=mixer.music.get_volume()*100

def mutesound():
    global currentvol
    root.mutebutton.grid_remove()
    root.unmutebutton.grid()
    currentvol=mixer.music.get_volume()
    mixer.music.set_volume(0)

def unmutesound():
    global currentvol
    root.unmutebutton.grid_remove()
    root.mutebutton.grid()
    mixer.music.set_volume(currentvol)

def creatwidget():
    ####################################          image registeration
    global play,pause,stop,volup,voldown,search,resume,mute,unmute
    global audiostatuslabel,progressbarvolumelabel ,progressbarvolume,progressbarlabel,progressbarmusiclabel,ProgressbarMusic, ProgressbarMusicStartTimeLabel, ProgressbarMusicEndTimeLabel

    play=PhotoImage(file="play.png")
    pause = PhotoImage(file="pause-button.png")
    resume = PhotoImage(file="pause-button.png")
    search = PhotoImage(file="search.png")
    stop = PhotoImage(file="stop-button.png")
    voldown = PhotoImage(file="volume-down.png")
    volup = PhotoImage(file="volume-up.png")
    mute = PhotoImage(file="mute.png")
    unmute = PhotoImage(file="sound.png")

    #################################           photo resize
    play=play.subsample(20,20)
    pause = pause.subsample(20,20)
    resume = resume.subsample(20, 20)
    search =  search.subsample(20,20)
    stop = stop.subsample(20,20)
    voldown = voldown.subsample(20,20)
    volup = volup.subsample(20,20)
    mute = mute.subsample(20, 20)
    unmute = unmute.subsample(20, 20)

    #######################################################################################################  label
    tracklabel=Label(root,text="select audio track",font=("arial 15 italic bold"),fg="#3185FC",bg="#403F4C")
    tracklabel.grid(row=0,column=0,padx=20,pady=20)
    audiostatuslabel=Label(root,text="",font=("arial 15 italic bold"),width=20,bg="#403F4C" ,fg="#3185FC")
    audiostatuslabel.grid(row=2,column=1,padx=20,pady=20)

    ########################################################################################################  entrybox
    tracklabelentry=Entry(root,font=("arial 15 italic bold"),width=40,textvariable= audiotrack )
    tracklabelentry.grid(row=0,column=1,padx=20,pady=20)

    ###################################################################################################3       buttons
    browsebutton=Button(root,text="search",font=("arial 13 italic bold"),width=200,bd=5,bg="#EFBCD5",fg="white",activebackground="#3185FC",image=search,compound=RIGHT,command=musicurl)
    browsebutton.grid(row=0,column=2,padx=20,pady=20)

    playbutton = Button(root, text="play", font=("arial 13 italic bold"), width=200, bd=5,fg="white", bg="black",activebackground="#3185FC",image=play,compound=RIGHT,command=playmusic)
    playbutton.grid(row=1, column=0, padx=20, pady=20)

    root.pausebutton = Button(root, text="pause", font=("arial 13 italic bold"), width=200, bd=5, fg="white",bg="black",
                          activebackground="#3185FC",image=pause,compound=RIGHT,command=pausemusic)
    root.pausebutton.grid(row=1, column=1, padx=20, pady=20)

    root.resumebutton= Button(root,text="resume",font=("arial 13 italic bold "),width=200, bd=5,fg="white",bg="black",activebackground="#3185FC",image=resume,compound=RIGHT,command=resumemusic)
    root.resumebutton.grid(row=1,column=1,padx=20,pady=20)
    root.resumebutton.grid_remove()

    volumeupbutton = Button(root, text="volumeup", font=("arial 13 italic bold"), fg="white",width=200, bd=5, bg="black",
                          activebackground="#3185FC",image=volup,compound=RIGHT,command=volumeup)
    volumeupbutton.grid(row=1, column=2, padx=20, pady=20)

    volumedownbutton = Button(root, text="volumedown", font=("arial 13 italic bold"),fg="white", width=200, bd=5, bg="black",
                          activebackground="#3185FC",image=voldown,compound=RIGHT,command=volumedown)
    volumedownbutton.grid(row=2, column=2, padx=20, pady=20)

    stopbutton = Button(root, text="stop", font=("arial 13 italic bold"), fg="white",width=200, bd=5, bg="black",
                          activebackground="#3185FC",image=stop,compound=RIGHT,command=stopmusic)
    stopbutton.grid(row=2, column=0, padx=20, pady=20)

    root.mutebutton = Button(root, text="mute", font=("arial 13 italic bold"),fg="white", width=100, bd=5, bg="black",
                               activebackground="#3185FC", image=mute, compound=RIGHT, command=mutesound)
    root.mutebutton.grid(row=3, column=3, padx=20, pady=20)
    root.mutebutton.grid_remove()

    root.unmutebutton = Button(root, text="unmute", font=("arial 13 italic bold"), fg="white",width=100, bd=5, bg="black",
                             activebackground="#3185FC", image=unmute, compound=RIGHT, command=unmutesound)
    root.unmutebutton.grid(row=3, column=3, padx=20, pady=20)
    root.unmutebutton.grid_remove()

    #######################################################   progress volume bar
    progressbarlabel=Label(root,text="",bg="red")
    progressbarlabel.grid(row=0,column=3,rowspan=3)
    progressbarlabel.grid_remove()

    progressbarvolume=Progressbar(progressbarlabel,mode="determinate",value=pvalue,orient=VERTICAL,length=190)
    progressbarvolume.grid(row=0,column=0,ipadx=5)

    progressbarvolumelabel = Label(progressbarlabel, bg="light grey", text="0%", width=3)
    progressbarvolumelabel.grid(row=0, column=0)

    ###################################################################################################      progressmusic bar
    progressbarmusiclabel=Label(root,text="",bg="red")
    progressbarmusiclabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
    progressbarmusiclabel.grid_remove()

    ProgressbarMusicStartTimeLabel=Label(progressbarmusiclabel,bg="red",text="00:00:00",width=6)
    ProgressbarMusicStartTimeLabel.grid(row=0,column=0)

    ProgressbarMusic=Progressbar(progressbarmusiclabel,mode="determinate",orient=HORIZONTAL,value=0)
    ProgressbarMusic.grid(row=0,column=1,ipadx=380,ipady=3)

    ProgressbarMusicEndTimeLabel=Label(progressbarmusiclabel,text="",bg="red")
    ProgressbarMusicEndTimeLabel.grid(row=0,column=2)


from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3

root=Tk()
root.title("music player")
root.geometry("1150x500+100+50")
root.iconbitmap("music.ico")
root.configure(bg="#403F4C")
root.resizable(False,False)
mixer.init()
###########################################  global variable
audiotrack = StringVar()
currentvol=0
TotalSongLength=0
pvalue=mixer.music.get_volume()*100

#####################################################
creatwidget()

################################################################# slider
count=0
text=""
ss="Developed by Pooja Rai"
sliderlabel=Label(root,text="",bg="#403F4C",font=("arial 25 italic bold"),fg="#3185FC")
sliderlabel.grid(row=4,column=0,columnspan=3,padx=20,pady=20)
def slider():
    global count,text
    if (len(text)>=len(ss)):
        count=-1
        text=""
        sliderlabel.configure(text=text)
    else:
        text=text+ss[count]
        sliderlabel.configure(text=text)
    count+=1
    sliderlabel.after(200,slider)
slider()
root.mainloop()
