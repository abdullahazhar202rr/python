import random
import robo_speaker as rs
import speech_recognition as sr

def listen_for_activation_phrase(recognizer, source):
    rs.speak("Listening for activation phrase.")
    while True:
        try:
            audio = recognizer.listen(source)
            phrase = recognizer.recognize_google(audio).lower()
            print(f"Recognized phrase: {phrase}")
            if any(keyword in phrase for keyword in ["hamla", "humnava", "hamna", "bhavna", "amna","cm","stout","stot","hast out","he stood", "hashtag", "hairstyle","rest out"]):
                return True
            else:
                rs.speak("access denied try again")
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            rs.speak("Could not reach the recognition service.")
            return False
        except Exception as e:
            print(f"Error: {e}")
            rs.speak("An error occurred. Please try again.")
            return False

def play_guessing_game():
    random_no = random.randint(1, 100)
    guesses = 0
    print("Welcome to the AI-made Guessing Game!")
    rs.speak("Welcome to the AI-made Guessing Game! I am thinking of a number between 1 and 100. Try to guess it.")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        rs.speak("Adjusting for ambient noise. Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                print("Speak your guess...")
                rs.speak("Please speak your guess.")
                
                audio = recognizer.listen(source)
                user_guess_str = recognizer.recognize_google(audio)
                user_guess = int(user_guess_str)
                
                guesses += 1
                print(f"You guessed: {user_guess}")
                rs.speak(f"You guessed {user_guess}.")
                
                if user_guess == random_no:
                    rs.speak(f"Congratulations stout You guessed it in {guesses} attempts")
                    print("Congratulations!")
                    break 
                elif user_guess > random_no:
                    rs.speak("Too high Try a lower number")
                else:
                    rs.speak("Too low Try a higher number")

            except ValueError:
                rs.speak("That's not a valid number. Please say a number.")
            except sr.UnknownValueError:
                rs.speak("Sorry, I didn't catch that. Please try again.")
            except sr.RequestError:
                rs.speak("There was an error with the speech recognition service. Please try again later.")
                break

def main():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for activation phrase...")
        if listen_for_activation_phrase(recognizer, source):
            play_guessing_game()
if __name__ == "__main__":
    main()
