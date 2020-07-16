# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:46:41 2020

@author: SOBIHA
"""


ones = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ",
		 "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ",
		 "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ",
		 "Seventeen ", "Eighteen ", "Nineteen "]
    
tens = ['','', "Twenty ", "Thirty ", "Forty ", "Fifty ",
		 "Sixty ", "Seventy ", "Eighty ", "Ninety "]

path = ('C:\\Users\\SOBIHA\\Desktop\\Training\\pythonBasics\\num.txt')


def convert(num, suffix):
        if num==0:
            return ''
        if(num>19):
            return tens[num//10] + ones[num%10] + suffix
        else:
            return ones[num] + suffix
        
class Numbers:
    
    nbr=0
    def __init__(self):
        
        f = open(path)
        try:
            self.nbr = int(f.readline().strip())
        except: 
            print("Please enter valid number in file!")
    def getNumber(self):
        return self.nbr
        
        

class Words:
    
    def __init__(self,n=0,word=""):
        self.n = n
        self.word = word  
    
    def toFile(self):
        f = open(path, "w") #overwriting file content(number to word)
        f.write(self.word)
        print("Number written in file succesfully!")
        f.close()   
        
    def toWords(self):
        res = convert((self.n//10000000000)%100, "Billion")
        res += convert((self.n // 10000000) % 100, "Crore, ")
        res += convert(((self.n // 100000) % 100), "Lakh, ")
        res += convert(((self.n // 1000) % 100), "Thousand ")
        res += convert(((self.n // 100) % 10), "Hundred ")
        if self.n > 100 and self.n % 100:
            res += "and "
        res += convert((self.n % 100), "")
        self.word = res
        self.toFile()
        
 

num_obj = Numbers()
if(num_obj.getNumber()!=0):
    word_obj = Words(num_obj.getNumber())
    word_obj.toWords()
    
        
        