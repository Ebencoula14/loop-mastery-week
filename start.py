import random
def solve_quadratic_equation(x):
    a = random.randint(1,100)
    b = random.randint(1,100)
    c = random.randint(1,100)
    quadratic_equation = a*(x ** 2) + b*(x) + c
    return quadratic_equation
user_choice = int(input("What is your value of X?\n"))
print(solve_quadratic_equation(user_choice))