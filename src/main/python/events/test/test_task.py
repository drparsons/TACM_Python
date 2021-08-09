"""
Name: David Parsons
Date: 8/8/21
TACM Task Test 
Description: Tests the Task Class using unittest
"""


import unittest

#for fixing file path errors in vsCode
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from task import Task

"""
#for fixing file path errors in vsCode, hardcode method
import sys
sys.path.append("D:\\Programming\\TACM\\src\\main\\python\\events")
from task import Task
"""

import time
from type import Type

class Test_Task(unittest.TestCase):
    def test_Task_default_constructor(self):
        task1 = Task()
        self.assertEqual(task1.getDesc(), " ")
        self.assertEqual(str(task1.getType()), " ")
    
    def test_Task_constructor(self):
        task2 = Task("Type2", "Description2")
        self.assertEqual(task2.getDesc(), "Description2", "Should be Description2")
        self.assertEqual(str(task2.getType()), "Type2", "Should be __str__ of Type(Type2)")

    def test_Task_timer(self):
        #upon init of event-subclass, start time is set
        task1 = Task()
        time.sleep(1)
        task1.setEnd()
        self.assertGreaterEqual(float(task1.duration()), 1)

    def test_Task_type(self):
        type1 = Type("TestName", "TestDescription", "CHG001", "TestComment")
        task3 = Task(type1, "test task")
        self.assertEqual(task3.getDesc(), "test task")
        self.assertEqual(str(task3.getType()), "TestName")


if __name__ == "__main__":
    unittest.main()