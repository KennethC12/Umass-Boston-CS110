import stdio
import sys

# Accept name1 (str), name2 (str), and name3 (str) as command-line arguments.
name1 = (sys.argv[1])
name2 = (sys.argv[2])
name3 = (sys.argv[3])

# Write "Hi name3, name2, and name1." to standard output.
stdio.write('Hi ')
stdio.write(sys.argv[3])
stdio.write(', ')
stdio.write(sys.argv[2])
stdio.write(', and ')
stdio.write(sys.argv[1])
stdio.write('.')



