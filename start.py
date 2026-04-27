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
game_images = [rock, paper, scissors]
import random
name = input("HiHi, Welcome to the HOUSE PARTY, we are going to be having TONS OF FUN "
             "TONIGHT,Y'll know the ROCK PAPER SCISSORS game right?\n").lower().title()
if "yes" in name or "yaa" in name or "Of course" in name :
    print("Good, let's play, I am excited!")
    computer = random.randint(0,2)
    while True:
        user_name = input("What is the name?\n").lower()
        if not user_name:
            print("Error, you can't leave an empty space.")
            break
        elif "why" in user_name or "need" in user_name or "what" in user_name or "hmmm":
            print("Well I need to know your name to proceed with the game")
        else:
            name = user_name.title()
            print(f"oh {name}, it is nice to meet your acquaintance. let us play!")
            break
            user_choice = int(input(f"ok, {user_name},kindly pick between 0 (rock), 1 (paper), 2 (scissors)\n"))
            if user_choice >= 0 and user_choice <= 2:
                print(game_images[user_choice])
            print(f"Computer chose:{game_images[computer]}")
            if user_choice == computer:
                print("It is a tie, let's try it again!")
            elif user_choice == 0 and computer == 1:
                print("The Computer wins!")
            elif user_choice == 1 and computer == 2:
                print("The computer wins!")
            elif user_choice == 2 and computer == 1:
                print(f"Hurray {name}, you won!")
            elif user_choice == 2 and computer == 0:
                print("The computer wins!")
            elif user_choice >= 3 or user_choice < 0:
                print(f"Hey {name}, you typed an invalid number, you lose!")
            else:
                print(f"Hurray {name}, you won!")
else:
    print("Really??")
    alternative_choice = input("Why though??\n")
while True:
    alternative_name = input("I understand your feelings, they are VALID,but would you "
                             "like to tell me your name?\n")
    if alternative_name.strip() and alternative_name.lower() not in ["bad", "sad","not interested","weak"]:
        name_variable = alternative_name.strip()
        break
    else:
        print("I really don't mind knowing your name\n ")
print("Alright",name_variable, "You should have a good one.")
