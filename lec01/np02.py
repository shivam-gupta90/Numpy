#taking array as a input
import numpy as np

l = []
for i in range(1,5):
    int_1 = int(input("Enter the number :"))
    l.append(int_1)

print(np.array(l))  
