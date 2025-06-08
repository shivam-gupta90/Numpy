'''---shape and reshape in numpy Array--'''

import numpy as np

var = np.array([[1,2,3,4],[1,2,3,4]])
print(var.shape)   #.shape is used to know the shape of array

#output = (2,4) wher 2 row and 4 coloum

var1 = np.array([1,2,3,4],ndmin = 4)

print(var1)
print(var1.ndim)
print()
print(var1.shape)


'''--Reshapeing--'''
var3 = np.array(([1,2,3,4,5,6]))
print(var3)
print(var3.ndim)
print()

x = var3.reshape(3,2)
print(x)
print(x.ndim)


'''--For multidimension aarray--'''
var4 = np.array([1,2,3,4,5,6,7,8,9,10,11,2])
print(var4)
print(var4.ndim)
print()

x = var4.reshape(2,3,2)
print(x)
print(x.ndim)

'''--To convert into multi to one dimension--'''
var5 = np.array([1,2,3,4,5,6,7,8,9,10,11,2])
print(var5)
print(var5.ndim)
print()

x = var5.reshape(2,3,2)
print(x)
print(x.ndim)

one = x.reshape(-1)
print(one)
print(one.ndim)