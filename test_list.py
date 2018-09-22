#!/usr/bin/env python3

import unittest
from linked_list import LinkedList, ListSizeException

class TestLinkedListMethods(unittest.TestCase):
    def test_append(self):
        linked_list = LinkedList().append(1).append(2).append(3)
        expected = [1, 2, 3]
        result = [item.data for item in linked_list]
        self.assertEqual(expected, result)

    def test_insert(self):
        linked_list = LinkedList().append(1).append(2).append(3)
        linked_list.insert(2, 4)
        expected = [1, 2, 4, 3]
        result = [item.data for item in linked_list]
        self.assertEqual(expected, result)

    def test_insert_at_head(self):
        linked_list = LinkedList().append(1).append(2).append(3)
        linked_list.insert(0, 4)
        expected = [4, 1, 2, 3]
        result = [item.data for item in linked_list]
        self.assertEqual(expected, result)

    def test_insert_past_tail(self):
        linked_list = LinkedList().append(1).append(2).append(3)
        with self.assertRaises(ListSizeException):
            linked_list.insert(3, 4)

    def test_static_initializer(self):
        linked_list = LinkedList.from_list([1, 2, 3, 4])
        expected = [1, 2, 3, 4]
        result = [item.data for item in linked_list]
        self.assertEqual(expected, result)

    def test_search(self):
        linked_list = LinkedList.from_list([1, 2, 3, 4])
        index, item = linked_list.search(3)
        self.assertEqual(index, 2)
        self.assertEqual(item.data, 3)
        self.assertEqual(item.next.data, 4)

    def test_reverse(self):
        linked_list = LinkedList.from_list([1, 2, 3, 4])
        linked_list.reverse()
        expected = [4, 3, 2, 1]
        result = [item.data for item in linked_list]
        self.assertEqual(expected, result)

    def test_get(self):
        linked_list = LinkedList.from_list([1, 2, 3, 4])

        start = linked_list.get(0)
        middle = linked_list.get(2)
        last = linked_list.get(3)

        self.assertEqual(start, 1)
        self.assertEqual(middle, 3)
        self.assertEqual(last, 4)

        with self.assertRaises(ListSizeException):
            linked_list.get(5)

    def test_remove(self):
        linked_list = LinkedList.from_list([1, 2, 3, 4])
        removed_value = linked_list.remove(0)
        self.assertEqual(removed_value, 1)
        self.assertEqual([item.data for item in linked_list], [2, 3, 4])

        linked_list = LinkedList.from_list([1, 2, 3, 4])
        removed_value = linked_list.remove(2)
        self.assertEqual(removed_value, 3)
        self.assertEqual([item.data for item in linked_list], [1, 2, 4])

        linked_list = LinkedList.from_list([1, 2, 3, 4])
        removed_value = linked_list.remove(3)
        self.assertEqual(removed_value, 4)
        self.assertEqual([item.data for item in linked_list], [1, 2, 3])

        with self.assertRaises(ListSizeException):
            linked_list = LinkedList.from_list([1, 2, 3, 4])
            linked_list.remove(4)

if __name__ == "__main__":
    unittest.main()
