"""
Name: David Parsons
Date: 8/8/21
TACM Type Test 
Description: Tests the Type Class using unittest
"""
import unittest

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from type import Type

"""
import sys
sys.path.append("D:\\Programming\\TACM\\src\\main\\python\\events")
from task import Task
"""

class Test_Type(unittest.TestCase):
    def test_Type_default_constructor(self):
        type0 = Type()
        self.assertEqual(str(type0)," ")
    
    def test_Type_constructor(self):
        type1 = Type("TestName", "TestDescription", "CHG001", "TestComment")
        self.assertEqual(type1.getName(), "TestName")
        self.assertEqual(type1.getDesc(), "TestDescription")
        self.assertEqual(type1.getChg(), "CHG001")
        self.assertEqual(type1.getComment(), "TestComment")

    def test_Type_setter(self):
        type0 = Type()
        type0.setName("Set")
        self.assertEqual(str(type0),"Set")


if __name__ == "__main__":
    unittest.main()