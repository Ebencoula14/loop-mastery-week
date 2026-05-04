def add_two_numbers(num_1, num_2):
    total = num_1 + num_2
    return total
user_input = input("Do you LIKE to the SUM of your two FAVORITE NUMBERS?\n")
if "yes" in user_input or "of course" in user_input or "yea" in user_input:
    first_number = int(input("So what is the first FAVORITE NUMBER?\n"))
    second_number = int(input("the SECOND?\n"))
    print("The SUM of your FAVORITE NUMBERS is:",add_two_numbers(first_number, second_number))
else:
    print("Well, it SEEMS you are NOT INTERESTED")