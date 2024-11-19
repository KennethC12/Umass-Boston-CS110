import stdio
import sys
n = int ( sys . argv [1])
x = 0
i = 1
while i <= n:
    if i % 2 == 0:
        x += i ** 2
    i += 1
stdio . writeln ( x)