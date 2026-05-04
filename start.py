fruits = ['banana', 'orange', 'mango', 'lemon']
user_input = input("What is you fave FRUIT?\n")
if user_input not in fruits:
    fruits.append(user_input)
    print("Here is a MODIFIED list:", fruits)
elif user_input in fruits:
    print("We already have that in the LIST!")
else:
    print("ERROR!")