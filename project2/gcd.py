import stdio
import sys

p = int(sys.argv[1])
q = int(sys.argv[2])


while p % q != 0:
    #Add temp variable for p
    temp = p
    p = q
    #If I put p % q it would be q % q, so I would use temp instead of p
    q = temp % q

print(q)