number =int(input("Please enter any number of your choice?\n"))
count =0
while number != 0:
    number = number // 10
    count = count + 1
print("The Total number of integers is : ", count)