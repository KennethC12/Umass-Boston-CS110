
def any(a):
    for i in range(len(a)):
        if a[i]:
            return True
    return False


# Returns True if all the values in the list are True, otherwise it would be false.
def all(a):
    for i in range(len(a)):
        #If the index of a is not in the list return false, otherwise return true.
        if not a[i]:
            return False
    return True


# Returns True if exactly k values in the list a are True, and False otherwise.
def exactly(a, k):
    #Count_K is to calulate the amount of True and Falses their are.
    count_k = 0
    for i in range(len(a)):
        if a[i]:
            count_k += 1
    if count_k == k:
        return True
    return False


# Returns the number of True values in the list a.
def count(a):
    count_t = 0
    for i in range(len(a)):
        if a[i]:
            count_t += 1
    return count_t


# Unit tests the library.
def _main():
    import stdio

    a = [False, False, True, False, True, True, True]
    stdio.writeln('a             = ' + str(a))
    stdio.writeln('any(a)        = ' + str(any(a)))
    stdio.writeln('all(a)        = ' + str(all(a)))
    stdio.writeln('exactly(a, 3) = ' + str(exactly(a, 3)))
    stdio.writeln('count(a)      = ' + str(count(a)))


if __name__ == '__main__':
    _main()