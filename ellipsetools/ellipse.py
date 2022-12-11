import math
from typing import Tuple

from scipy.integrate import quad


class Ellipse:

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    # in radians
    def point(self, theta: float) -> Tuple[float, float]:
        return self.a * math.cos(theta), self.b * math.sin(theta)

    def arc_length_integral_function(self, theta: float) -> float:
        a_squared = self.a * self.a
        sin_term = a_squared * (math.sin(theta) ** 2)

        b_squared = self.b * self.b
        cos_term = b_squared * (math.cos(theta) ** 2)

        return math.sqrt(sin_term + cos_term)

    def arc_length(self, theta_start: float = 0, theta_end: float = 2*math.pi) -> Tuple[float, float]:
        return quad(self.arc_length_integral_function, theta_start, theta_end)
