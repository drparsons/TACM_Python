"""
Name: David Parsons
Date: 8/8/21
TACM Event Test 
Description: Tests the Task Class using unittest
"""


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

from event import Event
import time


class Test_Event(unittest.TestCase):
    def test_Event_timer(self):
        #upon init of event, start time is set
        event0 = Event()
        time.sleep(1)
        event0.setEnd()
        self.assertGreaterEqual(float(event0.duration()), 1)
    
    def test_convert(self):
        event0 = Event()
        self.assertEqual(event0.convertToSeconds("03:55:05 AM"), 14105)
        self.assertEqual(event0.convertToSeconds("03:55:05 PM"), 446105)

    def test_setTime(self):
        task2 = Event()
        task2.customSetStart("03:55:05 AM")
        task2.customSetEnd("03:55:05 PM")
        self.assertEqual(task2.duration(),"12:00:00")

if __name__ == "__main__":
    unittest.main()