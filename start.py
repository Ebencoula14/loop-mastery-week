number = input("Enter a number please\n")
score = int(number)
count = 0
for i in range(score + 1):
    count += i
print(f"The SUM of numbers in {score} is : ", count)
