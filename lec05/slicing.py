import numpy as np


var1 = ([1,2,3,4,5,6,7,8])
print(var1)
print("2 to 5 :",var1[1:5])
print("2 to End :", var1[1:])


'''For 2D slicing--'''
var = np .array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(var)
print()
print(var[0,0:3])
print(var[1,0:5])
print(var[2,0:2])