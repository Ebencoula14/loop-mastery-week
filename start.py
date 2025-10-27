for i in range(1, 7):
    if i % 2 == 0:
        i = "*" * i
    else:
        i = str(i) * i
    print(i)