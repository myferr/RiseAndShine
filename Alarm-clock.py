"""
Alarm Clock - A simple clock where it plays a sound 
after X number of minutes/seconds or at a particular time.
"""
from tkinter import *
import datetime
import time
import simpleaudio as sa


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current Time:", current_time)
        if current_time == set_alarm_timer:
            print("Time to Wake up")
            wave_obj = sa.WaveObject.from_wave_file("sound.wav")
            for _ in range(5):
                play_obj = wave_obj.play()
                play_obj.wait_done()
            print("Set alarm again")
            return


def actual_time():
    set_alarm_timer = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm(set_alarm_timer)


# Tkinter setup
clock = Tk()
clock.title("TryCatch Alarm Clock")
clock.geometry("500x250")

# UI Elements
Label(clock, text="At what time do you wanna get up?",
      fg="Blue", font=("Arial", 20, 'bold')).place(x=35, y=10)
Label(clock, text="Enter the time in 24 hr format",
      fg="Blue", bg="black", font=("Arial", 15, 'bold')).place(x=115, y=200)
Label(clock, text="Hour  Min   Sec", font=60).place(x=150, y=90)

# Variables to set the alarm
hour = StringVar()
minute = StringVar()
second = StringVar()

Entry(clock, textvariable=hour, bg="powderblue", width=15).place(x=150, y=120)
Entry(clock, textvariable=minute, bg="powderblue", width=15).place(x=190, y=120)
Entry(clock, textvariable=second, bg="powderblue", width=15).place(x=240, y=120)

Button(clock, text="Set Alarm", fg="green", activebackground="grey", activeforeground="darkgreen", width=10, font=(
    "Arial", 15, 'bold'), command=actual_time).place(x=200, y=150)

clock.mainloop()
