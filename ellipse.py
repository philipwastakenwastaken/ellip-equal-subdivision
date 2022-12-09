import math
from scipy.integrate import quad

class Ellipse:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # in radians
    def point(self, theta):
        return self.a * math.cos(theta), self.b * math.sin(theta)

    def arc_length_integral_function(self, theta):
        a_squared = self.a * self.a
        sin_term = a_squared * (math.sin(theta) ** 2)
        
        b_squared = self.b * self.b
        cos_term = b_squared * (math.cos(theta) ** 2)

        return math.sqrt(sin_term + cos_term)
    
    def arc_length(self, theta_start=0, theta_end=2*math.pi):
       return quad(self.arc_length_integral_function, theta_start, theta_end)
