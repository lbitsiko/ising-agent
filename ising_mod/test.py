import matplotlib.pyplot as plt
import numpy as np

def plot_hexagonal_grid(states, grid_width, grid_height):
    """
    Plot a hexagonal grid using matplotlib.

    Parameters:
    - states: A 2D array of spin states (1 or -1).
    - grid_width: The width of the grid.
    - grid_height: The height of the grid.
    """
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    for x in range(grid_width):
        for y in range(grid_height):
            color = '#ccc2c9' if states[x, y] == 1 else '#7a0c58'
            hex = plt.Polygon(hexagon((x, y)), color=color)
            ax.add_patch(hex)

    plt.xlim([-1, grid_width])
    plt.ylim([-1, grid_height])
    plt.axis('off')
    plt.show()

def hexagon(position):
    """Generate the vertices of a regular hexagon given its position."""
    x, y = position
    return [(x + np.cos(np.pi/3 * i), y + np.sin(np.pi/3 * i)) for i in range(6)]

# Example usage
grid_width, grid_height = 10, 10
states = np.random.choice([-1, 1], size=(grid_width, grid_height))
plot_hexagonal_grid(states, grid_width, grid_height)
