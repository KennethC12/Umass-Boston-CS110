import math
import stdio
import sys

x = float(sys.argv[1])
t = float(sys.argv[2])

p = math.exp(-x*t)

stdio.write(p)