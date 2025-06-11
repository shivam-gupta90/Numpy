import numpy as np

var = np.array([1,2,3,4])
var1 = np.array([5,6,7,8])

ad = np.stack((var,var1))
print(ad)


'''--We also have 3 type of stack use--'''

#First
ad1 = np.hstack((var,var1))   # h means row

#sencond
ad2 = np.vstack((var,var1)) # v means coloum

#third is 
ad3 = np.dstack((var,var1)) # d for height

print(ad1,ad2,ad3)