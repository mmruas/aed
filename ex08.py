import ex01

class Queue:
    def __init__(self):
        self.items = ex01.LinkedList()

    def is_empty(self):
        return self.items.isEmpty()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items.get(0)

    def size(self):
        return self.items.size()