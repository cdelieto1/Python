#Title: Datetime – Python 2.7 – IDLE
#Cassandra Delieto -- Jan 12th, 2017
#Written on Mac OS

from datetime import datetime #from datetime = class datetime.datetime contains every possible datetype needed for collecting the time.  

def Get_the_PDX_time():
        print ("The current [military] time in PDX is " + str(time))

def NYC():
    time = portland_hr + 3
    if time >= 9 and time <= 21:
        print ("NYC location is currently open")
    else:       
        print ("NYC located is currently closed")

def London():
    time = portland_hr + 9
    if time >=9 and time <=21:
        print ("London location is currently open")
    else:       
        print ("London located is currently closed")

time = datetime.now().time() #collects the time right now
portland_hr=time.hour #gets the hour only, that way, we get an integer and can translate it into other timezones
Get_the_PDX_time() 
NYC()
London()
