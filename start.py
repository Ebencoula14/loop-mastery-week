count = 0
score = 0
for i in range(0, 101):
    if i % 2 == 0:
        count += i
    else:
        score += i
print(f"The sum of EVEN is {count} while the sum of ODD numbers is {score}")