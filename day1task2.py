# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:37:13 2020

@author: SOBIHA
"""

s = input();
dict ={'I':1,'V':5,'X': 10, 'L':50, 'C': 100, 'D':500, 'M': 1000}
l = len(s)
val = 0
i=0
while(i<l):
    if((i+1)<l and dict[s[i]]<dict[s[i+1]]):
        val+= dict[s[i+1]]-dict[s[i]]
        i+=2
    else:
        val+=dict[s[i]]
        i+=1
print(val)