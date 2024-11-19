import stdio
import sys

Temp = float(sys.argv[1])
WS = float(sys.argv[2])

WT = 35.74 + 0.6215 * (Temp) + (0.4275 * (Temp) - 35.75) * (WS**.16)

stdio.write(WT)