import math
from ellipse import Ellipse
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import sys


def arc_length_loss_function(theta, ellipse, arc_subdiv, r):
    dist, _ = ellipse.arc_length(r, theta)
    
    # MSE estimator
    return (dist - arc_subdiv) ** 2

def points_to_file(path, X, Y):
    with open(path, 'w') as f:
        f.truncate(0)
        
        for x, y in zip(X, Y):
            f.writelines(f'{x:.5f} {y:.5f}\n')

if __name__ == '__main__':
    # Ellipse dimensions
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    n_holes = int(sys.argv[3])

    total_rad = 2 * math.pi
    radian_per_hole = total_rad / n_holes

    ellipse = Ellipse(a, b)
    arc_length, _ = ellipse.arc_length()
    arc_subdiv = arc_length / n_holes

    # Knowing the size of each arc length, we must now segment the ellipse.
    t = 0
    x_coords = []
    y_coords = []
    ts = []
    for i in range(n_holes):
        # Estimate of next t-value
        t_prime = t + radian_per_hole 

        # Find a segment (t, t_prime) whose arc length is equal to arc_subdiv by optimization.
        optim = minimize(arc_length_loss_function, t_prime, args=(ellipse, arc_subdiv, t)) 
        t = optim.x[0]
        ts.append(t)
        
        x, y = ellipse.point(t)
        x_coords.append(x)
        y_coords.append(y)
        
    points_to_file('data.txt', x_coords, y_coords)

    plt.figure(figsize=(8, 5))
    plt.plot(x_coords, y_coords, 'o')
    plt.title('Optim. method')
    plt.axis('equal')
    plt.savefig('ellipse.png')
    plt.show()
    
