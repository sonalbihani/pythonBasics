# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:24:02 2020

@author: SOBIHA
"""


"""Write a program that finds all the reverse pairs in the word list. Two words are a
“reverse pair” if each is the reverse of the other. """

words = ['god','cat','dog','tac','god','zap','cat','tac']

def check_rev(words):
    for i in words:
        if(i[::-1] in words):
            print(i,i[::-1])
            words.remove(i)
            words.remove(i[::-1])
check_rev(words)