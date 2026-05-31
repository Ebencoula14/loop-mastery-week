count = 0
score = 0
for item in range(101):
    if item % 2 == 0 and item != 0:
        count += item
    else:
        score += item
print("The sum of EVEN numbers is ", count,"."" And the sum of ODD numbers is", score,"." )