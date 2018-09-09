class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail = self.tail.append(new_node)
        return self

    def __iter__(self):
        return LinkedListIterator(self.head)

class LinkedListIterator:
    def __init__(self, start):
        self.cursor = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor is None:
            raise StopIteration
        current = self.cursor
        self.cursor = self.cursor.next
        return current.data

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, n):
        self.next = n
        return self.next
