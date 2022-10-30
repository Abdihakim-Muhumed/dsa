# 1. Creating an array
from array import *
from multiprocessing.dummy import Array
my_array = array("i",[1,2,3,4,5,6])

for i in my_array:
    print(i)
    
# 2. Aceesing individual element
print("Step 2")
print(my_array[1])

# 3. Append to the array
print("Step 3")
my_array.append(6)
print(my_array)

# 4. Using insert method to insert a value
print("Step 4")
my_array.insert(0, 11)
print(my_array)

# 5. Extend python array with extend method
print("Step 5")
my_array1 = Array('i', [10,11,12])
my_array.extend(my_array1)
print(my_array)

# 6. Add item from list to array using fromList
print("Step 5")
tempList = [20,30,40]
my_array.fromlist(tempList)
print(my_array)

