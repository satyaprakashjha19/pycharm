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