n = int(input("Kindly choose any random number bro?"))
for i in range(1, n + 1):
    if i % 2 == 0:
        i = "*" * i
    else:
        i = str(i) * i
    print(i)