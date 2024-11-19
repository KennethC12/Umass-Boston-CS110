import stdio
import sys

#m = month d = Day y = year
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# Formulas to get Day of week
year = y-(14-m)//12
day = year+year//4-year//100+year//400
month = m + 12*((14-m)//12)-2
dow = (d + day + 31 * month//12)%7

stdio.writeln(dow)

