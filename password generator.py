
introduction = input("Welcome to the ROLLERCOASTER GAME, we are aware of THE AGE RESTRICTIONS RIGHT?"
                     "\n").lower()

if "yes" in introduction or "of course" in introduction or "yea" in introduction:
    print("cool, let's have FUN.")
    name = input("But first i need to know our names, so we can get ALONG quickly right?\n").lower()
    while True:
        if not name :
            print("we need to get acquainted with our names, for easy FLOW of the game.")
            break
        elif 'what' in name or 'why' in name or "not interested" in name :
            print("well,It's COMPANY POLICIES! ")
            break
        elif 'my name is ' in name or " i am " in name or "i'm" in name:
            name_variable  = name.split("my name is " or "i am " or "i'm")[-1].lower().strip().title()
            print(f"oh {name_variable},it is nice to have your acquaintance!")
            break
        elif name:
            name = name.lower().title()
            print(f"oh, {name} It's a PLEASURE to have your ACQUAINTANCE!")
            break
    age =int(input(f"{name}if you don't MIND,HOW OLD ARE YOU ?\n"))
    minor_age = int(18 - age )
    if age >= 18:
        print("WELCOME ONBOARD THE ROLLERCOASTER, YOU ARE OLD ENOUGH TO DRIVE!")
    elif age < 18:
        print(f"I am very SORRY, you need {minor_age} more  years to be ELIGIBLE TO drive.")
    else:
        print("I need to know your age to PERMIT to DRIVE the ROLLERCOASTER!")
else:
   print("Well, I am PLEASED to inform you that there are AGE RESTRICTIONS to be ELIGIBLE TO DRIVE!")