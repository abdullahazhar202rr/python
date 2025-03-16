import speech_recognition as sr
import requests
import json
import robo_speaker as rs

if __name__=="__main__":
    try:
        while True:
            print("Welcome to Weather App")
            rs.speak("Welcome to Weather App")
            recognizer=sr.Recognizer()
            with sr.Microphone() as source:
                print("Adjusting for ambient noice.Please wait...")
                recognizer.adjust_for_ambient_noise(source)
                print("Speak the city name: ")
                rs.speak("Speak the city name")
                try:
                    audio=recognizer.listen(source)
                    command=recognizer.recognize_google(audio)
                    print(command)
                    words=command.split()
                    city=command
                    if words:
                        city=words[-1]
                    if city:
                        print(f"You said {city}")
                        rs.speak(f"The weather data for {city} is being fetched")
                    else:
                        print("Please say the city name in last")
                        rs.speak("Please say the city name in last")
                        continue
                except sr.UnknownValueError:
                    print("I couldn't understand you. Please try again.")
                    rs.speak("I couldn't understand you. Please try again.")
                    continue
                except sr.RequestError:
                    print("Could not fetch weather data from the server")
                    rs.speak("Could not fetch weather data from the server")
                    continue
            # city=input("Enter the name of city: \n")
            url=f"https://api.weatherapi.com/v1/current.json?key=bad827423b674565b06155824241309&q={city}"
            r=requests.get(url)
            weather=r.json()
            if "error" in weather:
                print("You entered wrong spellings of city kindly recheck")
                continue
            
            else:
                temp=weather['current']['temp_c']
                print(f"The temprature in {city} is {temp} degree celcius")
                rs.speak(f"The Temprature in {city} is {temp} degree celcius")
                rs.speak(("All other data has been exported to weather.txt file"))
                with open("weather.txt","w") as w:
                    w.write(json.dumps(weather,indent=4))
                    print("All data has been written in file weather\n")
    except Exception as e:
            print(f"Some Exception is showing...{e}")
            rs.speak(f"Some Exception is showing...{e}")