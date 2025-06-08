import numpy as np
var =np.array([4,4,3,6,8,1,2,9])
print("min : ",np.min(var))
print("max : ",np.max(var))
print("sqrt : ",np.sqrt(var))


var1 = np.array([[2,1,3],[9,8,7]])
print(np.min(var1,axis = 0))   #axis =0 coloum , axis =1 row


print()

'''--To find the vale of sin--'''
var2 = np.array([1,2,3])
print(np.sin(var2))

'''--using of cumsum--'''
var3 = np.array([1,2,3,4])
print(np.cumsum(var3))