import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])

    pic = Picture(sys.argv[4])
    blob_finder = BlobFinder(pic, tau)
    prevBeads = blob_finder.getBeads(pixels)

    for frame in sys.argv[5:]:
        pic2 = Picture(frame)
        blob_finder2 = BlobFinder(pic2, tau)
        currBeads = blob_finder2.getBeads(pixels)

        for currBead in currBeads:
            dist = math.inf
            for prevBead in prevBeads:
                if dist > currBead.distanceTo(prevBead):
                    dist = currBead.distanceTo(prevBead)
            if dist <= delta:
                stdio.writef("%.4f\n", dist)

        stdio.writeln()
        prevBeads = currBeads


if __name__ == '__main__':
    main()
