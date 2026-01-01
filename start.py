count = 0
score = 0
for i in range(1,101):
    if i % 2 == 0:
        count += i
    else:
        score += i
print(f"The sum of EVEN number is {count} and the sum of ODD numbers is {score}")