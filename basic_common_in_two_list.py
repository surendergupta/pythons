import numpy as np
listA = [1, 2, 3, 4, 5]
listB = [5, 2, 6, 3, 9]

# using sets 
print("Common in two  List : ", (set(listA) & set(listB)))

# using numpy interset
print("Common using interset in numpy : ", np.intersect1d(listA, listB))
