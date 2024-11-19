import stdio
import math
import sys

X1 = float(sys.argv[1])
Y1 = float(sys.argv[2])
X2 = float(sys.argv[3])
Y2 = float(sys.argv[4])

x = (X1-X2)**2
y = (Y1-Y2)**2

ANS = math.sqrt(x+y)

print(ANS)