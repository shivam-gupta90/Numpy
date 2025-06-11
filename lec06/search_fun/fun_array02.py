#SUFFLE function

import numpy as np
var = np.array([1,2,3,4,5])
np.random.shuffle(var)
print(var)

#output : [3 5 2 1 4]
print()
print()

'''--UNIQUE FUNCTION--'''

var1 = np.array([1,2,3,4,2,3,4,5,6,7])
x = np.unique(var1,return_index = True,return_counts = True)
print(x)
#output :(array([1, 2, 3, 4, 5, 6, 7]), array([0, 1, 2, 3, 7, 8, 9]), array([1, 2, 2, 2, 1, 1, 1]))
#  it give the unique element in array as well as his index and also his count
print()
print()

'''--RESIZE FUNCTION--'''

var2 = np.array([1,2,3,4,5,6])
x1 = np.resize(var2,(2,3))
print(x1)
#output : 
#[[1 2 3]
 #[4 5 6]]
print()
'''--FLATTEN AND RAVEL--''' 
#it convert the 2 array into 1D array

var3 = np.array([1,2,3,4,5,6])
x2 = np.resize(var3,(2,3))
print(x2)
print()
print("flatten :",x2.flatten(order= "F"))
print("flatten :",x2.flatten(order= "A"))
print("flatten :",x2.flatten(order= "C"))
print("reval :",np.ravel(x2,order= "A"))