numbers = [3, 7, 2, 9, 12, 15, 1]
max_score = 0
even_number = []
for i in numbers:
    if i % 2 == 0:
        even_number.append(i)
print("The number of the  EVEN numbers is : ", len(even_number))