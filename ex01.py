class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class LinkedList:

    def __init__(self):
        self.head = None
        self.amount = 0

    def get(self, index):
        currentIndex = 0
        current = self.head
        while currentIndex != index:
            index += 1
            current = current.next
        return current

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.amount += 1

    def append(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.amount += 1

    def copy(self):
        return self

    def concatenate(self, other):
            last = self.get(self.size() - 1)
            last.next = other.head

    def insert(self, pos, item):
        if pos == 0:
            temp = Node(item)
            temp.setNext(self.head)
            self.head = temp
            return
        i = 0
        current = self.head
        previous = None
        while i != pos:
            previous = current
            current = current.next
            i += 1

        temp = Node(item)
        previous.setNext(temp)
        temp.setNext(current)

    def size(self):
        return self.amount

        return count

    def index(self, item):
        current = self.head
        found = False
        i = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                i += 1

        return i

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                self.amount -= 1
                found = True
            else:
                if current.getNext() == None:
                    return
                else:
                    previous = current
                    current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        '''current = self.head
        previous = None
        while current != None:
            if current.getData() == item:
                self.amount -= 1
                self.replaceNode(current, previous)
            else:
                previous = current
                current = current.getNext()'''

    def List(self):
        self.data = None
        self.head = None
        return self

    def pop(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()

        erased = current.getData()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        return erased

    def pop(self, pos):
        currentIndex = 0
        current = self.head
        previous = None
        while pos != currentIndex:
            currentIndex += 1
            previous = current
            current = current.getNext()

        erased = current.getData()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        return erased

    def __str__(self):
        current = self.head
        stringToPrint = "[ "

        while current != None:
            stringToPrint = stringToPrint + ", " + str(current.getData())
            current = current.getNext()

        stringToPrint = stringToPrint +  "]"
        return stringToPrint

mylist = LinkedList()

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

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(9999999)
print(mylist.size())
print(mylist.search(93))

print(mylist.pop(2))
print(mylist)

print(mylist.index(31))