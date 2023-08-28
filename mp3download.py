#======================
# imports
#======================
from tkinter import *
from pytube import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import subprocess, sys, os
from os.path import join as pjoin
from subprocess import PIPE, run
from tkinter import messagebox

#set the window and lable frames

class Fxg(Tk):
    def __init__(self):
        super(Fxg, self).__init__()
        
        self.title("YT MP3 downloader")
        self.minsize(100, 50)

        self.labelFrame = ttk.LabelFrame(self, text = "FFMPEG").grid(column = 0, row = 1)
        #self.labelFrame.grid(column = 0, row = 1)

        
        self.buttonstart()
        self.buttonquit()
        self.url()
        self.vidname()
    
    
        
#set the suttons
        
    def  buttonstart(self):

        self.bstart = ttk.Button(width = 16,text = "Start",command = self.run).grid(column = 1, row = 5)
        #self.bstart.grid(column = 1, row = 5)
        
    def buttonquit(self):
        self.bquit = ttk.Button(width = 16,text = "Quit",command = self.quit).grid(column = 1, row = 6)
        #self.bquit.grid(column = 1, row = 6)

    def  url(self):

        self.urlentry = ttk.Entry (width = 50)#.grid(column = 2, row = 1)
        self.urlentry.grid(column = 2, row = 1)
    

        self.urlname = ttk.Label(width= 15, text = "Enter URL") #grid(column = 1, row = 1)
        self.urlname.grid(column = 1, row = 1)
        
        
    def  vidname(self):

        self.vidnameb = ttk.Entry (width = 50)#.grid(column = 2, row = 3)
        self.vidnameb.grid(column = 2, row = 3)

        self.vidnamel =  ttk.Label(width= 15, text = "Enter Name")#.grid(column = 1, row = 3)
        self.vidnamel.grid(column = 1, row = 3)


    def  run(self):
        
        folder_selected = filedialog.askdirectory()
        
        self.progress = Progressbar(orient=HORIZONTAL,length=100,  mode='indeterminate')
        self.progress.grid( column = 2, row = 5)
        self.update_idletasks()
        self.progress['value'] += 30
        
        sufx = self.urlentry.get()
        newname = self.vidnameb.get()
        yt = YouTube(sufx)
        name = (newname)
        
        self.update_idletasks()
        self.progress['value'] += 30
        
        yt.streams.filter(mime_type="audio")
        a = yt.streams.get_audio_only()

        self.update_idletasks()
        self.progress['value'] += 30
        
        a.download(folder_selected, filename = name+".mp3")
        
        self.progress.destroy() # get rid of the progress bar
        tk.messagebox.showinfo('Completed(YT MP3 downloader)','Download Complated') # pop up a done messgae
        
        

    def quit(self):

        os._exit(1)

        




fxg = Fxg()
fxg.mainloop()
