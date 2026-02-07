num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Output:", factorial)



num = int(input("Enter a number: "))
count = len(str(abs(num))) 
print("Output:", count)


age = int(input("Enter your age: "))

if 0 <= age <= 12:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior Citizen")
else:
    print("Invalid age")