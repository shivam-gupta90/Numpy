# 3. Create an array of 10 random floats between 0 and 1
import numpy as np
var = np.random.rand(10)
print(var)

''' ten random valye lies between 0 and 1 ten : [0.34867314 0.96665011 0.29876852 0.93272887 0.5754291 
                                                0.22031726  0.41568208 0.17957983 0.67176204 0.21101124]'''



# there is two way to count his index number also
'''import numpy as np

var = np.random.rand(10)

for index, value in enumerate(var):
    print(f"Index {index}: Value {value}")

Index 0: Value 0.32569834
Index 1: Value 0.94623645
Index 2: Value 0.18590256
...
Index 9: Value 0.68231701 '''


import numpy as np

var = np.random.rand(10)

for i in range(len(var)):
    print(f"Index {i}: Value {var[i]}")
