import ex01

class Stack:
    def __init__(self):
        self.items = ex01.LinkedList()

    def is_empty(self):
        return self.items.isEmpty()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items.get(self.items.size() - 1)

    def size(self):
        return self.items.size()