# Creating an array
# 1. Assign it to a variable
# 2. Define type of elements
# 3. Define its size
# NB: Import array module for python 

from array import *
arr1 = array("i",[1,2,3,4,5,6])
arr2 = array("d",[1,2, 3.5, 5.6])
print(arr1)

# Insertion
arr1.insert(6, 7)
arr1.insert(2,8)
print(arr1)

# Traversing an array
def traverseArray(array):
    for element in array:
        print(element)
        
traverseArray(arr1)

# Accessing an element
def accessElement(array, index):
    if index >= len(array):
        print("There is no element in this index!")
    else:
        print(array[index])

accessElement(arr1, 4)

#finding/searching an element
def searchArray(array,value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The element does not exist in this array!"

print(searchArray(arr1, 9))