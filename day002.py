nums = []
for i in range(5):
    nums.append(int(input("Enter number: ")))

print("Largest:", max(nums))
print("Smallest:", min(nums))
print("Sum:", sum(nums))

unique_nums = list(set(nums))
print("Without duplicates:", unique_nums)
