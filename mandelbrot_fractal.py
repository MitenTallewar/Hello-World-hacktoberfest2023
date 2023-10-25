import matplotlib.pyplot as plt
import numpy as np

# Define the properties of the fractal image
width, height = 800, 800
xmin, xmax = -2, 1
ymin, ymax = -1.5, 1.5
max_iter = 256

# Create an empty image with the specified dimensions
img = np.zeros((width, height, 3), dtype=np.uint8)

# Generate the Mandelbrot fractal
for x in range(width):
    for y in range(height):
        zx, zy = x * (xmax - xmin) / (width - 1) + xmin, y * (ymax - ymin) / (height - 1) + ymin
        c = zx + zy * 1j
        z = c
        for i in range(max_iter):
            if abs(z) > 2.0:
                break 
            z = z * z + c
        # Assign a color based on the number of iterations
        r, g, b = i % 8 * 32, i % 16 * 16, i % 32 * 8
        img[x, y] = (r, g, b)

# Display the Mandelbrot fractal
plt.imshow(img)
plt.show()
