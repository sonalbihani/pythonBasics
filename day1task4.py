# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:36:28 2020

@author: SOBIHA
"""
def formatList(a):
    l = len(a)
    if(l==0):
        print('Empty list!')
    elif (l==1):
        print(a[0])
    else:
        s= a[0]
        for i in range(1,l-1):
            s+=(", "+ a[i])
        s+=" and " + a[l-1]
        print(s)

formatList(["hi"])

