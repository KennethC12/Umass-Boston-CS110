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

if dow == 0:
    print("Sunday")
elif dow == 1:
    print("Monday")
elif dow == 2:
    print("Tuesday")
elif dow == 3:
    print("Wednesday")
elif dow == 4:
    print("Thursday")
elif dow == 5:
    print("Friday")
elif dow == 6:
    print("Saturday")





