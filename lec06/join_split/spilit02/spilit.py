'''--split break one array into multiple--'''
import numpy as np
var = np.array([1,2,3,4,5,6])
print(var)

ar = np.array_split(var,3)
print(ar)
print(type(ar))
print(var[0])

'''output is : [1 2 3 4 5 6]
[array([1, 2]), array([3, 4]), array([5, 6])]
<class 'list'>
1   '''
print()
print()
# For 2D

var1 = np.array([[1,2],[3,4],[5,6]])
print(var1)

ar1 = np.array_split(var,3)
ar2 = np.array_split(var1,3,axis = 1)
print(ar1)
print()
print(ar2)