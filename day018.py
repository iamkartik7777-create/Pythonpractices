rows = 5
for i in range(rows):
    # Print spaces
    print(" " * (rows - i - 1), end="")
    # Print stars
    print("*" * (2 * i + 1))