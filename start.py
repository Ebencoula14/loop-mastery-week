def convert_celsius_to_fahrenheit(C):
    F = (C * 9 / 5) + 32
    return  F
C = int(input("What is the degree in celsius?\n"))
print(convert_celsius_to_fahrenheit(C))