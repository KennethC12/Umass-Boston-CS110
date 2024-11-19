import stdio
import sys

n = int(sys.argv[1])

a = 1
b = 1
i = 3

while i <= n:
    #temp variable
    temp = a
    a = b
    #If I put a + b it would be b + b, so I would use temp instead of a
    b = temp + b

    i += 1
print(b)
