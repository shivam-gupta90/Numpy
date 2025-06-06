'''---Special type of Array--'''

#Array filled with zero's
import numpy as np

arr_zero = np.zeros(4)
arr_zero1 = np.zeros((3,4))

print(arr_zero)
print()
print(arr_zero1)


#Array filled with one's
arr_one = np.ones(4)
print(arr_one)

#Array filled with Empty
arr_em =np.empty(4)
print(arr_em)

# An array with range of element

ar_rn = np.arange(4)
print(ar_rn)


# Array Diagonal element filled with 1's
dia = np.eye(3)
dia1 = np.eye(5,5)

print(dia)
print(dia1)

# Linspace array
arr_line = np.linspace(0,20,num=5)
print(arr_line)