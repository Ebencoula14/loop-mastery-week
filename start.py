import random
Heads = 0
Tails = 0
for i in range(100):
    toss = random.choice(['H', 'T'])
    if toss == "H":
        Heads += 1
    else:
        Tails += 1
print("The number of Heads is : ", Heads)
print("The number of Tails is: ", Tails)