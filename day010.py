# Fibonacci Series using for loop
n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Fibonacci Series using while loop
n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 0

while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1
 
# Fibonacci Series (first 10 terms – direct)

a = 0
b = 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

# Using a for loop (Multiplication)
# Printing squares of numbers from 1 to 5
print("Squares Table:")
for i in range(1, 6):
    square = i ** 2  # Using Exponent operator
    print(f"{i} squared is {square}")               

# Using a while loop (Modulo & Addition)
# Finding even numbers using the Modulo operator (%)
count = 1
while count <= 10:
    if count % 2 == 0:
        print(f"{count} is Even")
    else:
        print(f"{count} is Odd")
    
    count += 1  # Arithmetic addition to update the loop

                                    #Initializing the variable
total_sum = 0   

for number in range(1, 11):
    total_sum += number  # Adding 'number' to 'total_sum' each time
    print(f"Added {number}, Current Total: {total_sum}")

print(f"Final Result: {total_sum}")