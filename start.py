num = 1
choice =int(input('Kindly pick any number of your choice\n'))
for i in range(1,choice + 1 ):
    num *= i
print("The Factorial of the number you picked is : " , num)