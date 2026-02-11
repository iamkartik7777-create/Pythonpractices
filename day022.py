def find_second_largest(nums):
    largest = second = float('-inf')
    
    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif n > second and n != largest:
            second = n
            
    return second if second != float('-inf') else None

numbers = [10, 20, 4, 45, 99, 21]
print(find_second_largest(numbers)) 