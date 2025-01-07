#!/usr/bin/env python3
import unittest
from modulehqy import randcircle

class TestMyFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(randcircle(2), 2)

if __name__ == '__main__':
    unittest.main()

