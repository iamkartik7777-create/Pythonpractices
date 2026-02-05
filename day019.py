# name = input("ENTER YOUR NAME IS :")
# age = input("ENTER YOUR AGE IS :")

# print(f"Hello {name} you are {age} years old. ")

# Condition: Agar temperature 30 se zyada hai, toh print karo "It is hot today."
# Else (Warna): Print karo "It is a nice day."
# tem = int(input("Temperature is :"))
# if tem>30:
#          print ("It is hot today.")

# else:
#     print("It is a nice day.")


# Agar Marks 90 se zyada hain: Print karo "Excellent!"
# Agar Marks 40 se 90 ke beech hain: Print karo "You passed."
# Else (40 se kam): Print karo "Better luck next time."

# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Excellent!")
# elif marks >= 40:
#     print("You passed.")
# else:
#     print("Better luck next time.")
            
# User se uski Salary pucho.
# Agar salary 50,000 se zyada hai, toh print karo "You are rich!"
# Agar salary 20,000 aur 50,000 ke beech hai, toh print karo "You are doing well."
# Agar 20,000 se kam hai, toh print karo "Work hard!"

# salary = int(input("Enter your salary:"))
# if salary>=50000:
#          print("You are rich!")
# elif salary>=20000:
#          print("You are doing well.")
# elif salary<20000:
#         print("Work hard!")


# for i in range(1,11):
#     print(i,end=" ")

# count = 5
# while count >= 1:
#     print(f"Count is: {count}")
#     count = count - 1 


# for i in range(1, 11):
#     if i == 5:
#         break  # 5 par aate hi loop ruk jayega
#     print(i)


# count = 1
# while count <=3000:
# #     print()
#     print("I LOVE YOU:",count)
#     count +=1

# for i in range(2, 21, 2):
#     print(i , end=" ")

colors = ["red", "green", "blue"]

for i in range(len(colors)):
    print(i, colors[i])

colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(index, color)


total = 0

for i in range(1, 11):
    total += i

print("Sum:", total)

num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

num = 546
count = 0

for i in str(num):
    count += 1

print("Digits:", count)

text = "hello"
rev = ""

for ch in text:
    rev = ch + rev

print(rev)
