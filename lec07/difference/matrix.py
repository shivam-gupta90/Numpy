'''--Where is the only difference between in multiplication--'''
import numpy as np
var = np.matrix([[1,2,3],[1,2,3]])
print(var)
print(type(var))
print()
#output :[[1 2 3]
#         [1 2 3]]
 #       <class 'numpy.matrix'>

var1 = np.array([[1,2,3],[1,2,3]])
print(var1)
print(type(var1)) 
print()
#output: [[1 2 3]
     #    [1 2 3]]
    #     <class 'numpy.ndarray'>


'''--DOT function --'''
var2 = np.matrix([[1,2],[1,2]])
var3 = np.matrix([[1,2],[1,2]])
print(var2.dot(var3))

#output :[[3 6]
      #  [3 6]] this is right answer

