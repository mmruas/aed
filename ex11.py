class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.previous = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrevious(self, newprevious):
        self.previous = newprevious


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.amount = 0

    def isEmpty(self):
        return self.head == None and self.tail == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        temp.setPrevious(self.tail)
        self.head = temp
        self.amount += 1

    def append(self, item):
        temp = Node(item)
        temp.setPrevious(self.tail)
        temp.setNext(self.head)
        self.tail = temp
        self.amount += 1

    def insert(self, pos, item):
        if pos == 0:
            temp = Node(item)
            temp.setNext(self.head)
            self.head = temp
            return
        i = 1
        current = self.head
        previous = None
        while i != pos:
            previous = current
            current = current.getNext()
            i += 1

        temp = Node(item)
        previous.setNext(temp)
        previous.setPrevious(current.previous)
        temp.setNext(current)
        self.amount += 1

    def size(self):
        return self.amount

    def index(self, item):
        current = self.head
        found = False
        i = 0
        if self.head == item:
            return i
        i += 1
        while current != self.head and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                i += 1

        return i

    def search(self, item):
        current = self.head
        found = False
        i = 0
        if self.head == item:
            return True
        while current != self.head and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        '''current = self.head
        previous = self.tail
        found = False

        if item == self.tail:
            previous = self.tail
            current.setPrevious(previous.getPrevious())
            self.tail = None
            return

        if item == self.head:
            previous = self.tail
            current.setPrevious(previous)
            current.setNext(current.getNext())
            self.head = None
            return

        while not found:
            if current.getData() == item:
                found = True
            else:
                if current.getNext() == self.tail:
                    break
                else:
                    previous = current
                    current = current.getNext()
                    self.amount -= 1

        next = current.getNext()
        previous = current.getPrevious()
        current.setNext(current.getNext())
        current
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())'''

        current = self.head
        i = 0
        while current.getData() != item:
            current = current.getNext()
            if current == self.head:
                i += 1
            if i > 1:
                return

        previous = current.getPrevious()
        previous.setNext(current.getNext())

    def List(self):
        self.data = None
        self.head = None
        self.tail = None
        return self



mylist = DoubleLinkedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

#mylist.remove(54)
print(mylist.size())
#mylist.remove(93)
print(mylist.size())
#mylist.remove(9999999)
print(mylist.size())
print(mylist.search(93))