#!/usr/bin/env python3

import unittest
from stack import Stack, ListStack, LinkedListStack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)

    def test_pop(self):
        popped = self.stack.pop()
        self.assertIs(popped, None)

        self.stack.push(1)
        popped = self.stack.pop()
        self.assertEqual(popped, 1)

    def test_full_stack(self):
        for i in range(10):
            self.stack.push(i)

        self.assertEqual(self.stack.peek(), 9)

        for i in range(10):
            self.assertEqual(self.stack.pop(), 9-i)

        self.assertEqual(self.stack.pop(), None)


class TestListStack(unittest.TestCase):
    def setUp(self):
        self.stack = ListStack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)

    def test_pop(self):
        popped = self.stack.pop()
        self.assertIs(popped, None)

        self.stack.push(1)
        popped = self.stack.pop()
        self.assertEqual(popped, 1)

    def test_full_stack(self):
        for i in range(10):
            self.stack.push(i)

        self.assertEqual(self.stack.peek(), 9)

        for i in range(10):
            self.assertEqual(self.stack.pop(), 9-i)

        self.assertEqual(self.stack.pop(), None)

class TestLinkedListStack(unittest.TestCase):
    def setUp(self):
        self.stack = LinkedListStack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)

    def test_pop(self):
        popped = self.stack.pop()
        self.assertIs(popped, None)

        self.stack.push(1)
        popped = self.stack.pop()
        self.assertEqual(popped, 1)

    def test_full_stack(self):
        for i in range(10):
            self.stack.push(i)

        self.assertEqual(self.stack.peek(), 9)

        for i in range(10):
            self.assertEqual(self.stack.pop(), 9-i)

        self.assertEqual(self.stack.pop(), None)
