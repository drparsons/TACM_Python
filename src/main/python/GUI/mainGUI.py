import tkinter as tk

import os, sys
from tkinter import Button, Entry, Label, Menu, Scrollbar, Toplevel, font
from tkinter.constants import ANCHOR, CENTER, END, RIGHT, Y
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import sys
sys.path.append("D:\\Programming\\TACM\\src\\main\\python\\events")

from day import Day
from task import Task
from type import Type


# ---- Create test variables
type1 = Type("TestName1", "TestDescription1", "CHG001", "TestComment1")
type2 = Type("TestName2", "TestDescription2", "CHG002", "TestComment2")
types = [type1, type2]
task1 = Task(type1, "task1")
task2 = Task(type2, "task2")
task3 = Task(type1, "task3")    
day0 = Day()
day0.addTask(task1)
day0.addTask(task2)
day0.addTask(task3)

window = tk.Tk()

class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Hello World")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
        self.top.bind('<Return>',self.enter_cleanup)
        self.type = tk.StringVar(self)
        type1 = Type("TestName1", "TestDescription1", "CHG001", "TestComment1")
        type2 = Type("TestName2", "TestDescription2", "CHG002", "TestComment2")
        types = [type1, type2]
        self.option = tk.OptionMenu(
            self,
            self.type,
            str(types[0]),
            *self.types
        )
    def enter_cleanup(self, key_press):
        print(key_press) #'<Return>' bind gives 2 arguments 
        self.cleanup()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

def popup():
    w=popupWindow(window)
    button_newTask["state"] = "disabled" 
    window.wait_window(w.top)
    button_newTask["state"] = "normal"
    task4 = Task(type2,w.value)
    day0.addTask(task4)



#window.geometry("400x250")

#give weight so it floats

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)


#---------Table---------
frame = tk.Frame(master=window, borderwidth=5)
frame.grid(row=0, column=0, sticky="nsew")

#size
TaskTypeWidth = 15
TaskDescWidth = 20
TaskTimeWidth = 12

#Task Type
e = tk.Entry(frame, width=TaskTypeWidth)
e.grid(row=0,column=0)
e.insert(END, "Task Type")
#Task Description
f = tk.Entry(frame, width=TaskDescWidth)
f.grid(row=0,column=1)
f.insert(END, "Task Description")
#Start Time
f = tk.Entry(frame, width=TaskTimeWidth)
f.grid(row=0,column=2)
f.insert(END, "Start Time")
#TEnd Time
f = tk.Entry(frame, width=TaskTimeWidth)
f.grid(row=0,column=3)
f.insert(END, "End Time")
#TDuration
f = tk.Entry(frame, width=TaskTimeWidth)
f.grid(row=0,column=4)
f.insert(END, "Duration")

def update_table():
    for itr, task in enumerate(day0.getTasks()):
        #Task Type
        e = tk.Entry(frame, width=TaskTypeWidth, fg='blue')
        if (e.grid_info() == {}):
            e.grid(row=itr + 1,column=0)
            e.insert(END, str(task))
        
        #Task Description
        f = tk.Entry(frame, width=TaskDescWidth, fg='blue')
        if (f.grid_info() == {}):
            f.grid(row=itr + 1,column=1)
            f.insert(END, str(task.getType()))
    
        #Start Time
        g = tk.Entry(frame, width=TaskTimeWidth)
        if (g.grid_info() == {}):
            g.grid(row=itr + 1,column=2)
            g.insert(END, task.getStart())
    
        #End Time
        h = tk.Entry(frame, width=TaskTimeWidth)
        if (h.grid_info() == {}):
            h.grid(row=itr + 1,column=3)
            h.insert(END, task.getEnd())
        
        #Duration
        j = tk.Entry(frame, width=TaskTimeWidth)
        if (j.grid_info() == {}):
            j.grid(row=itr + 1,column=4)
            j.insert(END, task.duration())
    window.after(1000, update_table)



#-------------Side Buttons---------------
frame2 = tk.Frame(master=window, borderwidth=5)
frame2.grid(row=0, column=1, sticky="nsew")
button1 = tk.Button(
    master=frame2,
    text="New Type",
    width=15
)
button1.grid(row=0, column=0)
button2 = tk.Button(
    master=frame2,
    text="End Day",
    width=15
)
button2.grid(row=1, column=0)
buttonExit = tk.Button(
    master=frame2,
    text="Exit",
    width=15,
    command=window.quit
)
buttonExit.grid(row=3, column=0)
#----------Bottom Buttons-----------
#TODO doesn't work, should be on bottom
frame3 = tk.Frame(master=window, border=5)
frame3.grid(row=2, column=0, sticky="ew", columnspan=2)
frame3.grid_rowconfigure(0, weight=1)
frame3.grid_columnconfigure(0, weight=1)
button_newTask = tk.Button(
    master=frame3,
    text="New Task",
    width=15, command=popup
)
button_newTask.grid(row=0, column=0)#, columnspan=2)

# ------------------- Update Table test--------
import random
def table_update():
    l.config(text=str(random.random()))
    window.after(1000,table_update)

l = tk.Label(master=window, text='0')
l.grid(row=3, column=0,sticky="ew",columnspan=2)
window.after(1000,table_update)
window.after(1000, update_table)
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