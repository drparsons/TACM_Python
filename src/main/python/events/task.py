"""
Name: David Parsons
Date: 07/09/2021
TACM Task Class
Description: Inhereits Event Class. For holding task
information.
"""

from event import Event

class Task(Event):
#Type: Type
#Description    
    def __init__(self, type = " ", desc = " "):
        super().__init__()
        self.type = type
        self.desc = desc


#Create Task (hooks for GUI to call)

#Start Task
#End Task

#Getters and Setters
    def getType(self):
        return self.type

    def getDesc(self):
        return self.desc

import time

if __name__ == "__main__":
    print("hello world!")
    task1 = Task()
    print(task1.getDesc())
    print(task1.getType())
    time.sleep(5)
    task1.setEnd()
    print(task1.duration())
    task2 = Task("Type2", "Description2")
    print(task2.getDesc())
    print(task2.getType())
    time.sleep(2)
    task2.setEnd()
    print(task2.duration())
