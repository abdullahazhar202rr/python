import os
def speak(text):
    command = f'powershell "Add-Type -AssemblyName System.Speech; ' \
                f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'
    os.system(command)

if __name__=="__main__":
    print("Welcome to RoboSpeaker made by Abdullah Azhar")
    while True:
            x=input("Enter the text you want to spoken by Computer:(or type 'exit' to quit: ")
            speak(x)
            if x.lower()=="exit":
                break


