from ellipse import Ellipse
from subdivide_ellipse import subdivide_ellipse
import matplotlib.pyplot as plt
import numpy as np

import sys
import math


def points_to_file(path, X, Y):
    with open(path, 'w') as f:
        f.truncate(0)

        for x, y in zip(np.nditer(X), np.nditer(Y)):
            f.writelines(f'{x:.2f} {y:.2f}\n')


if __name__ == '__main__':
    # Ellipse dimensions
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    n_holes = int(sys.argv[3])

    a_prime = a - 6
    b_prime = b - 6

    ellipse = Ellipse(a_prime, b_prime)
    x_coords, y_coords = subdivide_ellipse(ellipse, n_holes)

    x_coords += a
    y_coords += b

    print_idx = 13
    print(f'Left most point: ({x_coords[print_idx]}, {y_coords[print_idx]})')

    points_to_file('data.txt', x_coords, y_coords)

    n_points = 300
    t = 0
    subdiv = (2 * math.pi) / n_points
    outer_ellipse = Ellipse(a, b)

    outer_x = []
    outer_y = []
    for i in range(n_points):
        x, y = outer_ellipse.point(t)
        outer_x.append(x)
        outer_y.append(y)
        t += subdiv

    outer_x = np.array(outer_x)
    outer_y = np.array(outer_y)

    outer_x += a
    outer_y += b

    plt.figure(figsize=(8, 5))
    plt.plot(x_coords, y_coords, 'o', markersize=1)
    plt.plot(outer_x, outer_y, '-')
    plt.title('Optim. method')
    plt.axis('equal')
    plt.savefig('ellipse.png')
    plt.show()
