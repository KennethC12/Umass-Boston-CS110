from circle import Circle
import stdio
import sys
# Entry point.
def main():
    # Read floats h, k, and r as command-line arguments.
    h = float(sys.argv[1])
    k = float(sys.argv[2])
    r = float(sys.argv[3])
    # Create a Circle object c of radius r centered at (h, k).
    c = Circle(h, k, r)
    # Read (x, y) points (both floats) from standard input until EOF (use the functions stdio.isEmpty() and stdio.readFloat()).
    count = 0
    total = 0
    while not stdio.isEmpty():
        x = stdio.readFloat()
        y = stdio.readFloat()
        total += 1
        if c.contains(x, y):
            count += 1
    # Write the fraction of points that are not contained in c.
    stdio.writeln(count / total)
if __name__ == "__main__":
    main()