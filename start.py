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
import random
message = input("Hihi Everyone, we are all welcome to the HOUSE PARTY,"
                             "we are going to be having a lot of FUN, we know the "
                             "ROCK,PAPER SCISSORS game right??\n").lower()
if "of course" in message or "yes" in message or "i think so" in message or "alright" in message or "yea" in message:
    print("Sweet, let's play!")
elif "no" in message or "nah"or "i haven't heard of it" in message or "what are the rules" or "what is that" in message:
    print("Are you for real?")
    choice = input("Are you guys interested? I can quickly bring you guys to speed?\n").lower()
    if "yes" in choice or "cool" in choice or "of course" in choice:
        print("ok, good these are the rules of the game.")
        choice_rules_of_game=input("it is ROCK PAPER SCISSOR game, you are pick any of the three options"
              "PAPER >> ROCK ,"
              "ROCK >> SCISSORS and  SCISSORS >> PAPER do you get that?\n").lower()
        if "yes" in choice_rules_of_game or " i get it " in choice_rules_of_game:
            print("Sweet, them let's play!")
        else:
            print("Go back to the rules of the game.")
    else:
        name_of_uninterested=input("alright, no problem, i didn't get name tho'\n")
    while True:
        if not name_of_uninterested:
            print("alright,You should have a GOOD one!")
            break
        elif "why" in name_of_uninterested or "what" in name_of_uninterested:
            print("No problem, You should have good day!")
            break
    print("alright", name_of_uninterested,"enjoy the rest of your evening")