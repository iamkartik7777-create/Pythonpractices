nums = []
for i in range(5):
    nums.append(int(input("Enter number: ")))

print("Largest:", max(nums))
print("Smallest:", min(nums))
print("Sum:", sum(nums))

unique_nums = list(set(nums))
print("Without duplicates:", unique_nums)






students = {
    "Rahul": 85,
    "Aman": 90,
    "Neha": 85
}

marks = students.values()

print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))

marks_set = set(marks)
print("Final set of marks:", marks_set)