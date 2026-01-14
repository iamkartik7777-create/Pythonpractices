# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# num = int(input("Enter week number (1-7): "))

# if 1 <= num <= 7:
#     print(days[num-1])
# else:
#     print("Invalid input")


day = int(input("Enter week number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid input! Please enter a number between 1 and 7.")
