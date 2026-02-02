# Simple Right-Angled Triangle
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Increasing Number Triangle    
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()


# Same Number Pattern
for i in range(1, 5):
    print(str(i) * i)


# Pyramid Pattern
n = 3
for i in range(n):
    print(" "*(n-i-1) + "*"*(2*i+1))
