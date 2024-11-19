import stdio
import sys

M1 = float(sys.argv[1])
M2 = float(sys.argv[2])
R = float(sys.argv[3])

G = 6.674 * 10**-11

F = (G * M1 * M2)/R**2

stdio.write(F)


