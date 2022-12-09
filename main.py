import math
from ellipse import Ellipse
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize


def arc_length_loss_function(theta, ellipse, arc_subdiv, r):
    dist, _ = ellipse.arc_length(r, theta)
    
    # MSE estimator
    return (dist - arc_subdiv) ** 2

def points_to_file(X, Y):
    with open('data.txt', 'w') as f:
        f.truncate(0)
        
        for x, y in zip(X, Y):
            f.writelines(f'{x:.5f} {y:.5f}\n')

if __name__ == '__main__':
    total_rad = 2 * math.pi
    a = 4
    b = 2

    n_holes = 30
    radian_per_hole = total_rad / n_holes

    ellipse = Ellipse(a, b)
    arc_length, _ = ellipse.arc_length()
    arc_subdiv = arc_length / n_holes

    t = 0
    x_coords = []
    y_coords = []
    ts = []
    for i in range(n_holes):
        # estimate of next t-value
        next_t = t + radian_per_hole 

        optim = minimize(arc_length_loss_function, next_t, args=(ellipse, arc_subdiv, t)) 
        t = optim.x[0]
        ts.append(t)
        
        x, y = ellipse.point(t)
        x_coords.append(x)
        y_coords.append(y)
        
    points_to_file(x_coords, y_coords)

    old_method_x = []
    old_method_y = []
    a = 0
    for i in range(n_holes):
        x, y = ellipse.point(a)
        old_method_x.append(x)
        old_method_y.append(y)
        a += radian_per_hole
    
    plt.figure(figsize=(8, 5))
    plt.plot(x_coords, y_coords, 'o')
    plt.title('Optim. method')
    plt.axis('equal')
    plt.show()
    
