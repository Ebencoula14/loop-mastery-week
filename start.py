def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
user_choice = int(input("what is your favorite number?\n"))
print("Prime Number?", is_prime(user_choice))
