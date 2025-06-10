import numpy as np
var =np.array([1,2,3,4])
co = var.copy()

print("var :",var)
print("copy :",co)

print()  # just for extra gap
print()

#if we change in original value it didnot effect the copy array

var1 =np.array([1,2,3,4])
co = var1.copy()
var1[0] = 40

print("var :",var1)
print("copy :",co)

print()
print()

'''-- view in numpy array --'''
var2 = np.array([9,2,3,4,5])
vi = var2.view()
print("var2 :",var2)
print("view :",vi)

print()
print()
#if we make a change in original array the change is aslo seem in view array

var3= np.array([9,2,3,4,5])
vi = var3.view()
var3[3] = 50
print("var2 :",var3)
print("view :",vi)