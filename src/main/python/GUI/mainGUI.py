import tkinter as tk

import os, sys
from tkinter import Menu, Scrollbar, font
from tkinter.constants import END, RIGHT, Y
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import sys
sys.path.append("D:\\Programming\\TACM\\src\\main\\python\\events")

from day import Day
from task import Task
from type import Type


  
type1 = Type("TestName1", "TestDescription1", "CHG001", "TestComment1")
type2 = Type("TestName2", "TestDescription2", "CHG002", "TestComment2")
task1 = Task(type1, "task1")
task2 = Task(type2, "task2")
task3 = Task(type1, "task3")    
day0 = Day()
day0.addTask(task1)
day0.addTask(task2)
day0.addTask(task3)

window = tk.Tk()
#window.geometry("400x250")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

#---------Table---------
frame = tk.Frame(master=window, borderwidth=5)
frame.grid(row=0, column=0, sticky="nsew")

#size
TaskTypeWidth = 15
TaskDescWidth = 25

#Task Type
e = tk.Entry(frame, width=TaskTypeWidth)
e.grid(row=0,column=0)
e.insert(END, "Task Type")
#Task Description
f = tk.Entry(frame, width=TaskDescWidth)
f.grid(row=0,column=TaskDescWidth)
f.insert(END, "Task Description")
#TODO Start Time
#TODO End Time
#TODO Duration

for itr, task in enumerate(day0.getTasks()):
    #Task Type
    e = tk.Entry(frame, width=TaskTypeWidth, fg='blue')
    e.grid(row=itr + 1,column=0)
    e.insert(END, str(task))
    #Task Description
    f = tk.Entry(frame, width=TaskDescWidth, fg='blue')
    f.grid(row=itr + 1,column=TaskDescWidth)
    f.insert(END, str(task.getType()))
    #TODO Start Time
    #TODO End Time
    #TODO Duration


#-------------Side Buttons---------------
frame2 = tk.Frame(master=window, borderwidth=5)
frame2.grid(row=0, column=1, sticky="nsew")
button1 = tk.Button(
    master=frame2,
    text="New Type",
    width=15
)
button1.pack()
button2 = tk.Button(
    master=frame2,
    text="End Day",
    width=15
)
button2.pack()

#----------Bottom Buttons-----------
#TODO doesn't work, should be on bottom
frame3 = tk.Frame(master=window, border=5)
frame3.grid(row=50, column=0, sticky="ew", columnspan=50)
button3 = tk.Button(
    master=frame2,
    text="New Task",
    width=15
)
button3.pack()

#-------------Menu Bar--------------
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Day")#, command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help")#, command=donothing)
helpmenu.add_command(label="About...")#, command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)
window.mainloop()
#window.destroy()