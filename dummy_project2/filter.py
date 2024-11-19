from point3d import Point3D
import stdio
import sys


def main():
    r = float(sys.argv[1])

    filtered_points = []

    while not stdio.isEmpty():
        
        x = stdio.readFloat()
        y = stdio.readFloat()
        z = stdio.readFloat()

        point = Point3D(x, y, z)

        if point.distToOrigin() <= r:
            filtered_points.append(point)
        

    filtered_points.sort()

    for point in filtered_points:
        stdio.writef("%s\n" , point)

if __name__ == "__main__":
    main()