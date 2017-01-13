'''Scenario: Your employer wants a program to move all his .txt files from one folder to another
with the click of a click of a button. On your desktop make 2 new folders. Call one Folder A &
the second Folder B. Create 4 random .txt files & put them in Folder A.
Plan:
- Move the files from Folder A to Folder B.
- Print out each file path that got moved onto the shell.
- Upon viewing Folder A after the execution, the moved files should not be there.
'''

import shutil
import os

def start(source,destination):
    files = os.listdir(source)
    for f in files:
        src_f = source + str(f)
        dst_f = destination + str(f)

        print "File transfer : %s " % src_f
        print "       to other location : %s " % dst_f

        shutil.move(src_f, dst_f)

source = '/Users/Mac/Desktop/FolderA/'
destination = '/Users/Mac/Desktop/FolderB/'
#c:\ is for windows only

start(source,destination)
