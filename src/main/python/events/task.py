"""
Name: David Parsons
Date: 07/09/2021
TACM Task Class
Description: Inhereits Event Class. For holding task
information.
"""

from event import Event
from type import Type

class Task(Event):
#Type: Type
#Description    
    def __init__(self, type = Type(), desc = " "):
        super().__init__()
        self.type = type
        self.desc = desc

    def __str__(self):
        return self.desc
#Create Task (hooks for GUI to call)
#Start Task
#End Task

#Getters and Setters
    def getType(self):
        return (self.type)
        #return self.type.__str__()

    def getDesc(self):
        return self.desc

    def setType(self, type):
        self.type = type
    
    def setDesc(self, desc):
        self.desc = desc

import time

if __name__ == "__main__":
    print("hello world!")
    print("\nTask1 default constructor 5s wait")
    task1 = Task()
    print("task1 descript: ", task1.getDesc())
    print("task1 type: ", task1.getType())
    time.sleep(5)
    task1.setEnd()
    print(task1.duration())
    
    print("\n Task2 constructor and 2 sec wait")
    task2 = Task("Type2", "Description2")
    print(task2.getDesc())
    print(task2.getType())
    #print(task2.getType())
    time.sleep(2)
    task2.setEnd()
    print("Task2 wait time: ", task2.duration())

    print("\nTask3 with type")
    type1 = Type("TestName", "TestDescription", "CHG001", "TestComment")
    task3 = Task(type1, "test task")
    print(task3.getDesc())
    print(task3.getType())