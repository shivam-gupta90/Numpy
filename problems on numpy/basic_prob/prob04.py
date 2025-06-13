#  Create a 5×5 matrix with values from 1 to 25.
import numpy as np

matrix = np.arange(1,26)   
print(matrix)

var = matrix.reshape(5,5)
print(var)


'''-- in this problem first we use arange function to print the elements from 
    1 to 25 . then we reshape the element into 5*5 matrix--'''