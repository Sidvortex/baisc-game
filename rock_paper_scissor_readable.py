import random
print('''choices are as follows: Rock; Paper; Scissor''')


comp = random.choice([1,2,3])
player= input ( "enter your choice :")
youdict = {"rock":1, "paper":2, "scissor":3}
compdict = {1:"rock", 2:"paper", 3:"scissor"}
you = youdict[player]
print (f"you chose {compdict [you]}\ncomputer chose {compdict[comp]}")

if (comp ==  you):
    print ("TIEEE!")
else:
    if (comp == 2 and you ==1):  #1
        print("you looose!")
    elif (comp==2 and you ==3):  #-1
        print ("You WIN!")
    elif (comp==1 and you ==3):  #-2
        print ("You loose!")
    elif (comp==1 and you ==2):  #-1
        print ("You WIN!")
    elif (comp==3 and you ==2):  #1
        print ("You loose!")
    elif (comp==3 and you ==1):  #2
        print ("You WIN!")
    else :
        print("something went wrong")
