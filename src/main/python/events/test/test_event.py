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

if __name__ == "__main__":
    unittest.main()