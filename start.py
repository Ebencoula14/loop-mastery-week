from random import choice

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
games_images = [rock, paper, scissors]
import random
message = input("Hihi Everyone, we are all welcome to the HOUSE PARTY,"
                             "we are going to be having a lot of FUN, we know the "
                             "ROCK,PAPER SCISSORS game right??\n").lower()
The_options = ["Rock", "Paper", "Scissors"]
computer_choice = random.randint(0,1)
if "of course" in message or "yes" in message or "i think so" in message or "alright" in message or "yea" in message:
    name = input("so what is the name?\n").lower()
    if "i am" in name :
        name_variable = name.split("i am")[-1].strip().title()
        print("Hello,", name_variable,"it is nice having you here, let's play the game.")
    elif "my name is " in name:
        name_variable =name.split("my name is ")[-1].strip().title()
        print(f"well,well,well,{name_variable} it is a pleasure to have your acquaintance")
    elif "i'm" in name :
        name_variable  = name.split("i'm ")[-1].strip().title()
        print(f"welcome,{name_variable}, it is nice to meet you!")
    else:
        print("You wouldn't want to playing these games without knowing  our names right?.")

    user_choice = input(f"so,{name_variable}, you are to pick between ROCK (0), PAPER(1), SCISSORS (2)\n")
    user_choice = int(user_choice)
    if user_choice >= 0 and user_choice <= 2:
        print("Your choice: ",games_images[user_choice])
    print("The computer chose: ",games_images[computer_choice])
    if user_choice == computer_choice:
        print(f"oh,{name_variable} it is a Tie!")
    elif user_choice == 0 and computer_choice == 1:
        print(f"{name_variable}, The COMPUTER WINS!")
    elif user_choice == 1 and computer_choice == 2:
        print(f"{name_variable} The COMPUTER WINS!")
    elif user_choice == 2 and computer_choice == 1:
        print(f"Hurray {name_variable},YOU WON!")
    elif user_choice == 2 and computer_choice == 0:
        print(f"oh {name_variable}, The COMPUTER WINS!")
    elif user_choice >= 3 or user_choice < 0:
        print(f"oh dear, you have entered an invalid number,{name_variable}")
    else:
        print(f"{name_variable}, you won!")



elif "no" in message or "nah"or "i haven't heard of it" in message or "what are the rules" or "what is that" in message:
    print("Are you for real?")
    choice = input("Are you guys interested? I can quickly bring you guys to speed?\n").lower()
    if "yes" in choice or "cool" in choice or "of course" in choice:
        print("ok, good these are the rules of the game.")
        choice_rules_of_game=input("it is ROCK PAPER SCISSOR game, you are to  pick any of the three options "
              "PAPER >> ROCK ,"
              "ROCK >> SCISSORS and  SCISSORS >> PAPER do you get that?\n").lower()
        if "yes" in choice_rules_of_game or " i get it " in choice_rules_of_game:
            print("Sweet, them let's play!")
            alt_name = input("so what is the name?\n").lower()
            if "i am" in alt_name:
                alt_name_variable = alt_name.split("i am")[-1].strip().title()
                print("Hello,", alt_name_variable, "it is nice having you here, let's play the game.")
            elif "my name is " in alt_name:
                alt_name_variable = alt_name.split("my name is ")[-1].strip().title()
                print(f"well,well,well,{alt_name_variable} it is a pleasure to have your acquaintance")
            elif "i'm" in alt_name:
                alt_name_variable = alt_name.split("i'm ")[-1].strip().title()
                print(f"welcome,{alt_name_variable}, it is nice to meet you!")
            else:
                print("You wouldn't want to playing these games without knowing  our names right?.")

            alt_user_choice = input(f"so,{alt_name_variable}, you are to pick between ROCK (0), PAPER(1), SCISSORS (2)\n")
            alt_user_choice = int(alt_user_choice)
            if alt_user_choice >= 0 and alt_user_choice <= 2:
                print("Your choice: ", games_images[alt_user_choice])
            print("The computer chose: ", games_images[computer_choice])
            while True:
                if alt_user_choice == computer_choice:
                    print(f"oh,{alt_name_variable} it is a Tie!")
                    break
                elif alt_user_choice == 0 and computer_choice == 1:
                    print(f"{alt_name_variable}, The COMPUTER WINS!")
                    break
                elif alt_user_choice == 1 and computer_choice == 2:
                    print(f"{alt_name_variable} The COMPUTER WINS!")
                    break
                elif alt_user_choice == 2 and computer_choice == 1:
                    print(f"Hurray {alt_name_variable},YOU WON!")
                    break
                elif alt_user_choice == 2 and computer_choice == 0:
                    print(f"oh {alt_name_variable}, The COMPUTER WINS!")
                    break
                elif alt_user_choice >= 3 or alt_user_choice < 0:
                    print(f"oh dear, you have entered an invalid number,{alt_name_variable}")
                    break
                else:
                    print(f"{alt_name_variable}, you won!")
                    break



        else:
            print("Go back to the rules of the game.")
            co
    else:
        name_of_uninterested=input("alright, no problem, i didn't get name tho'\n").lower()
    while True:
        if not name_of_uninterested:
            print("Alright,You should have a GOOD one!")
            break
        elif "why" in name_of_uninterested or "what" in name_of_uninterested:
            print("No problem, You should have good day!")
            break
        elif "my name is" in name_of_uninterested :
            name_of_uninterested_variable =name_of_uninterested.split("my name is ")[-1].strip()
            print(f"Alright,{name_of_uninterested_variable},have a good evening.")
            break
        elif "i'm " in name_of_uninterested:
            name_of_uninterested_variable = name_of_uninterested.split("i'm")[-1].strip()
        elif "" in name_of_uninterested:
            print("Alright", name_of_uninterested,"enjoy the rest of your evening")
            break