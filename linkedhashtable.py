"""
description: A chained hash table that
            (1) Automatically expands and contracts (by a factor of 2), and
            (2) Recalls the insertion order of its elements
file: linkedhashtable.py
language: python3
author: vinay more
"""

from set import SetType

class LinkedHashTable(SetType):


    __slots__ = 'table', 'capacity', 'size', 'back', 'front','Load_Limit','minBuckets'

    def __init__( self, capacity=100,Load_Limit=0.75 ):
        """
        this method initializes the constructor for class LinkedHashTable
        :param capacity: maximum number of buckets in the set
        :param Load_Limit: limit for load factor to cause rehashing
        :return: None
        """
        self.minBuckets = 10
        self.table = capacity * [ None ]
        self.capacity=capacity
        if (self.capacity<self.minBuckets):
            self.capacity = self.minBuckets
        self.Load_Limit = Load_Limit
        self.back = None
        self.front = None
        self.size = 0

    class LinkedNode :
        """
        class node for the linked list used in chaining
        """

        __slots__ = 'next','previous','value', 'forward'

        def __init__( self,value=None):
            """
            constructor of class LinkedNode
            :param value: value to be added in the set
            :return: None
            """

            self.value = value
            self.forward = None
            self.previous = None
            self.next = None

    def hashFunction(self,value):
        """
        method to generate hash function
        :param value: value that is to be added to the set
        :return: index: index where value is added
        """
        sum = 0
        power = 0
        for letter in value:
            sum = sum + ord(letter)*(31**power)
            power += 1
        index = sum%(len(self.table))
        return index

    def contains(self,value):
        """
        method to check if a value exists in the node
        :param value: value that is to be checked for existence in set
        :return: True or False
        """
        if not isinstance(value,str):
            pass
        else:
            index = int(self.hashFunction(value))
            if self.table[index]==None:
                return False
            else:
                linkedNode = self.table[index]
                temp = linkedNode.value
                while linkedNode is not None:
                    if linkedNode.value == value:
                        return True
                    linkedNode = linkedNode.next

                return False


    def add(self,value):
        """
        method to add value in the set
        :param value: value that is to be added
        :return: None
        """
        if (((self.size+1)/self.capacity)>=self.Load_Limit):
            self._rehash(0)
        if not isinstance(value,str):
            pass
        elif self.contains(value):
            print('duplicate value cannot be added')
        else:
            entry = LinkedHashTable.LinkedNode(value)
            index = int(self.hashFunction(value))
            if self.size == 0:
                self.table[index] = entry
                self.front = entry
                self.back = entry
            elif self.table[index] is None:
                self.table[index] = entry
            else:
                current = self.table[index]
                while current.next is not None:
                    current = current.next
                current.next = entry
            self.back.forward = entry
            entry.previous = self.back
            self.back = entry
            self.back.forward = None
            self.size+=1


    def remove(self,value):
        """
        method to remove element from set
        :param value: element to be removed from set
        :return: None
        """
        if not isinstance(value,str):
            pass
        elif self.contains(value) == False:
            print('value not present')
        else:
             index = int(self.hashFunction(value))
             linkedNode = self.table[index]
             previous = linkedNode

             while linkedNode is not None:
                 if linkedNode.value == value:
                     if previous == linkedNode:
                        self.table[index] = linkedNode.next
                     else:
                        previous.next = linkedNode.next

                     previousNode = linkedNode.previous
                     fwdNode = linkedNode.forward

                     if previousNode is not None:
                        previousNode.forward = fwdNode

                     if fwdNode is not None:
                        fwdNode.previous = previousNode

                     if self.front == linkedNode:
                         self.front = linkedNode.forward

                     if self.back == linkedNode:
                         self.back = linkedNode.previous
                         self.back.forward = None

                     self.size-=1

                     if (self.size<(self.Load_Limit*self.capacity)):
                         self._rehash(1)
                     break

                 previous = linkedNode
                 linkedNode = linkedNode.next



    def __iter__(self):
        """
        method to itereate over the set
        :return: None
        """
        node = self.front
        while node is not None:
            yield node.value
            node = node.forward

    def _rehash( self ,number):
        """
        method to create new table for the set after rehashing
        :param number: number to decide whether rehash was called to increase
                       or decrease the table size
        :return: None
        """
        if number==0:
            print("Rehashing to increase the size")
            newCapacity = 2 * self.capacity
            newSet = LinkedHashTable(newCapacity)
            node = self.front
            while node is not None:
                newSet.add(node.value)
                node = node.forward

            self.table = newSet.table
            self.capacity = newSet.capacity
        elif number==1:
            print("Rehashing to decrease the size")
            newCapacity = self.capacity//2
            newSet = LinkedHashTable(newCapacity)
            node=self.front
            while node is not None:
                newSet.add(node.value)
                node = node.forward
            self.table = newSet.table
            self.capacity = newSet.capacity
