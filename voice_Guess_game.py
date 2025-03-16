import random
import robo_speaker as rs
import speech_recognition as sr
randomNo=random.randint(1,100)
gusses=0
userguess=None
print("Welcome to AI made guess Game")
rs.speak("Welcome to AI made guess Game")
rs.speak("I am thinking of a number between 1 and 100. Try to guess it")
recognizer=sr.Recognizer()
ambient_noise_adjusted=False
while(userguess!=randomNo):
    try:
        with sr.Microphone() as source:
            if not ambient_noise_adjusted:
                rs.speak("Adjusting the ambient noise. Please wait...")
                recognizer.adjust_for_ambient_noise(source)
                ambient_noise_adjusted=True
            recognizer.adjust_for_ambient_noise(source)
            print("Speak now...")
            rs.speak("Speak Now...")
            audio=recognizer.listen(source)
            username_listened=recognizer.recognize_google(audio)
            userguess_save=username_listened
            userguess=int(userguess_save)
            print(userguess)
            rs.speak(f"You guessed the number {userguess}")
            gusses+=1
            if(userguess==randomNo):
                print("Congratulations...")
                rs.speak("COngratulations You guessed it in "+str(gusses)+" attempts")
            elif(userguess>randomNo):
                print("Too high...")
                rs.speak("It is Too HighEnter lower number please")
            elif(userguess<randomNo):
                print("Too low...")
                rs.speak("It is Too low Enter higher number please")
                    
            with open("highscore.txt","r") as h:
             hs=int(h.read())

             if (gusses<hs):
                rs.speak("you just broke the highscore It's saved now")
                with open("highscore.txt","w") as g:
                    g.write(str(gusses))
    except Exception as e:
        print(f"Some exception occurs...{e}")
        rs.speak("Some error occurred"+str(e)+"Please try again.")