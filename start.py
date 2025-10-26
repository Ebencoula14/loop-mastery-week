number = 0
for i in range(1, 301):
    if (i % 4 == 0 or i % 9 == 0) and not ( i % 4 == 0 and i % 9 == 0):
        number += 1
print("The total number of numbers is : ", number)