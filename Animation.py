# Initialize an empty plot
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Initialize an empty plot
fig, ax = plt.subplots()
x_data = []
y_data = []

plt.xlabel("Number of iterations")  # Label for the x-axis
plt.ylabel("Error (hours)")  # Label for the y-axis

line, = ax.plot(x_data, y_data, 'ro')  # 'ro' for red points

# Set initial axis limits
ax.set_xlim(0, 10)  # Adjust x-axis limits as needed
ax.set_ylim(-1, 1)  # Adjust y-axis limits as needed

# Function to update the plot with new data
def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame))  # Replace this with your data source or calculation

    line.set_data(x_data, y_data)

    # Adjust axis limits to fit the data
    ax.relim()
    ax.autoscale_view()

    return line,

# Decrease the interval for faster animation (e.g., 50 milliseconds)
interval = 50  # Adjust this value to control the animation speed

# Create an animation with the adjusted interval
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), blit=True, repeat=False, interval=interval)

# Show the plot (note: the plot will continuously update)
plt.show()