# it is a dictionary where make key and value
letter={
    "name":"neha",
     "standard":"high",
      "attitute":"high",
       "marks":[1,2,3,4]}
print(letter["name"])
print(letter["marks"])
letter["marks"]=[45,78]
print(letter["marks"])
 # nesting in dictinary
'''letter={
    "name":"neha",
     "standard":"high",
      "attitute":"high",
    "anotherdictionary":{"books":"social study"}}
print(letter["anotherdictionary"]["books"])'''

myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A Coder",
    "Marks": [1, 2, 5],
    "anotherdict": {'harry': 'Player'}
}

# print(myDict['Fast'])
# print(myDict['Harry'])
myDict['Marks'] = [55, 88]
print(myDict['Marks'])
print(myDict['anotherdict']['harry']) 
