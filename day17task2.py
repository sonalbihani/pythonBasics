# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:14:20 2020

@author: SOBIHA
"""


"""Write a function called is sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. You can assume (as a
precondition) that the elements of the list can be compared with the relational
operators <, >, etc.
For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should
return False """

l = ['v','a','b']
def is_sorted(l):
    for i in range(len(l)-1):
        if(l[i]<=l[i+1]):
            continue
        else:
            return False
    return True
print(is_sorted(l))
    