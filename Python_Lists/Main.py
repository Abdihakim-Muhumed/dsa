# Created by Abdihakim Muhumed
# A list is a data structure that holds an ordered collection of items

# Creating a list
integers = [1,2,3,4]
print(integers)
strings = ['milk', 'cheese', 'butter']
print(strings)

# Accessing / Traversing the list
shoppingList = ['milk', 'cheese', 'butter']
print('First Item: '+ shoppingList[0])
print('Last Item: ' + shoppingList[-1])

# Traversing
for item in shoppingList:
    print(item)
for i in range(len(shoppingList)):
    print(i,'. ' + shoppingList[i])
    

#update/insert a list
myList = [1,2,3,4,5,6,7]
print(myList)
myList[2] = 33 # updating
myList.insert(0, 11) # inserting
print(myList)

# Slicing, Deleting in a list
myList = ['a', 'v', 'b','c', 'd', 'e']
print(myList[0:2]) #slicing
#myList.pop(1)
#del myList[3] 
#del myList[2:4]
myList.remove('e')
print(myList)
