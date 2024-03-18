import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

# Placeholder for image path
image_path = "/path/to/your/image.jpg"

# Load the image
img = Image.open(image_path)
fig, ax = plt.subplots()

# Display the image
ax.imshow(img)

# Function to handle button click event
button_locations = []  # To store button names and their locations

def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        print(f"Clicked at: x={event.xdata}, y={event.ydata}")
        button_name = input("Enter button name: ")
        circle_radius = input("Enter circle radius (default 10): ")
        circle_radius = int(circle_radius) if circle_radius.isdigit() else 10
        
        # Draw a circle around the clicked location
        circle = patches.Circle((event.xdata, event.ydata), circle_radius, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(circle)
        plt.draw()
        
        # Store the button information
        button_locations.append({
            "name": button_name,
            "x": event.xdata,
            "y": event.ydata,
            "radius": circle_radius
        })

# Connect the click handler
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
