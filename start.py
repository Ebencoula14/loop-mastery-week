for i in range(1, 21):
    if i % 2 == 0:
        i = "Even"
    elif i % 5 == 0:
        i = "⭐"
    else:
        i = "Odd"
    print(i)