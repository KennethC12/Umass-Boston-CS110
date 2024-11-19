import stdio
import stdrandom


rank = stdrandom.uniformInt(2,15)
suit = stdrandom.uniformInt(1,5)

rankstr = str(rank)

if rank == 11:
    rankstr = "Jack"
elif rank == 12:
    rankstr = "Queen"
elif rank == 13:
    rankstr = "King"
elif rank == 14:
    rankstr = "Ace"
    
suitstr = str(suit)

if suit == 1:
    suitstr = "Clubs"
elif suit == 2:
    suitstr = "Diamonds"
elif suit == 3:
    suitstr = "Hearts"
elif suit == 4:
    suitstr = "Spades"

print(rankstr, 'of', suitstr)