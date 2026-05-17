def add_all_nums(*nums):
    total = 0
    for i in nums:
        total += i
    return total

print(add_all_nums(23,234,6364))