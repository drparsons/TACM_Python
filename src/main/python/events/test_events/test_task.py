import unittest

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from task import Task

"""
import sys
sys.path.append("D:\\Programming\\TACM\\src\\main\\python\\events")
from task import Task
"""

class Test_Task(unittest.TestCase):
    def test_constructor(self):
        task2 = Task("Type2", "Description2")
        self.assertEqual(task2.getDesc(), "Description2", "Should be Description2")
        self.assertEqual(str(task2.getType()), "Type2", "Should be __str__ of Type(Type2)")

if __name__ == "__main__":
    unittest.main()