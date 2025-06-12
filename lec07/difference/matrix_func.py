'''--TRANSPOSE--'--swapaxces--'''
import numpy as np
var = np.array([[1,2,3],[3,4,5]])
print(var)
print()
print(np.transpose(var))
print()
print(np.swapaxes(var,0,1))    # we  can also write as np.T to find the transpose
print()
'''output : [[1 2 3]
             [3 4 5]]

[[1 3]
 [2 4]
 [3 5]]'''

# INVERSE
var2 = np.array([[1,2],[3,4]])
print(var2)
print(np.linalg.inv(var2))
print()

'''--it find the inverse of matrix  [[-2.   1. ]
                                     [ 1.5 -0.5]]'''

# POWER
var3 = np.matrix([[1,2],[3,4]])
print(np.linalg.matrix_power(var3,2))
print(np.linalg.matrix_power(var3,0))
print(np.linalg.matrix_power(var3,-2))
#output ;[[ 7 10]
  #        [15 22]]

       #    [[1 0]
      #     [0 1]]

     #   [[ 5.5  -2.5 ]
    #    [-3.75  1.75]]

    #DETERMINT

var4 = np.matrix([[1,2],[3,4]])
print(np.linalg.det(var4))    
#output :-2.0000000000000004