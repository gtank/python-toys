class LinkedList:
    @staticmethod
    def from_list(contents):
        ll = LinkedList()
        for item in contents:
            ll.append(item)
        return ll

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

    def insert(self, pos, data):
        new_node = LinkedListNode(data)

        # Special case for insert at beginning
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        prev = self.head
        position = 0
        inserted = False
        for item in self:
            if position == pos:
                new_node.next = prev.next
                prev.next = new_node
                if new_node.next is None:
                    self.tail = new_node
                inserted = True
                break
            prev = item
            position += 1

        if not inserted:
            raise ListSizeException("index past size of list")

        return

    def search(self, target):
        position = 0
        for item in self:
            if item.data == target:
                return (position, item)
            position += 1

    def reverse(self):
        prev = None
        item = self.head

        # Reverse the pointers.
        # TODO: can do this with the iterator? relies on rebinding loop item.
        while item is not None:
            next_item = item.next
            item.next = prev
            prev = item
            item = next_item
        self.head = prev

    def get(self, index):
        pos = 0
        for element in self:
            if pos == index:
                return element.data
            pos = pos + 1
        raise ListSizeException("index past size of list")

    def remove(self, index):
        # Special case for empty list
        if self.head is None:
            return None

        # Special case for beginning of list
        if index == 0:
            removed = self.head.data
            self.head = self.head.next
            return removed

        # Otherwise, walk the list
        prev = None
        curr = self.head
        for _ in range(index):
            prev = curr
            curr = curr.next
            if curr is None:
                raise ListSizeException("index past size of list")
        removed = curr.data
        prev.next = curr.next
        return removed

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
        return current

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, n):
        self.next = n
        return self.next

class ListSizeException(Exception):
    pass
