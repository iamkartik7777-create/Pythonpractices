#Print Armstrong numbers from 1 to 1000
for num in range(1, 1001):
    temp = num
    sum = 0
    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    if sum == num:
        print(num)

#Check Armstrong Number (Using for loop only)
num = int(input("Enter a number: "))

digits = len(str(num))
sum = 0

for d in str(num):
    sum = sum + (int(d) ** digits)

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
