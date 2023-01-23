import numpy
stu_roll = numpy.array([10, 20, 30, 40, 40, 50])
print(stu_roll)
print(type(stu_roll))
print(stu_roll.dtype)

stu_roll[1] = 500
print(stu_roll)

# Accessing array using for loop

import numpy
stu_roll1 = numpy.array([101, 102, 103, 104, 105])
for element in stu_roll1:
    print(element)

# Accessing array using for loop with index

stu_roll2 = numpy.array([101, 102, 103, 104, 105])
n = len(stu_roll2)
for i in range(n):
    print(i, "=",  stu_roll2[i])

# Zeros function default float value
from numpy import *
a = zeros(5)
n = len(a)
for i in range(n):
    print('index', i, '=', a[i])

# ones function default float value
from numpy import *
one = ones(5)
n = len(one)
for i in range(n):
    print(one[i])

# arange function

from numpy import *
a = arange(5, 20, 2)
n = len(a)
for i in range(n):
    print("index", i, "=", a[i])


from numpy import *
k = array([101, 102, 103, 104, 105])
A = k -5
for i in A:
    print(i)

from numpy import *
k = array([101, 102, 103, 104, 105])
l = array([10, 200, 15, 120, 25])
result = where(k>l, k, l)
print(result)

"""Getting input in numpy one dimensional array
from user for loop"""

from numpy import *
n = int(input("Enter no. of elements: "))
a = zeros(n, dtype=int)
n = len(a)
print((a))
for i in range(n):
    x = int(input("Enter elements: "))
    a[i] = x

print(a)

for i in range(n):
    print(i, "=", a[i])


"""Getting input in numpy one dimensional array 
from user using while loop"""

from numpy import *
n = int(input("Enter no. of elements: "))
z = zeros(n, dtype=int)
n = len(z)

print(z)

i = 0
j = 0
while i < n:
    x = int(input("Enter elements: "))
    z[i] = x
    i += 1

print(z)

while j < len(z):
    print(z[j])
    j += 1



"""Multi-Dimensional Array"""

from numpy import *
a = array([[10, 20, 30, 40], [50, 60, 70, 80]])
n = len(a)

for c in range(n):
    for r in range(len(a[c])):
        print(a[c][r])
    print()

"""Multi- D array using zeros function """

from numpy import *
x = zeros((3, 3), dtype=int)
print(x)
n = len(x)

for i in range(n):
    for j in range(len(x[i])):
        print(x[i][j])
    print()


"""Getting input in Multi-D array
 using zeros function with for loop """

from numpy import *
m = int(input("Enter no.of rows: "))
n = int(input("Enter no. of column: "))
x = zeros((m, n), dtype=int)
L = len(x)
print(x)

for m in range(L):
    for n in range(len(x[m])):
        E = int(input("Enter elements: "))
        x[m][n] = E

for m in range(L):
    for n in range(len(x[m])):
        print(x[m][n])

print(x)






