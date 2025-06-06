'''---creating Numpy with Random number---'''
#rand() 
'''--this function is used to generate random number between 0 to 1--'''

import numpy as np
var = np.random.rand(4)
var1 = np.random.rand(4,3)
print(var)
print()
print(var1)


#randn()
'''--this function is used to genrate a random value close to zero . this may return positive and negative number
as well--'''

var2 = np.random.randn(4)
print(var2)

#ranf()
'''--this function for doing sampling in numpy.it return an array of specified space and fil it with
random float in th half open interval  [0.0,1.0)--'''
var3 = np.random.ranf(4)
print(var3)


#randintt()
'''--the function is used to generate a random number between given range'''

var4 = np.random.randint(5,20,5)
print(var4)