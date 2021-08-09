"""
Name: David Parsons
Date: 07/09/2021
TACM Task Class
Description: Inhereits Event Class. For holding day
information.
"""
##todo: add database backup wrapper 
# (no database or backup inside here)

from event import Event
from datetime import date
from task import Task

class Day(Event):
    def __init__(self):
        self.dayDate = date.today()
        self.dayTasks = list()

    def addTask(self, task):
        self.dayTasks.append(task)
    
    def getDate(self):
        return self.dayDate

    def getTasks(self):
        return self.dayTasks
#Date
#Task Array


#Add to Task Array
#When setting type to task object, search 

#Create Day (Set start time) (hooks for gui to call)
#End Day


#Getter/Setter
from type import Type

if __name__ == "__main__":
    print('hello world')
    type1 = Type("TestName1", "TestDescription1", "CHG001", "TestComment1")
    type2 = Type("TestName2", "TestDescription2", "CHG002", "TestComment2")
    task1 = Task(type1, "task1")
    task2 = Task(type2, "task2")
    task3 = Task(type1, "task3")
    day0 = Day()
    print(day0.getDate())
    day0.addTask(task1)
    day0.addTask(task2)
    day0.addTask(task3)
    for task in day0.getTasks():
        print("task name: ", task)
        print("task type: ", task.getType())
