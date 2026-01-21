                                #Fibonacci Series using for loop
n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


                                #Fibonacci Series using while loop
n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 0

while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1
