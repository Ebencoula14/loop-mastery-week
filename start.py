number = int(input("Kindly pick a RANDOM number?\n"))
count = 1
for item in range(1, number + 1):
    count = count * item
print(f"The Factorial of {number} is :", count)
