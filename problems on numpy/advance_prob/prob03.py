#  Sort a 2D array by the second column.
import numpy as np

arr = np.array([[3,2,7],[9,5,7,],[5,1,9]])
print(arr)

# Sort by second column (column index 1)
sorted_arr = arr[arr[:, 1].argsort()]

print("Sorted by 2nd column:\n", sorted_arr)





'''--✅ arr[:, 1] selects the second column.
✅ .argsort() returns the index order to sort that column.
✅ arr[...] reorders the whole rows based on that index.--'''