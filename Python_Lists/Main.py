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