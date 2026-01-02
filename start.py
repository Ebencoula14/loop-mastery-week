prime_number = []
for num in range(25,51):
    for i in range(2, num):
        if (num % i ) == 0:
            break
    else:
        prime_number.append(num)
print(prime_number)