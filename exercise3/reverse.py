import stdio


# Accept all the strings from standard input and store them in a list a.
a = stdio.readAllStrings()

j = len(a)
# Reverse a.
for i in range(0, j // 2):
    # Iterate over half of the list a...

    # Exchange element at i in a with the element at len(a) - i - 1.
    temp = a[i]
    a[i] = a[j - i - 1]
    a[j - i - 1] = temp

# Write a to standard output.
for i in range(j):
    if i != (j - 1):
        # If i is not the last column, write a[i] with a space after.
        stdio.write(str(a[i]) + ' ')
    else:
        # Otherwise, write the element with a newline after.
        stdio.writeln(a[i])
