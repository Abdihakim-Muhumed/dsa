# Created by Abdihakim Muhumedon 30/10/2022
# Copyright @ 2022 Abdihakim. All rights reserved.

# Two Dimensional Array
""" Day 1 - 11, 15, 10, 6
    Day 2 - 10, 14, 11, 5
    Day 3 - 12, 17, 12, 8
    Day 4 - 15, 18, 14, 9
"""
import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

# Inserting -  Two Dimensional Array
newTwoDArray = np.insert(twoDArray, 1,[[1,2,3,4]], axis=1)
print(newTwoDArray)

# Accessing an element of a 2D array
print(newTwoDArray[0][1])

# Traversing 2D array
def traverseTwoDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverseTwoDArray(newTwoDArray)