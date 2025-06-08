import numpy as np

var = np.array([1,2,3,4])
varadd = var +3    # it add 3 in each element of array
print(varadd)

#output [4 5 6 7]

'''--To add two array'''
var1 = np.array([1,2,3,4])
var2 = np.array([1,2,3,4])

varadd = var1 + var2
print(varadd)
#output = [2 4 6 8]

'''--To add 2D Array--'''
var21 = np.array([[1,2,3,4],[1,2,3,4]])
var22 = np.array([[2,3,4,1],[5,4,3,2]])

varadd = np.add(var21,var22)
print(varadd)

# We can also substract
subs = np.subtract(var21,var22)