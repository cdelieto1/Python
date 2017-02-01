#Cassandra Delieto
#Python vs. 3.6 using sublime text editor
#1/30/17

from tkinter import *
import tkinter as ttk
from datetime import datetime
from datetime import timedelta
import shutil, time, os, sqlite3
import Drill_5

def create_db(self):
    conn = sqlite3.connect('timestamp.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_timestamp(ID INTEGER PRIMARY KEY, tsp REAL );")
        cur.execute("""INSERT INTO tbl_timestamp (tsp) VALUES (0.0)""")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('timestamp.db')
    with conn:
        cur = conn.cursor()
        current_time=time.time()
        cur.execute("INSERT INTO tbl_timestamp (tsp) VALUES ({})".format(current_time,))
        conn.commit()
    conn.close()
    timer(self)

def timer(self):
    conn = sqlite3.connect('timestamp.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT tsp FROM tbl_timestamp ORDER BY tsp DESC LIMIT 1 OFFSET 1")
        recent=cur.fetchone()[0]
        theTime=time.ctime(recent)
        print (theTime)
        self.lr_var.set(theTime)
        conn.commit()
    conn.close()

if __name__ == "__main__":
    pass
