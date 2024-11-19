import stdio
import sys

n = int(sys.argv[1])
a = 1
# Set a = 1
while 1 <= a <= n**(1/3):
    b = a + 1
    while a + 1 <= b**3 <= n - a **3:
        c = a + 1
        while a + 1 <= c <= n**(1/3):
            d = c + 1
            while c + 1 <= d**3 <= n - c**3:
                if a**3 + b**3 == c**3 +d**3:
                    print(str(a**3+b**3) + " = " + str(a) + "^3 + " + str(b) + "^3 = " + str(c) + "^3 + " + str(d) +"^3")
                #Remember to always increment it by 1
                d += 1
            c += 1
        b += 1
    a += 1

