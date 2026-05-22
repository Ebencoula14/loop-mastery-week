def add_item(n):
    food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
    food_stuff.append(n)
    return  food_stuff
n = input("What is your favorite FOODSTUFF?\n")
print("Ok the updated LIST is : ", add_item(n))