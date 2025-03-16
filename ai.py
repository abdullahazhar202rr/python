import random
import robo_speaker as rs
import speech_recognition as sr

def listen_for_activation_phrase(recognizer, source):
    rs.speak("Listening for activation phrase.")
    while True:
        audio = recognizer.listen(source)
        try:
            phrase = recognizer.recognize_google(audio).lower()
            if "hey jarvis" in phrase:
                return True
        except sr.UnknownValueError:
            continue
        except sr.RequestError:
            rs.speak("Could not request results from the service.")
            break

def play_guessing_game():
    random_no = random.randint(1, 100)
    guesses = 0
    user_guess = None
    print("Welcome to the AI-made Guessing Game!")
    rs.speak("Welcome to the AI-made Guessing Game!")
    rs.speak("I am thinking of a number between 1 and 100. Try to guess it.")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        ambient_noise_adjusted = False
        while user_guess != random_no:
            try:
                if not ambient_noise_adjusted:
                    rs.speak("Adjusting ambient noise. Please wait...")
                    recognizer.adjust_for_ambient_noise(source)
                    ambient_noise_adjusted = True
                
                print("Speak now...")
                rs.speak("Speak now...")
                audio = recognizer.listen(source)
                user_guess_str = recognizer.recognize_google(audio)
                user_guess = int(user_guess_str)
                print(f"You guessed: {user_guess}")
                rs.speak(f"You guessed the number {user_guess}")
                guesses += 1

                if user_guess == random_no:
                    print("Congratulations!")
                    rs.speak(f"Congratulations! You guessed it in {guesses} attempts.")
                elif user_guess > random_no:
                    print("Too high!")
                    rs.speak("It's too high. Enter a lower number, please.")
                elif user_guess < random_no:
                    print("Too low!")
                    rs.speak("It's too low. Enter a higher number, please.")

            except ValueError:
                print("I couldn't understand that. Please try again.")
                rs.speak("I couldn't understand that. Please say a number.")
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that. Please try again.")
                rs.speak("Sorry, I didn't catch that. Please try again.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                rs.speak("There was an error with the speech recognition service. Please try again later.")
            except Exception as e:
                print(f"Some exception occurred: {e}")
                rs.speak("Some error occurred. Please try again.")

def main():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        rs.speak("Ready to listen for activation phrase.")
        print("Listening for activation phrase...")

        # Wait for "Hey Jarvis"
        if listen_for_activation_phrase(recognizer, source):
            play_guessing_game()

if __name__ == "__main__":
    main()
