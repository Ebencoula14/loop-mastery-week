import random
count_above_70 = 0
num_in_a_list = []
for i in range(50):
    num = random.randint(1,101)
    if num > count_above_70:
        count_above_70 += 1
        num_in_a_list.append(num)
print(num_in_a_list)
print("The Numbers above 70 : " , count_above_70)