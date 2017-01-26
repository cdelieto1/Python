from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

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
                  text = ("Select source and destination folders. Then 'Move Files' that have been modified in the last 24 hours.")).pack(pady=15)    
        #dimensions of header + content
                                                 
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Button(self.frame_content, text='Original Folder', command= lambda: self.Source()).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(self.frame_content, text='Destination Folder', command= lambda: self.Dest()).grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(self.frame_content, text='Files within 24 hrs', command= lambda: Drill3.transfer("/Users/Mac/Desktop/Original/","/Users/Mac/Desktop/Destination/")).grid(row=2, column=0, padx=10, pady=20)
        #this last tkk.Button is where we imported the last exercise^

        ttk.Label(self.frame_content, text="Original Folder").grid(row=0, column=1, padx=10, pady=3)
        self.src_var = StringVar()
        self.entry_src = ttk.Entry(self.frame_content, width=60, textvariable=self.src_var)
        self.entry_src.grid(row=0, column=2, padx=10, pady=3)
        self.entry_src.configure(state='readonly')
        
        ttk.Label(self.frame_content, text="Destination Folder").grid(row=1, column=1, padx=10, pady=3)
        self.dst_var = StringVar()
        self.entry_dst = ttk.Entry(self.frame_content, width=60, textvariable=self.dst_var)
        self.entry_dst.grid(row=1, column=2, padx=10, pady=3)
        self.entry_dst.configure(state='readonly')

        #Drill5.create_db(self)
        #content dimensions + content + input fields for the labels

    def Source(self):
        src_dirname = askopenfilename()
        self.src_var.set(src_dirname+'/')

    def Dest(self):
        dst_dirname = askopenfilename()
        self.dst_var.set(dst_dirname+'/')

if __name__ == "__main__": 
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
