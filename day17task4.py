# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:31:39 2020

@author: SOBIHA
"""

"""Write a program that finds all of the metathesis pairs in the dictionary. Two
words form a “metathesis pair” if you can transform one into the other by
swapping two letters; for example, “converse” and “conserve.”
Hint: don’t test all pairs of words, and don’t test all possibleswaps. """

def find_anagrams(words):
    anag_dict ={}
    for w in words:
        if(isSorted(w)) not in anag_dict:
            anag_dict[isSorted(w)] = [w]
        else:
            anag_dict[isSorted(w)].append(w)
    return anag_dict
            
def find_pairs(anag_dict):
    for sorted_word,list_anag in tuple(anag_dict.items()):
        if(len(list_anag)<2):
            continue
        else:
            for i in range(len(list_anag)):
                w1 = list_anag[i]
                for w2 in list_anag[i+1:]:
                    if(check_metathesis(w1,w2)):
                        print(w1,w2)
                
            
def check_metathesis(word1, word2):
    if(word1 == word2):
        return False
    else:
        count=0
        for w1,w2 in zip(word1,word2):
            if(w1!=w2):
                count+=1
        if(count==2):
            return True
    return False

def isSorted(word):
    list_sorted = sorted(word)
    return "".join(list_sorted)

words = ['conserve','converse','coonvrs','aab','aba','a','a','ab','ba']
anag_dict = find_anagrams(words)
find_pairs(anag_dict)
