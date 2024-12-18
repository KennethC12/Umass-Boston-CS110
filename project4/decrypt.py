import rsa
import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    d = int(sys.argv[2])

    width = rsa.bitLength(n)

    message = stdio.readAll()

    for i in range(0, len(message) -1, width):
        s = message[i: i + width]
        y = rsa.bin2dec(s)  
       
        stdio.write(chr(rsa.decrypt(y, n, d)))



if __name__ == '__main__':
    main()
