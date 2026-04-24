import random
Heads = 0
Tails = 0
for i in range(1000):
    toss = random.choice(['H', 'T'])
    if toss == "H":
        Heads += 1
    else:
        Tails += 1
    percentage = ((Heads) / 1000) * 100
print("The number of Heads is : " , Heads)
print("the number of Tails is : ", Tails)
print("The percentage of Heads is :" , percentage)