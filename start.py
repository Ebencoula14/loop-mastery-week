def solve_quadratic_equation(x):
    quadratic_equation = 3*(x ** 2) + 5*(x) + 10
    return quadratic_equation
user_choice = int(input("What is your value of X?"))
print(solve_quadratic_equation(user_choice))