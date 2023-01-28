import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 2, 17, 2, 9,
     4, 11, 12, 9, 6]

y = [99, 86, 87, 88, 100, 86,
     103, 87, 94, 78, 77, 85, 86]

plt.scatter(x, y, c='blue')
plt.show()

"""Plot with different data shape
and color for two datasets"""

import matplotlib.pyplot as plt
# Dataset 1
x1 = [89, 43, 36, 36, 95, 10,
      66, 34, 38, 20]

y1 = [21, 46, 3, 35, 67, 95,
      53, 72, 58, 10]

# Dataset 2
x2 = [26, 29, 48, 64, 6, 5,
      36, 66, 72, 40]

y2 = [26, 34, 90, 33, 38,
      20, 56, 2, 47, 15]

plt.scatter(x1, y1, c='pink', linewidths=2, marker='s',
            edgecolors='red', s=50)
plt.scatter(x2, y2, c="yellow", linewidths=2, marker="^",
            edgecolors="red", s=200)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()


# Legend in scatter plot

import matplotlib.pyplot as plt

#Adjust cordinates
x = [1,2,3,4,5]
y1 = [2,4,6,8,10]
y2 = [3,6,9,12,15]

# Depict illustration

plt.scatter(x, y1)
plt.scatter(x, y2)

# Apply legend

plt.legend(["2*x", "3*x"], ncol=2,
loc='lower right', bbox_to_anchor=(1,1))
plt.show()

# If use lable parameter then legend() must be use

# import required modules
import matplotlib.pyplot as plt
import numpy as np

# assign coordinates
x = np.arange(1, 6)
y1 = x ** 2
y2 = x ** 4

# depict illustration
plt.scatter(x, y1, label="x**2")
plt.scatter(x, y2, label="x**4")

# apply legend()
plt.legend()
plt.show()


# Scatterplot points with line

import matplotlib.pyplot as plt
import numpy as np

# Initialize x and y coordinates

x = [0.1, 0.2, 0.3, 0.4, 0.5]
y = [6.2, -8.4, 8.5, 9.2, -6.3]

# set the title of a plot

plt.title("Connected scatterplot points with lines")
plt.scatter(x,y)
plt.plot(x,y)
plt.show()

# using colormap

import matplotlib.pyplot as plt
import numpy as np

# assign data points
a = np.array([[9, 1, 2, 7, 5, 8, 3, 4, 6],
                 [4, 2, 3, 7, 9, 1, 6, 5, 8]])
categories = np.array([0,1,2,0,1,2,0,1,2])
colormap = np.array(['r','g','b'])

plt.scatter(a[0], a[1], s=100, c=colormap[categories])
plt.show()



import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [8, 7, 6, 4, 5, 6, 7, 8, 9, 10]

plt.xticks(np.arange(11))
plt.yticks(np.arange(11))

plt.scatter(x, y, s=500, c='g')

plt.title("Scatter Plot", fontsize=25)

plt.xlabel('x-axis', fontsize=18)
plt.ylabel('y-axis', fontsize=18)

plt.show()


# data points with variable size

import matplotlib.pyplot as plt

plt.style.use('seaborn')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
points_size = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]

plt.xticks(np.arange(13))
plt.yticks(np.arange(13))

plt.scatter(x, y, s=points_size, c='g')
plt.title("Scatter plot with increase size")

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.show()