my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
odd_list = []
count = 0
for item in my_list[1::2]:
    odd_list.append(item)
for num in odd_list:
    count += num
print("The sum of ODD-INDEXED Numbers is : ",count)