import stdio
import sys

#N1 = Player 1's money, N2 = Player 2's money 
N1 = float(sys.argv[1])
N2 = float(sys.argv[2])
P = float(sys.argv[3])

Q = 1 - P

P1 = (1 - (P/Q)**N2) / (1 - (P/Q)**(N1 + N2))

P2 = (1 - (Q/P)**N1) / (1 - (Q/P)**(N1 + N2))

stdio.writeln(P1)

stdio.writeln(P2)
