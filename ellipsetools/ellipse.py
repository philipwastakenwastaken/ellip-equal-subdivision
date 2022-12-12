import math
from typing import Tuple

from scipy.integrate import quad

"""
Module for the Ellipse class.


Typical usage example:

  ellipse = Ellipse(4, 2)
  x, y = ellipse.point(3/4 * math.pi)
  perimeter = ellipse.arc_length()
"""


class Ellipse:
    """
    An instance of Ellipse contains parameters for an elliptical shape (a, b),
    and contains basic processing methods.

    Attributes
    ----------
    a : float
        Semi-major axis length
    b : float
        Semi-minor axis length
    """

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def point(self, theta: float) -> Tuple[float, float]:
        """
        Find the point in (x, y) coordinate space given by angle theta.

        Parameters
        ----------
        theta : float
            Angle from 0 to theta on the unit sphere in radians.

        Returns
        ----------
        x : float
            The x-coordinate.
        y : float
            The y-coordinate.
        """

        return self.a * math.cos(theta), self.b * math.sin(theta)

    def _arc_length_integral_function(self, theta: float) -> float:
        a_squared = self.a * self.a
        sin_term = a_squared * (math.sin(theta) ** 2)

        b_squared = self.b * self.b
        cos_term = b_squared * (math.cos(theta) ** 2)

        return math.sqrt(sin_term + cos_term)

    def arc_length(self, theta_start: float = 0, theta_end: float = 2*math.pi) -> Tuple[float, float]:
        """
        Find the arc length from theta_start to theta_end (given in radians).
        Calling with default arguments is equal to calculating the perimeter of
        the ellipse. The integral required has no closed form solution
        and must be calcualted with numeric methods.

        Parameters
        ----------
        theta_start : float
            Lower bound for integration.
        theta_end : float
            Upper bound for integration. Default value is 2 * Pi.

        Returns
        ----------
        arc_length : float
            The arc length given the bounds above.
        error : float
            The size of the error given the numeric integration.
        """

        return quad(self._arc_length_integral_function, theta_start, theta_end)
