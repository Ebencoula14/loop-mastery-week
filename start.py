scores = 0
age = 0
for number in range(0, 101):
    if number % 2 == 0:
        scores += number
    else:
        age +=  number

print(f"The sum of EVEN number is {scores}. And the sum of ODD number is {age}.")
