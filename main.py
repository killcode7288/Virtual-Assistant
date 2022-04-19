from math import e
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia 
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)
engine.say("Hello i am Darlington your personal assistant....")

engine.say("I would be in sleep mode.... if you need me just say my name")
engine.runAndWait()





def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        try:
            print("Listening.......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command

        except sr.RequestError:
            talk("Sorry i didnt get that.... Try again")
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            print("Listening.......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    


def start():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        voice = listener.listen(source)
    
    command = listener.recognize_google(voice)
    if 'stephanie' in command: 
        command = command.replace("stephanie", "")
        print(command)
    

    while True:
        try:
            command = take_command()
            if "play" in command:
                song = command.replace("play", "")
                print("playing.. " + song)
                talk("playing.. " + song)
                pywhatkit.playonyt(song)
                
            elif "time" in command:
                time = datetime.datetime.now().strftime("%I:%M %p")
                print(time)
                talk(f"The time is {time}")

            elif "date" in command:
                talk("sorry, i dont do dates")
            
            elif "i love you" in command:
                talk("Aww I love you too")
                print("Aww I love you too")
            
            elif "good morning" in command:
                print("Good morning Darlington. How was your night?")
                talk("Good morning Darlington. How was your night?")
                if "fine" in command:
                        print("Great, Thank God")
                        talk("Great Thank God")
                else:
                    print("oww what is wrong?")
                    talk("oww what is wrong?")   


            status = ["are you single","are u dating","are u in a relationship","are you seeing anyone"]
            for i in status:
                if i in command:
                    talk("I am in a relationship with Darlington")

            joke = ["i am bored","boring","stress","stressed","joke"]
            for i in joke:
                if i in command:
                    print("i'll cheer you up by telling you a joke")
                    talk("i'll cheer you up by telling you a joke")
                    j = pyjokes.get_joke()
                    print(j)
                    talk(j)


            create = ["who made you", "who is your creator"]
            for i in create:
                if i in command:
                    talk("My creator is the smartest man i know, Darlington")

            intro = ["introduce yourself", "who are you", "tell me about yourself"]
            for i in intro:
                if i in command:
                    talk("I am Stephanie 2 point o your personal assistant. Designed by Darlingcorp Technologies")
                    print("I am Stephanie 2.0 your personal assistant. Designed by Darlingcorp Technologies")
            
            words = ["who is","tell me about","tell me who","search"]
            for p in words:
                if  p in command:
                    person = command.replace("wikipedia", "")
                    info = wikipedia.summary(person, 5)
                    print(info)
                    talk(info)

        except:
            talk("Sorry i didnt get that")
            print("Sorry i didnt get that")


while True: 
    start()
