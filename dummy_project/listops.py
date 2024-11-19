
#Create a function where first occurrence in the list, if it doesnt match or exist, return -1
def find(a, k):
    for i in range (len(a)):
        if a[i] == k:
            return i
    return -1
#Create a function where last occurrence in the list, if it doesnt match or exist, return -1 
#Since I already have a return in the for loop that tells you if it is right, then you have to have a return statement outside of the for loop if it is wrong
def rfind(a, k ):
    for i in reversed(range(len(a))):
        if a[i] == k:
            return i
    return -1
#Create a function where it +=1 if there is the same number in the list.
def count(a, k ): 
    j = 0
    for i in (a):
        if i == k:
            j +=1
    return j
#Create a function where it shows that if a is == to k then it returns true or else it will be false.
def  contains(a, k):
    for i in (a):
        if i == k:
            return True
    return False

def _main():
    import stdio
    a = [5 , -1, 3, 4, 3, -2, 3, 5]
    stdio.writeln(find(a , 3))
    stdio.writeln(rfind (a , 3))
    stdio.writeln(count (a , 3))
    stdio. writeln(contains (a , 6))

if __name__ == "__main__":
    _main()

