# Second largest

def second_max(num):
    largest = float("-inf")
    second_largest = float("-inf")

    for i in num:
        if i>largest:
            second_largest = largest
            largest = i
        if i> second_largest and i<largest:
            second_largest = i
    return second_largest

li1 = [1,3,8,4,46]
li2 = [1,4,6,3,5,3,4]
li3 = [5,6,43,5,3,5,3]