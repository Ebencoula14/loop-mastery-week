sum_of_odd = 0
sum_of_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        number = "EVEN"
        sum_of_even += i
    else:
        number = "ODD"
        sum_of_odd += i
#print(number, end= " ")
print("The sum of ODD number inn the list is : " , sum_of_odd)
print("The sum of EVEN number in the list is : " , sum_of_even)


