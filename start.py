list_fibonacci = []
a, b = 0 , 1
for item in range(1, 10):
    a, b=b, a + b
    list_fibonacci.append(a)
    if item > 100:
        break
print("The Fibonacci Series is: ", list_fibonacci)