import stdio
import sys

k = int(sys.argv[1])
c = float(sys.argv[2])
e = float(sys.argv[3])

t = c

while abs(1 - c / (t ** k)) > e:
    ft = t**k-c
    fot =  k*(t**(k-1))
    t = t-ft/fot


print(t)