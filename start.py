my_age = 30
your_age = int(input("How OLD are YOU?\n"))
diff = my_age - your_age
diff_1 = your_age - my_age
if my_age > your_age:
    print(f"I am {diff} years older than YOU!")
elif your_age > my_age:
    print(f"you are {diff_1} years older than ME! ")
else:
    print(f"We are AGE MATES!")