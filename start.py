def area_of_a_circle(r):
    PIE = 3.142
    area = PIE * r * r
    return area
user_input = int(input("what is the RADIUS of the CIRCLE?\n"))
print(area_of_a_circle(user_input))
