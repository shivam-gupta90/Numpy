import numpy as np
var = np.array([1,2,3,4,5,6,3,2,1,2,3,4])
x = np.where(var == 2)     # it give the index value of 2 where it is switched in np.array 
print(x)

#output : (array([1, 7, 9]),)

x1 = np.where(var/2 ==0)
print(x1)

#output : (array([], dtype=int64),) it give empty array because remminderr is not eqaula to zero

x2 = np.where(var%2 ==0 )
print(x2)

#output :(array([ 1,  3,  5,  7,  9, 11]),)

'''-- second fuction is SEARCH SHORTED ARRAY--'''

'''--which perform a binary search in the array 
      and return the index where the  specified value would be insert 
      to maintane the search order--'''

var2 = np.array([1,2,3,4,6,7,8])
x2 = np.searchsorted(var2,5)
print(x2)

#output : 4 because at 4 index 5 is place in order

'''-- We can also palced the value from right and left--'''
var3 = np .array([1,2,3,4,5,7,8,9])
x3 = np.searchsorted(var3,6,side ="left")
print(x3)
#output : 5

var4 = np .array([1,2,3,4,5,7,8,9])
x4 = np.searchsorted(var3,[5,6,7],side ="right")
print(x4)

'''-- and the 3rd is SORT ARRAY--'''

'''--order sequencce is any sequence that on order correspoinding 
      to element like numeeric or alphabetical ascending or descending--'''
var5 = np.array([1,2,3,22,21,14,45,4])
print(np.sort(var5))

#for 2D

var6 = np.array([[1,2,4,3],[8,6,5,7]])
print(np.sort(var2))

#we can also make a sort in string

var7 = np.array(["s","h","i","v","a","m"])
print(np.sort(var7))
#output :['a' 'h' 'i' 'm' 's' 'v']

'''-- And the 3 is FILTER ARRAY--'''

'''--Getiing some element of an existing array and 
     creatinng new array out of them--'''
var8 = np.array(["s","h","i","v"])
f = [True,False,True,False]
new_arr = var8[f]
print(new_arr)

#output :['s' 'i']
