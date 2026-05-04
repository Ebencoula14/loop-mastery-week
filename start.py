def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
user_input = int(input("what is your FAVORITE numbers, and I will tell you THE SUM!\n"))
print(sum_of_numbers(user_input))