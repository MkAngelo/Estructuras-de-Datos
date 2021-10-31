from double_linked_list import *


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
            
    def append(self, data, previous=None, next=None):

        if self.head == None:
            self.head = TwoWayNode(data)
            self.tail = self.head
        else:
            tail = self.tail
            while tail.next:
                tail = tail.next
            tail.next = TwoWayNode(data, previous, next)

        self.size += 1

    def size(self):
        return str(self.size)

    def iter(self):
        probe = self.tail
        while probe.previous:
            print(probe.data)
            probe = probe.previous

        