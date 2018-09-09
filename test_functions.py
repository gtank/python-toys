#!/usr/bin/env python3

import unittest
import fun

TEST_TABLE = [
    ("input", "tupni"),
    ("kayak", "kayak"),
    ("amanaplanacanalpanama", "amanaplanacanalpanama"),
]

class TestStringReverse(unittest.TestCase):
    def test_reverse(self):
        for (test_input, expected_output) in TEST_TABLE:
            self.assertEqual(expected_output, fun.reverse(test_input))

if __name__ == "__main__":
    unittest.main()
