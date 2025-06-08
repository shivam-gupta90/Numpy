'''--Boardcasting Numpy array--'''
import numpy as np
var = np.array([1,2,3])      #(1,3)
print(var.shape)
print()
print(var)
print()

var1 = np.array([[1],[2],[3]])    #Here we are creating (3,1) matrix
print(var1.shape)
print()
print(var1)
print()
print(var + var1)
#print(np.add(var,var1))    we use also this to print the result