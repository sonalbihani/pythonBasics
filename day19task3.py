# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:45:22 2020

@author: SOBIHA
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self,head=None):
        self.head = None

    def pushNode(self, nd): 
        node_new = Node(nd) 
        node_new.next = self.head 
        self.head = node_new
    def printList(self): 
        temp = self.head
        print("List: ",end=" ")
        while(temp): 
            print(temp.data,end=" ")
            temp = temp.next
        print()
        
    def reverseList(self): 
        prev = None
        curr = self.head 
        while(curr is not None): 
            nxt = curr.next
            curr.next = prev 
            prev = curr 
            curr = nxt
        self.head = prev 
        
        self.printList()
s=""
l = LinkedList()
while(s!="-1"):
    print("Choose between the options:\n 1.Add data to list\n 2.Print List\n 3.Reverse List\n Press -1 to quit")
    s = input()
    if(s=="1"):
        n = int(input("Enter data to add"))
        l.pushNode(n)
    elif s=="2":
        l.printList()
    elif s =="3":
        l.reverseList()
          
    
    