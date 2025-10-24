number = []
for i in range(1, 201):
    if i % 3 == 0 and not i % 6 == 0:
        number.append(i)
print(len(number))

