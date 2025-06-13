# . Replace all odd numbers in an array with -1.
import numpy as np

arr =np.array([1,2,3,4,5,6,7,8])
arr[arr %2 == 1] = -1
print("Modified array :",arr)


'''
arr % 2 == 1: finds odd numbers.

arr[...] = -1: replaces those values with -1'''