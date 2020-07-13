# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:34:42 2020

@author: SOBIHA
"""


tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']] 
for l in tableData:
    for item in l:
        print(item.rjust(10), end=" ")
    print()

