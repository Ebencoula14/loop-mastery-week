def generate_fruit():
    fruits = ["orange", "banana", "apple","grape", "breadfruit", "lemon"]
    new_fruits = []
    for item in fruits:
        capitalized_item = item.upper()
        new_fruits.append(capitalized_item)
    print(new_fruits)

generate_fruit()