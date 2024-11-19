import stdio
import stdrandom
import sys

N = int(sys.argv[1])

R1 = stdrandom.uniformInt(1 , N + 1) 
R2 = stdrandom.uniformInt(1, N + 1) 


R = R2 + R1

stdio.write(R)