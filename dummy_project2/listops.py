
def any(a):
    for i in range(len(a)):
        if a[i]== False:
            return True
    return False


def all(a):
    for i in range(len(a)):
        if a[i] == True:
            return False
    return True


def exactly(a, k):
    count1 = 0
    for i in range(len(a)):
        if a[i]:
            count1 += 1
        if count1 == k:
            return True
    if count1 == 0:
        return True
    return False


def count(a):
    count2 = 0
    for i in range(len(a)):
        if a[i] == False:
            count2 += 1

    return count2


# Unit tests the library.
def _main():
    import stdio

    a = []
    stdio.writeln(any(a))
    stdio.writeln(all(a))
    stdio.writeln(exactly(a,3))
    stdio.writeln(count(a))


if __name__ == '__main__':
    _main()