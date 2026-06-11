def age_name_introductory_message():
    name = input("But first i need to know our names, so we can get ALONG quickly right?\n").lower()
    while True:
        if not name:
            print("we need to get acquainted with our names, for easy FLOW of the game.")
            break
        elif 'what' in name or 'why' in name or "not interested" in name:
            print("well,It's COMPANY POLICIES! ")
            break
        elif 'my name is ' in name or " i am " in name or "i'm" in name:
            name_variable = name.split("my name is " or "i am " or "i'm")[-1].lower().strip().title()
            print(f"oh {name_variable},it is nice to have your acquaintance!")
            break
        elif name:
            name = name.lower().title()
            print(f"oh, {name} It's a PLEASURE to have your ACQUAINTANCE!")
            break


introduction = input("Welcome to the ROLLERCOASTER GAME, we are aware of THE AGE RESTRICTIONS RIGHT?"
                     "\n").lower()

if "yes" in introduction or "of course" in introduction or "yea" in introduction:
    print("cool, let's have FUN.")
    print(age_name_introductory_message())

    age =int(input("if you don't MIND,HOW OLD ARE YOU ?\n"))
    minor_age = int(18 - age )
    if age >= 18:
        print("WELCOME ONBOARD THE ROLLERCOASTER, YOU ARE OLD ENOUGH TO DRIVE!")
    elif age < 18:
        print(f"I am very SORRY, you need {minor_age} more  years to be ELIGIBLE TO drive.")
    else:
        print("I need to know your age to PERMIT to DRIVE the ROLLERCOASTER!")
elif 'no' in introduction or "i haven't" in introduction or "tell me about it" in introduction :
    choice = input("well,I can bring you to speed quickly, do you mind?\n")
    if "no" in choice or "i am interested" in choice or 'alright' in choice :
        print("Alright, we need to know your age first?\n")
        pt

else:
   print("Well, I am PLEASED to inform you that there are AGE RESTRICTIONS to be ELIGIBLE to DRIVE!")
