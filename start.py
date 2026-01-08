import random
num = random.randint(1, 21)
if num < 2:
    is_prime = False
else:
    is_prime = True

    for item in range(2, int(num**0.5)+ 1):

        if num % item == 0:
            is_prime= False
        break

    if is_prime :
        print(num, "is a Prime number.")
    else:
        print(num,"is not a prime number.")