#Cassandra Delieto
#Python vs. 3.6 using sublime text editor
#1/30/17

from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askdirectory
import GUI_db, Drill3
import time, datetime, os, shutil, sqlite3

class ParentWindow:

    def __init__(self, master): 
        
        master.title('Move Your modified files < than 24 hrs old')
        master.minsize(700,200)
        master.configure(bg="#F0F0F0")
        master.resizable(width=False, height=False) 
        #dimensions of window

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        ttk.Label(self.frame_header, wraplength=2000,
                  text = ("Select source and destination folders to move files that have been modified in the last 24 hours.")).pack(pady=15)    
                                                 
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Button(self.frame_content, text='Original Folder', command= lambda: self.Source()).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(self.frame_content, text='Destination Folder', command= lambda: self.Dest()).grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(self.frame_content, text='Press to locate Files', command= lambda: Drill3.transfer(self)).grid(row=2, column=2, padx=10, pady=20)
        #this last tkk.Button is where we imported the last exercise^

        ttk.Label(self.frame_content).grid(row=0, column=1, padx=10, pady=3)
        self.src_var = StringVar()
        self.entry_src = ttk.Entry(self.frame_content, width=60, textvariable=self.src_var)
        self.entry_src.grid(row=0, column=2, padx=10, pady=3,sticky=N+W)
        self.entry_src.configure(state='readonly')
        
        ttk.Label(self.frame_content).grid(row=1, column=1, padx=10, pady=3)
        self.dst_var = StringVar()
        self.entry_dst = ttk.Entry(self.frame_content, width=60, textvariable=self.dst_var)
        self.entry_dst.grid(row=1, column=2, padx=10, pady=3,sticky=N+W)
        self.entry_dst.configure(state='readonly')

        #Label for the last time the file-check was done
        ttk.Label(self.frame_content, text="Last time file-check was performed ").grid(row=4, column=2, padx=10, pady=3)
        self.lr_var = StringVar()
        self.lr_var.set("The file transfer drill has not been run!")
        self.entry_lr = ttk.Entry(self.frame_content, width=60, textvariable=self.lr_var)
        self.entry_lr.grid(row=3, column=2, padx=10, pady=3,sticky=N+W)
        self.entry_lr.configure(state='readonly')

#Call the database and fufill the conditions stated for the time constraint. Print last file check. 
        GUI_db.create_db(self)

#Open up the folders
    def Source(self):
        src_dirname = askdirectory()
        self.src_var.set(src_dirname + "/")

    def Dest(self):
        dst_dirname = askdirectory()
        self.dst_var.set(dst_dirname + "/")

if __name__ == "__main__": 
    root = Tk()
    App = ParentWindow(root) 
    root.mainloop()

