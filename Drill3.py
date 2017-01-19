import os
import datetime
import shutil

def transfer(src,dst):
    original_folder = os.listdir(src)
    for file in original_folder:
        if file.endswith('.txt'):
                file_absolute_path = src+file # src = path of directory; file = name of file
                file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(file_absolute_path))
                if datetime.datetime.now() - file_modified <= datetime.timedelta(hours=24):
                    shutil.copy(file_absolute_path,dst)
                    print (file + " file modified within 24 hrs has been copied to: " + os.path.abspath(dst))
                else:
                    print ("no.txt files have been modified within 24 hrs")
                 
src="/Users/Mac/Desktop/Original/"  
dst="/Users/Mac/Desktop/Receiving/" 
transfer(src,dst)
