def sum_of_all(*nums):
    total = 0
    for i in nums:
        total += i
    return total
nums = int(input("Pick any random numbers and I will tell you the sum of the numbers."))
print(sum_of_all(nums))