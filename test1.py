from numpy import *
a = array([array([i for i in range (1, 11)]) * j for j in range (1, 11)])
print(a)
b = a[[1, 3], ]
c = a[2, ]
print("\n\n",b, "\n\n", c, "\n\n")
print(a/c)