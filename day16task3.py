# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:04:57 2020

@author: SOBIHA
"""

s = int(input())
m = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
d = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
if(s not in d.keys()):
    print("Error")
else:
    print(m[s] + " has " + str(d[s]) +" days." )