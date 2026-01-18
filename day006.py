#Sum of even numbers from 1 to 100 is
# sum_even = 0

# for i in range(1, 101):
#     if i % 2 == 0:
#         sum_even += i

# print("Sum of even numbers from 1 to 100 is:", sum_even)







# For loop example
print("For Loop:")
for i in range(1, 6):
    print(i)

print("----------------")

# While loop example
print("While Loop:")
i = 1
while i <= 5:
    print(i)
    i += 1

print("----------------")

# Sum of numbers 1 to 10
sum_all = 0
for i in range(1, 11):
    sum_all += i
print("Sum of 1 to 10:", sum_all)

print("----------------")

# Sum of even numbers 1 to 100
sum_even = 0
for i in range(2, 101, 2):
    sum_even += i
print("Sum of even numbers 1 to 100:", sum_even)

print("----------------")

# Sum of odd numbers 1 to 100
sum_odd = 0
for i in range(1, 101, 2):
    sum_odd += i
print("Sum of odd numbers 1 to 100:", sum_odd)

print("----------------")

# break example
print("Break Example:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("----------------")

# continue example
print("Continue Example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)







#Full Loop Program (User Input + Table + Count)
# User input
n = int(input("Enter a number: "))

print("Numbers from 1 to", n)
for i in range(1, n + 1):
    print(i)

print("----------------")

# Multiplication table
print("Multiplication Table of", n)
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

print("----------------")

# Count even and odd numbers
even = 0
odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count:", even)
print("Odd count:", odd)

print("----------------")

# Reverse loop
print("Reverse Order:")
for i in range(n, 0, -1):
    print(i)








#Opposite Loop Code (WHILE LOOP)
# User input
n = int(input("Enter a number: "))

# Print numbers from 1 to n
print("Numbers from 1 to", n)
i = 1
while i <= n:
    print(i)
    i += 1

print("----------------")

# Multiplication table using while loop
print("Multiplication Table of", n)
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

print("----------------")

# Count even and odd numbers
even = 0
odd = 0
i = 1

while i <= n:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
    i += 1

print("Even count:", even)
print("Odd count:", odd)

print("----------------")

# Reverse order using while loop
print("Reverse Order:")
i = n
while i >= 1:
    print(i)
    i -= 1

