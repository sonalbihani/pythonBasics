# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:07:23 2020

@author: SOBIHA
"""

list = [1,4,52,4]

#for loop
sum = 0
for i in list:
    sum+=i
print("Using for loop: ",sum)

#while loop
sum =0
i=0
while i<len(list):
    sum+=list[i]
    i+=1
print("Using while loop: ",sum)

#recursion
def sum_arr(arr,n):
   if (n == 0):
     return 0
   else:
     return arr[n-1] + sum_arr(arr,n-1)
print("Using recursion: ",sum_arr(list,len(list)))
