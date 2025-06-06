import numpy as np

''' ---this is 1D array---'''
x = [1,2,3,4,]

y = np.array(x)

print(y)
print(type(y))  #it print the type 
print(y.ndim)


''' ---this is 2D array---'''
arr2 = np.array([[1,2,3,4],[1,2,3,4]])

print(arr2)
print(arr2.ndim)



''' ---this is 3D array---'''
arr3 = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(arr3)
print(arr3.ndim)



''' ---this is Multi-Dimension Array---'''
arn = np.array([1,2,3,4],ndmin =10)
print(arn)
print(arn.ndim)