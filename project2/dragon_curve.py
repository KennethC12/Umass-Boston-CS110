import stdio
import sys

n = int(sys.argv[1])

dragon = "F"
nogard = "F"

for i in range (1 , n+1):
     temp = dragon
     dragon = str(temp) + "L" + str(nogard)
     nogard = str(temp) + "R" + str(nogard)
     
print(dragon)