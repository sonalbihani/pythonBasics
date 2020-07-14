# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:14:56 2020

@author: SOBIHA
"""
#Sort the list
l1 = [3, 1, 4, 2, 5] 
l_sorted = []
while l1:
    mini = l1[0]
    for j in l1:
        if(j<mini):
            mini = j
    l_sorted.append(mini)
    l1.remove(mini)
print(l_sorted)
    
#print the squares of all the number in the list
l2 = [3, 1, 4, 2, 5] 

print([a**2 for a in l2])

l3 = [
 (105, "d"),
 (21, "z"),
 (0, "v")
] 
#print all the elements in the list 
for a,b in l3:
    print(a,b,end=" ") 
print()


l = [
 {
 "color": "red",
 "value": "#f00"
 },
 {
 "color": "green",
 "value": "#0f0" 
 },
 {
 "color": "blue",
 "value": "#00f"
 }
] 

#Print all the value in the list 
print([i["value"] for i in l])
#print the hex value of green
print([i["value"] for i in l if(i["color"]=="green")])
#print the hex codes of all colors 
for i in l:
    print("Colour:",i["color"], "Hexcode:", i["value"])


#Print the languages that are inferior to Python
py = {'Python': 'Rocks', 'inferior': ['java', 'cobol']} 
print(py["inferior"])


prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
 'apple': 1,
 'banana': 6} 

#Print my Bill 
print("my Bill:", str(sum([my_purchase[item]*values for item,values in prices.items()])))


junk = { 
        "characters": {
            "Lonestar": {
                "id": 55923,
                "role": "renegade",
                "items": ["space winnebago","leather jacket"]
                },
            "Barfolomew": {
                "id": 55924,
                "role": "mawg",
                "items": ["peanut butter jar","waggy tail"]
                },
            "Dark Helmet": {
                "id": 99999,
                "role": "Good is dumb",
                "items": ["Shwartz","helmet"]
                },
            "Skroob": {
                "id": 12345,
                "role": "Spaceballs CEO", 
                "items": ["luggage"]
                }
            }
        }
#print the items
print([junk["characters"][i]["items"] for i in junk["characters"].keys()])
#print the roles 
print([junk["characters"][i]["role"] for i in junk["characters"].keys()])


omg = {2: [1, 2, 3], 'a': {'b': {'c': {'d': {'e': [1, 2, 3]}}}}} 
#Get the first array value for the key 2
print(omg[2][0])
#Print all the array value for the key 2
print(omg[2])
#Print value of key 'a','b','c','d','e'
print(omg['a']['b']['c']['d']['e'])
#Print the sum of the array with key 'e'
print(sum(omg['a']['b']['c']['d']['e']))
#set value of key 'e' to ['Chera','Chola','Pandiya']
omg['a']['b']['c']['d']['e'] =  ['Chera','Chola','Pandiya']
print(omg['a']['b']['c']['d']['e']) 



body = {
 'query': {
     'filtered': {
         'query': {
             'match': {'description': 'addictive'}
             },
         'filter': {
             'term': {'created_by': 'Mats'} 
             }
         }
     }
 }
#Get the value Mats from the Dict 
print(body['query']['filtered']['filter']['term']['created_by'])
#Modify the below statement to print Mats
#print(body["query"]['filtered']['filter']) 
print(body['query']['filtered']['filter']['term']['created_by']) 

movie_box = {
    "Robin Hood: Men in Tights": {
        "imdb_stars": 6.7,
        "length": 104,
        "stars": [ 
            {"name": "Cary Elwes", "imdb": "nm0000144", "role": "Robin Hood"},
            {"name": "Richard Lewis", "imdb": "nm0507659", "role": "Prince John"} 
                  ]
        }
    } 
# print the IMDB star rating ( 6.7)
print(movie_box["Robin Hood: Men in Tights"]["imdb_stars"])
# print the length of the movie 
print(movie_box["Robin Hood: Men in Tights"]["length"])

