# Python3.6 实现链表的一些操作

import numpy as np


class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.next = newdata

    def setNext(self, nextNode):
        self.next = nextNode


#if __name__ == "__main__":
#    tmp = Node(99)
#    tmp.setData(10)
#    print(tmp.getNext())

# 定义一个无序的链表


class UnOrderList(object):
    def __init__(self):
        self.head = None


    def isEmpty(self):
        return self.head == None

    def add(self, item):
        tmp = Node(item)
        tmp.setNext(self.head)
        self.head = tmp


    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found


    def remove(self,item):
        current = self.head
        preivous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                preivous = current
                current = current.getNext()
        if preivous == None:
            self.head = current.getNext()
        else:
            preivous.setNext(current.getNext())







if __name__ == "__main__":
    myList = UnOrderList()
    myList.add(31)
    myList.add(77)
    myList.add(17)
    myList.add(93)
    myList.add(26)
    tmp = myList.add(54)
    print(tmp)
    tmp1 = myList.search(17)
    print(tmp1)
    tmp2 = myList.remove(54)
    print(tmp2)


















def LinkedList():
    pass
