from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.top = None

    def push(self, e):
        item = StackItem(e)
        item.next = self.top
        self.top = item

    def pop(self):
        if self.top is None:
            return None
        item = self.top
        self.top = self.top.next
        return item.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

class StackItem:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListStack:
    def __init__(self):
        self.v = []

    def push(self, e):
        self.v.append(e)

    def pop(self):
        if len(self.v) == 0:
            return None
        return self.v.pop()

    def peek(self):
        if len(self.v) == 0:
            return None
        return self.v[-1]

class LinkedListStack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, e):
        self.ll.insert(0, e)

    def pop(self):
        return self.ll.remove(0)

    def peek(self):
        return self.ll.get(0)
