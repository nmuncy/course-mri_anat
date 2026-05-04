import matplotlib.pyplot as plt
import numpy as np
import mpld3

# Create the figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Vector origin (starting point)
x, y, z = [0], [0], [0]

# Vector direction (components)
u, v, w = [1], [2], [3]

# Plot the vector
ax.quiver(x, y, z, u, v, w, color="blue", length=1.0)

# Set labels and axis limits
ax.set_xlim([0, 2])
ax.set_ylim([0, 3])
ax.set_zlim([0, 4])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

mpld3.save_html(fig, "plot.html")
