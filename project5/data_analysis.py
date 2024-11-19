import math
import stdio


# Entry point.
def main():
    ETA = 9.135e-4
    RHO = 5e-7
    T = 297
    R = 8.31457
    

    var = 0
    n = 0

    while not stdio.isEmpty():
        r = stdio.readFloat()
        converted = r * 0.175e-6
        squared = converted ** 2
        var += squared
        n += 1

    var = var / (2 * n)

    k = (6 * math.pi * var * ETA * RHO) / T

    a = R / k

    stdio.writef("%e %e\n", k, a)


if __name__ == '__main__':
    main()
