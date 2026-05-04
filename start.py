def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
user_input = int(input("what is the radius of your CIRCLE?\n"))
print(area_of_circle(user_input))