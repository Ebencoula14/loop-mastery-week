number = 0
odd = 0
for i in range(1,101):
    if i % 2 == 0:
        number += i
    else:
        odd += i
print(f"The sum of EVEN numbers is {number}. and The sum of all ODD numbers is {odd}")