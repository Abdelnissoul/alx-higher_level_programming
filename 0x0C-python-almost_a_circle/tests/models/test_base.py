#!/usr/bin/python3
"""Unit tests for the Base class"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def test_id_increment(self):
        """Test if id increments correctly"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_given_id(self):
        """Test if given id is assigned correctly"""
        b = Base(10)
        self.assertEqual(b.id, 10)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()

