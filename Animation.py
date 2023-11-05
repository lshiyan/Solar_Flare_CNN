# Initialize an empty plot
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from IPython import get_ipython
import csv
import os

os.chdir("C:\\Users\\Shiyan Liu\\GitHub\\Solar_Flare_CNN")
losses=[]

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = next(reader)  # Assuming one row of data
    losses=list(data)

losses=[float(num) for num in losses]

print(len(losses))

# Initialize an empty plot
fig, ax = plt.subplots()
x_data = []
y_data = []

plt.xlabel("Number of iterations")  # Label for the x-axis
plt.ylabel("Error (hours)")  # Label for the y-axis

line, = ax.plot(x_data, y_data, 'r--')  # 'ro' for red points

# Set initial axis limits
ax.set_xlim(0, len(losses)//5)
ax.set_ylim(0, 50)
# Function to update the plot with new data
def update(frame):
    x_data.append(frame)
    y_data.append(losses[frame*5])  # Replace this with your data source or calculation
    
    line.set_data(x_data, y_data)

    # Adjust axis limits to fit the data
    ax.relim()
    ax.autoscale_view()

    return line,

# Decrease the interval for faster animation (e.g., 50 milliseconds)
interval = 50  # Adjust this value to control the animation speed

# Create an animation with the adjusted interval
ani = FuncAnimation(fig, update, frames=range(len(losses)//5), blit=True, repeat=False, interval=interval)

# Show the plot (note: the plot will continuously update)
plt.title("Average Iteration Error Over Time of CNN Trained on Solar Images")
plt.show()