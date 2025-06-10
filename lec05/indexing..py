import numpy as np
var =np.array([1,2,3,4,5,6,7])
#indexing      0,1,2,3,4,5,6
 #            -7,-6,-5,-4,-3,-2,-1
print(var)
print("1 to end :",var[1:])
print("start to 8 :",var[:8])
print("start to 5 :",var[0:5])
print("stop :",var[0:7:2])

'''-- Indexing in 2D Array--'''
var1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(var1)
print()
print(var1[1,0,])


'''--Indexing for 3D--'''
var2 = np.array([[[1,2],[6,7]]])
print(var2)
print(var2.ndim)
print()
print(var2[0,1,0])