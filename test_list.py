#!/usr/bin/env python3

import unittest
from linked_list import LinkedList

class TestLinkedListMethods(unittest.TestCase):
    """test_append tests the append function"""
    def test_append(self):
        linked_list = LinkedList().append(1).append(2).append(3)
        expected = [1, 2, 3]
        result = [item for item in linked_list]
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()
