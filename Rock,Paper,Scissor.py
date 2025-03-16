import random

def newgame(comp,you):
    if comp==you:
       return None
    elif comp=="R":
        if you=="P":
            return True
        elif you=="S":
            return False
    elif comp=="P":
        if you=="S":
            return True
        elif you=="R":
            return False
    elif comp=="S":
        if you=="R":
            return True
        elif you=="P":
            return False

randnumber=random.randint(1,3)
if randnumber==1:
    comp="R"
elif randnumber==2:
    comp="P"
elif randnumber==3:
    comp="S"
    with open('Game_History.txt','w') as g:
        g=g.write("The History of the game is: \n")
while True:
    print("It's the Rock,paper,sissor game\nPress E to exit")
    you=input("Enter R for Rock P for Paper and S for scissor: ").upper()
    if you=='E':
        break
    print(f"Computer: {comp}")
    print(f"You: {you}")
    game=newgame(comp,you)
    if game==None:
        print("The game tie")
    elif game:
        print("You won")
    else:
        print("You Lose")
    with open('Game_History.txt','a') as g:
        g=g.write(f"Comp chooses:{comp} and user chooses{you}\n")

with open('Game_History.txt','r') as g:
        g=g.read()
        print(g)