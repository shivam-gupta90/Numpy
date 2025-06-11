import numpy as np
var = np.array([1,2,3,4])
print(var)
v = np.insert(var,4,60)
print(v)
#output :[ 1  2  3  4 60] it insert the value in array

'''--IN 2D array--'''
var1 = np.array([[1,2,3,4],[5,6,7,8]])
v1 = np.insert(var1,2,9,axis =1)
print(v1)
#output : [[1 2 9 3 4]
         # [5 6 9 7 8]]

var2 = np.array([[1,2,3,4],[5,6,7,8]])
v2 = np.insert(var2,2,9)
print(v2)    
#output :[1 2 9 3 4 5 6 7 8]
print()

'''--FOR MULTIPLE DATA__'''
v3 = np.insert(var2,2,[22,23],axis =1)
print(v3)
#output :[[ 1  2 22  3  4]
         #[ 5  6 23  7  8]]