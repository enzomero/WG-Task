# -*- coding: utf-8 -*-
from node import *

class LinkedList:

   def __init__(self,head = None):
       self.head = head


   def addNode(self, data):
       newNode = Node(data,self.head)
       self.head = newNode
       return True

   def reverse(self):
       curr = self.head
       lList = LinkedList()
       while curr:
           lList.addNode(getattr(curr, 'data', 'empty'))
           curr = getattr(curr, 'nextNode', 'None')
       return lList;
       
   def printNode(self):
       curr = self.head
       while curr:
           print(getattr(curr, 'data', 'empty'))
           curr = getattr(curr, 'nextNode', 'None')

   def reverseAfter(self, val):
       curr = self.head
       lList = LinkedList()
       # First run
       while curr:
           lList.addNode(getattr(curr, 'data', 'empty'))
           if getattr(curr, 'data', 'empty') == val:
               lList = lList.reverse()
           curr = getattr(curr, 'nextNode', 'None')
       return lList
           
myList = LinkedList()
print("Entre simbol by one")
while 1:
    value = raw_input("")
    value = value.rstrip("\r")
    if value:
        myList.addNode(value)
    else:
        break;
print("Entre HEAD of reverse")
value = raw_input("")
value = value.rstrip("\r")
print("----Result----")
myList = myList.reverseAfter(value)
myList.printNode()
raw_input("Enter for close")
