
def even_numbers(n):
    even =[]
    odd = []
    for i in range(n+1):
        if i % 2 ==0:
            even.append(i)
    return even


n =int(input("pick any arbitrary number of your choice and  i will list the even NUMBERS iin that range\n "))
print(even_numbers(n))