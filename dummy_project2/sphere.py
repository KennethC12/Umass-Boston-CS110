import math
import stdio
import sys

r = float(sys.argv[1])

a = (4*(math.pi*(r**2)))
v = (4*(math.pi*(r**3)))/3

stdio.writeln("area = " + str(a))
stdio.writeln("volume = " + str(v ))