# -*- coding: utf-8 -*-
from node import *

class LinkedList:

   def __init__(self,head = None):
       self.head = head

   def addNode(self, p_data):
       lv_node = Node(p_data,self.head)
       self.head = lv_node
       return True

   def reverse(self):
       lv_curr = self.head
       lv_list = LinkedList()
       while lv_curr:
           lv_list.addNode(getattr(lv_curr, 'data', 'empty'))
           lv_curr = getattr(lv_curr, 'nextNode', 'None')
       return lv_list;
       
   def printNode(self):
       lv_curr = self.head
       while lv_curr:
           print(getattr(lv_curr, 'data', 'empty'))
           lv_curr = getattr(lv_curr, 'nextNode', 'None')

   def reverseAfter(self, p_val):
       lv_curr = self.head
       lv_list = LinkedList()
       # First run
       while lv_curr:
           lv_list.addNode(getattr(lv_curr, 'data', 'empty'))
           if getattr(lv_curr, 'data', 'empty') == p_val:
               lv_list = lv_list.reverse()
           lv_curr = getattr(lv_curr, 'nextNode', 'None')
       return lv_list


# Runing 
gv_list = LinkedList()
print("Entre simbol by one")
while 1:
    lv_value = raw_input("")
    lv_value = lv_value.rstrip("\r")
    if lv_value:
        gv_list.addNode(lv_value)
    else:
        break;
print("Entre HEAD of reverse")
gv_value = raw_input("")
gv_value = gv_value.rstrip("\r")
print("----Result----")
gv_list = gv_list.reverseAfter(gv_value)
gv_list.printNode()
raw_input("Enter for close")
