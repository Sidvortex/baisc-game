import random
print('''choices are as follows: Rock; Paper; Scissor''')


comp = random.choice([1,2,3])
compdict = {1:"rock", 2:"paper", 3:"scissor"}

player= input ( "enter your choice :")
youdict = {"rock":1, "paper":2, "scissor":3}

you = youdict[player]

print (f"you chose {compdict [you]}\ncomputer chose {compdict[comp]}")


if (comp == you):
    print("It's a Draw!")
    
else:
    if ((comp - you) == 1 or (comp - you) == -2):
        print("You Lose!")
    elif ((comp - you) == -1 or (comp - you) == 2):
        print("You win!")