# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:12:54 2020

@author: SOBIHA
"""
import os,re
path = ('C:\\Users\\SOBIHA\\Desktop\\Training\\pythonBasics\\input.txt')
f = open(path)
max = int(input("Enter max value"))
min = int(input("Enter min value"))
sentences = []
for line in f:
    sen = re.split(r'(?<=\.|\!|\?) ', line.strip())
    sentences+=sen
    
for i in sentences:
    if(min<= (len(i)+1) <=max):
        print(i)