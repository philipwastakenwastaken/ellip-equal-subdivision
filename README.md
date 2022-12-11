# ellipsetools
This package provides a few convinient tools for ellipses. The main takeaway is the ability to subdivide an
ellipse. Specifically, it can generate $N$ points on an ellipse, with axes $(a, b)$,
where the arc length between each point is identical. Refer to the *Usage* section to see an example of this.
The total arc length of the ellipse is solved (numerically) by the integral

![](https://raw.githubusercontent.com/philipwastakenwastaken/ellipsetools/main/images/arc_length_formula.png)

Using the above, we split the task into $N$ optimization problems to find coordinates of each segment.
The program is reasonably fast and can easily generate more than $N = 1000$ points.

## Installation
The package is available on `PyPI`. You can install using the command below.
```
pip install ellipsetools
```

## Usage
An example of a command-line program is given in `examples/cnc_drill_holes.py`. It creates coordiates
for hole-drilling on an elliptical shape for CNC machines. In such cases, it is paramount that each hole
has equal spacing.

Running the program produces the following ellipse:
![](https://raw.githubusercontent.com/philipwastakenwastaken/ellipsetools/main/images/ellipse.png)
From the above, it is clear that the holes are evenly spaced. Blue points indicate holes, whereas the
orange curve is the shape of the body which is to be drilled by the CNC machine.
