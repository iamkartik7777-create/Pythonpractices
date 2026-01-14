days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

num = int(input("Enter week number (1-7): "))

if 1 <= num <= 7:
    print(days[num-1])
else:
    print("Invalid input")
