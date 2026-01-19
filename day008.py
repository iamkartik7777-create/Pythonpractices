                                 #for loop – print numbers 1 to 100
for i in range(1, 101):
    print(i,end=" ")

#step=10
for i in range(1, 101,10):
    print(i,end=" ")

                               #while loop – print numbers 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

                              #Sum of numbers from 1 to 10
total = 0
for i in range(1, 11):
    total += i

print("Sum =", total)


                              #Print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

                              #Print Even Numbers (1–100)
print("Even numbers from 1 to 100:")
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
                              #Print Odd Numbers (1–100)
print("Odd numbers from 1 to 100:")
for i in range(1, 101):
    if i % 2 != 0:
        print(i)

                             #Both Even and Odd in One Program
for i in range(1, 101):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

                              #Loop through a list
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


                                #Using enumerate()
names = ["Ram", "Shyam", "Mohan"]

for index, name in enumerate(names):
    print(index, name)
                               #Using break
for i in range(1, 10):
    if i == 5:
        break
    print(i)
    
                                