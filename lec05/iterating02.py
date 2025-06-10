'''--Here we gonig to know about the iterating in numpy array--'''
import numpy as np

var = np.array([1,2,3,4,5,6,7])

print(var)
print(var.ndim)   #dimensio of array
print() #for extra gap in output
for i in var:
    print(i)


'''-- For 2D --'''    

var1 = np.array([[1,2,3,4],[5,6,7,8]])

print(var1)
print(var1.ndim)   #dimensio of array
print() #for extra gap in output
for k in var1:
    for l in k:
        print(l)


print()
print()
'''-- For 3D --'''
var2 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(var2)
print()
print(var2.ndim)
print()

for a in var2:
    for j in a:
        for p in j:
            print(p)

'''-- By using the fuction--''' 
var3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(var3)
print()
for i in np.nditer(var3):
    print(i)           


'''-- We can also print the indexing number of array--'''

var4 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(var4)
print()
for i,d in np.ndenumerate(var4):
    print(i,d)