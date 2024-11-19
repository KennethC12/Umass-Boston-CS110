import math
import stdio
import sys

Theta1 = float(sys.argv[1])
N1 = float(sys.argv[2])
N2 = float(sys.argv[3])

T = math.radians(Theta1)

Theta2 = (N1 * math.sin(T)) / N2

A2 = math.asin(Theta2)

A3 = math.degrees(A2)

stdio.write(A3)