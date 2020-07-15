# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:52:33 2020

@author: SOBIHA
"""
import math 
num = [12,2,4,8,16,8,16,36,81,25,4,8,16,25,31,28,29,16,4,2,4,1,9,3,2,5,4,16,49,50,25,60,34,4,50,25,9]

def checkPerfSquare(n):
    sq = math.sqrt(n) 
    return ((sq - math.floor(sq)) == 0) 

res = list(map(checkPerfSquare,num))
c =1
for i in range(len(num)):
    if(res[i] and c <=20):
        print(num[i],end=" ")
        c+=1

        
    
