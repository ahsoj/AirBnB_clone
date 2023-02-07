#!/usr/bin/env python3
""" Test case for pycodepass """
import unittest


class TestPyPassMethods(unittest.TestCase):

    def test_pass(self):
        self.assertEqual("foo", "foo")

    def test_isUpper(self):
        self.assertTrue("pass the pycode checks".islower())


if __name__ == "__main__":
    unittest.main()
