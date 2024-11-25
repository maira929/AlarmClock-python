#import threading
from tkinter import *
import datetime
import time
from boombox import BoomBox
#import pygame
#from playsound import playsound
#pygame.init()
#pygame.mixer.init()

boombox = BoomBox("mixkit-classic-alarm-995.wav")
def alarm(set_alarm_time):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d:%m:%y")
        print("The date is: ", date)
        print(now)
        if now==set_alarm_time:
            print("Time to wake up")
            boombox.play()
            break
def actual_time():
   set_alarm_time = f"{hour.get()}:{min.get()}:{sec.get()}"
   alarm(set_alarm_time)


clock = Tk()
clock.title("My First Alarm Clock")
clock.geometry("400x200")
time_format = Label(clock, text="Enter time in 24 hour format!",fg="red",bg="black",font="arial").place(x=60,y=120)
add_time = Label(clock, text="Hour  Min   Sec",font=60).place(x=110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)


hour = StringVar()
min = StringVar()
sec = StringVar()

get_hour = Entry(clock, textvariable=hour , bg="pink" , width=15).place(x=110,y=30)
get_min = Entry(clock,textvariable=min,bg="pink",width=15).place(x=150,y=30)
get_sec = Entry(clock, textvariable=sec,bg="pink",width=15).place(x=200,y=30)


submit = Button(clock,text="submit" , fg="red" , width=10 ,command = actual_time).place(x=200,y=70)
clock.mainloop()
#main
