#set
s = {1, 2, 3, 3}
print(s)

s = {1, 2}
s.add(3)

s.update([4, 5, 6])
print(s)

s.remove(2)

s.discard(10)

s.pop()

s.clear()

print(s)

A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)

print(A & B)

print(A - B)

print(A ^ B)

print(2 in A)     # True
print(10 in A)    # False

nums = [1, 2, 2, 3, 4, 4]
unique_nums = set(nums)
print(unique_nums)



