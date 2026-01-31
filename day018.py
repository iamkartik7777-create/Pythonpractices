rows = 5
for i in range(rows):
    # Print spaces
    print(" " * (rows - i - 1), end="")
    # Print stars
    print("*" * (2 * i + 1))


size = 5

for i in range(size):
    for j in range(size):
        # Print stars only if it's the first or last row/column
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print() 