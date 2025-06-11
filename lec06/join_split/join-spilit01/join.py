'''--Joining means putting content of two or more arrays in a single array--'''
import numpy as np

var = np.array([1,2,3,4])
var1 = np.array([5,6,7,8])

ad = np.concatenate((var,var1))
print(ad)

'''-- We can also add along the axis=0 and 1 in 2D array--'''
var3 = np.array([[1,2],[3,4]])
var4 = np.array([[5,6],[7,8]])

ar_new = np.concatenate((var3,var4),axis =1)
print(ar_new)


# Along axis =0
var5 = np.array([[1,2],[3,4]])
var6 = np.array([[5,6],[7,8]])

ar_new = np.concatenate((var5,var6),axis =0)
print(ar_new)