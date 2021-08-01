import unittest

#from ..playground import multMath as mult

#import sys
#sys.path.append("D:\\Programming\\TACM\\src\\playground")
#from multMath import multMath

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from playground.multMath import multMath

class Test_multMath(unittest.TestCase):
    #name of test should start with "test_"
    def test_add(self):
        self.assertEqual(multMath().mult(2,2), 4, "Should be 4")
        #self.assertEqual(multMath(2,2), 4, "Should be 2")
    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__ == "__main__":
    unittest.main()




