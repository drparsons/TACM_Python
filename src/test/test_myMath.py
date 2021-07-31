import unittest
from unittest import suite
from myMath import myMath2

class Test_myMath(unittest.TestCase):
    #name of test should start with "test_"
    def test_add(self):
        self.assertEqual(myMath2.add(1,1), 2, "Should be 2")
    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__ == "__main__":
    unittest.main()

    
