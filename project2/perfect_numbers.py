import stdio
import sys

n = int(sys.argv[1])


for i in range(2 , n +1):
    total = 0
    #Make i/2 a int because it will automatically take it as a float
    for j in range(1, int(i/2) + 1):
        if i % j == 0:
            total += j
    if total == i:
        print(i)

