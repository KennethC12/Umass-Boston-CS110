import stdaudio
import stdio
import sys

waltz = stdio.readAllInts()

if len(waltz) != 32:
    sys.exit("A waltz must contain exactly 32 measures")

#Add a for loop for Minuet
for i in range(0, 16):
    #If the number isnt between i and 176 write ""
    if not 1 <= waltz[i] <= 176:
        sys.exit("A minuet measure must be from [1, 176]")

for j in range(16, 32):
    if not 1 <= waltz[j] <= 96:
        sys.exit("A trio measure must be from [1, 96]")

#Add a for loop for minuet and use STDAUDIO to play the file
for k in range(0, 16):
    f = 'data/M' + str(waltz[k])
    stdaudio.playFile(f)


#Add a for loop for Trio and use STDAUDIO to play the file
for l in range(16, 32):
    f = 'data/T' + str(waltz[l])
    stdaudio.playFile(f)
