import stdarray
import stdrandom
import stdio

minuet = stdarray.create2D(11,16)
#This for loop is to read the List
for i in range(11):
    for j in range(16):
        minuet[i][j] = stdio.readInt()
        
#This for loop is to get a random Colmum and Row.
for count in range (16):
    i = stdrandom.uniformInt(0,11)
    j = stdrandom.uniformInt(0,16)
    m = minuet[i][j]
    #Then Print out the data in this format.
    stdio.write(str(minuet[i][j])+ " ")

trio = stdarray.create2D(6,16)

for i in range (6):
    for j in range (16):
        #DO NOT FOR GET () AFTER READINT or ELSE IT WONT READ THE LIST!!!
        trio[i][j] = stdio.readInt()

for counts in range (16):
    i = stdrandom.uniformInt(0,6)
    j = stdrandom.uniformInt(0,16)
    t = trio[i][j]
    stdio.write(str(trio[i][j])+ " ")

