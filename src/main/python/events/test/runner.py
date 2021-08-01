# tests/runner.py
import unittest

# import your test modules
import test_task

#initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

#add test cases
suite.addTests(loader.loadTestsFromModule(test_task))

"""
verbosity:
0 (quiet): you just get the total numbers of tests executed and the global result
1 (default): you get the same plus a dot for every successful test or a F for every failure
2 (verbose): you get the help string of every test and the result
"""

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

