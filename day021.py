num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Output:", factorial)

num = int(input("Enter a number: "))
count = len(str(abs(num))) 
print("Output:", count)