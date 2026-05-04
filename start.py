Autumn = ["September", "October",  "November"]
Winter = ["December", "January", "February" ]
Summer = ["June", "July", "August"]
Spring = ["March", "April", "May"]
user_input = input("what MONTH is it over there?\n").title()
if user_input in Autumn :
    print("Oh It's AUTUMN already.")
elif user_input in Winter:
    print("WINTER is HERE!")
elif user_input in Summer:
    print("SUMMER BODY banging")
elif user_input in Spring:
    print("It's SPRING.")
else:
    print("??")