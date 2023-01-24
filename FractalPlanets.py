import noise
import numpy as np
import matplotlib.pyplot as plt
import random

# Define the size of the planet
width = 800
height = 800

# Create a numpy array to hold the fractal planet
planet = np.zeros((height, width))

# Define the properties of the fractal planet
octaves = 8
persistence = 0.5
lacunarity = 2.0
scale = 100.0

# Generate the fractal planet
for y in range(height):
    for x in range(width):
        planet[y][x] = noise.pnoise2(x / scale, y / scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)

# Normalize the fractal planet
planet = (planet + 1) / 2

# Generate a random color map
color_map = np.zeros((256, 3))
for i in range(256):
    color_map[i] = [random.random(), random.random(), random.random()]

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the fractal planet
ax.imshow(planet, cmap='gray')

# Add the colorbar
fig.colorbar(ax.imshow(planet, cmap='gray'))

# Show the plot
plt.show()
