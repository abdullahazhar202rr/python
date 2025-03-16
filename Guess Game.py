import random
randomNo=random.randint(1,100)
gusses=0
userguess=None
while(userguess!=randomNo):
    userguess=int(input("Enter the number: "))
    gusses+=1
    if(userguess==randomNo):
        print("Congratulations ")
    elif(userguess>randomNo):
        print("It's Too High.Enter lower number please\n")
    elif(userguess<randomNo):
        print("It's Too low.Enter higher number please.")

if gusses==1:
    print(f"you guess the number in {gusses}st attempt")
elif(gusses==2):
    print(f"you guess the number in {gusses}nd attempt")
elif(gusses==3):
    print(f"you guess the number in {gusses}rd attempt")
elif(gusses>=4):
    print(f"you guess the number in {gusses}th attempt")
    
    
with open("highscore.txt","r") as h:
    hs=int(h.read())

if (gusses<hs):
    print("you just broke the highscore!!")
    with open("highscore.txt","w") as g:
        g.write(str(gusses))