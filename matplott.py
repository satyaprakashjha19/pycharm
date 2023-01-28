""" Matplotlib """

"""print(matplotlib.__version__)"""

"""Draw a line in a diagram from
position (0,0) to position (6,250):"""

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

# plotting without lines using parameter 'o'
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

# Multiple points

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

# Multiple points without lines

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

# When we leave the x axis-points

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

# Matplotlib Markers

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='1')
plt.show()

# Format string fmt = marker|line|color

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'or')
plt.show()

# Marker size short version ms

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', ms=20)
plt.show()

# Marker edge color short version mec and face color short version is mfc

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', ms=20, mec='#b44646', mfc='#4CAF50')
plt.show()

# Matplotlib line style short version ls

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', ms=20,
         mec='#b44646', mfc='#4CAF50', linestyle='dotted')
plt.show()

# Multiple lines

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1, marker='o')
plt.plot(y2, marker='*')


plt.show()

# Specify values for both lines

import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

# Matplotlib Labels and title and font properties
# by fontdict and position of title by loc

import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'red', 'size': 15}


plt.title("Sports Watch Data", fontdict=font1, loc='left')
plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)


plt.plot(x, y)
plt.show()

# Matplotlib adding grid lines by grid
# and which axis grid line show

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis='x')

plt.show()












