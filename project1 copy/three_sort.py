import stdio
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])


First = min(x, y, z)

Last = max(x, y, z)

Middle = (x + y + z) - (First + Last)

stdio.write(str(First) + ' ' + str(Middle) + ' ' + str(Last))


