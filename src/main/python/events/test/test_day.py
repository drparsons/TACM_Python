"""
Name: David Parsons
Date: 8/8/21
TACM Day Test 
Description: Tests the Day Class using unittest
"""


from typing import Counter
import unittest

#for fixing file path errors in vsCode
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


"""
#for fixing file path errors in vsCode, hardcode method
import sys
sys.path.append("D:\\Programming\\TACM\\src\\main\\python\\events")
from task import Task
"""

from day import Day
from task import Task
from type import Type
from datetime import date

class Test_Day(unittest.TestCase):

    def test_Day(self):
        # Setup      
        type1 = Type("TestName1", "TestDescription1", "CHG001", "TestComment1")
        type2 = Type("TestName2", "TestDescription2", "CHG002", "TestComment2")
        task1 = Task(type1, "task1")
        task2 = Task(type2, "task2")
        task3 = Task(type1, "task3")    
        day0 = Day()
        self.assertEqual(day0.getDate(), date.today())
        day0.addTask(task1)
        day0.addTask(task2)
        day0.addTask(task3)
        # readback tasks added to Day object
        for itr, task in enumerate(day0.getTasks()):
            self.assertEqual(str(task), "task" + str(itr+1) )


if __name__ == "__main__":
    unittest.main()