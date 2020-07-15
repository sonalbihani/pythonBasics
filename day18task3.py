# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:15:05 2020

@author: SOBIHA
"""


sen = "The dog is over the dog the dog fence"
import math

def isSeq(a,b):
    if(ord(a)<ord(b)):
        return True
    return False

 
s = sen.replace(" ","").lower()
    
dictionary = {}
for i in range(len(s)-1):
    dict_key = s[i]+s[i+1]
    if(dict_key in dictionary.keys()):
        dictionary[dict_key]+=1
    else:
        dictionary[dict_key] = 1
total = sum(list(dictionary.values()))
fin = {k:round((float(v)/float(total))*100,2) for k,v in sorted(dictionary.items(),key = lambda item: item[1],reverse=True)[:5]}
print(fin)
for k,v in fin.items():
    print(k,": ",v,"%")
