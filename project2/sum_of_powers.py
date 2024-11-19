import stdio
import sys

n = int(sys.argv[1])
k = int(sys.argv[2])

total = 0
#Dont use brackets [] use () for Range
for i in range(1, n+1):
    total += i**k

print(total)