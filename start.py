number_list = [5, 3, 8, 6, 2, 10]
new_number_list = []

for i in number_list:
    if i % 2 == 0:
        i = i ** 2
    new_number_list.append(i)
print(new_number_list)
