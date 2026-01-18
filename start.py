count = 0
num = 0
for item in range(1,101):
    if item % 2 == 0:
        count += item
    else:
        num += item
print(f"The sum of EVEN numbers is {count} and the sum of ODD numbers is {num}")