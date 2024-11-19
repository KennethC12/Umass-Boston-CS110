import math
import stdio
import sys

lat = float(sys.argv[1])
long = float(sys.argv[2])


stdio.writeln(sys.argv[2])

cen = math.radians(0)



y = math.log((1 + math.sin(math.radians(lat)))/(1 - math.sin(math.radians(lat))))/2


stdio.writeln(y)



