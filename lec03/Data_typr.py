'''--Data type in numpy--'''
import numpy as np

var = np.array([1,2,3,4,34,23])
print("Data type : ",var.dtype)

#output = int64

var1 = np.array([2.1,3.4,6.5])
print("Data type: ",var1.dtype)

#output = float64

var2 = np.array(["s","h","d","k"])
print("Data type: ",var2.dtype)

#output = <ui


var3 = np.array(["s","h","d","k",2,3,4])
print("Data type: ",var3.dtype)

# output = <21

'''--To convert into another datatype--'''

x = np.array([1,2,3,4],dtype = np.int8)
print("Data type: ",x.dtype)

#output = int8

'''--another way to convert--'''

x =np.array([1,2,3,4], dtype = "f")
print("Data type: ",x.dtype)

#output = float64