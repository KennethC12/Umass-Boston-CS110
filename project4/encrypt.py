import rsa
import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    width = rsa.bitLength(n)
    message = stdio.readAll()

    for char in message:
        x = ord(char)
        y = rsa.encrypt(x, n, e)

        stdio.write(rsa.dec2bin(y, width))

    stdio.writeln()

if __name__ == '__main__':
    main()
