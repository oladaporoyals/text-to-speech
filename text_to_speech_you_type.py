import pyttsx3

def text_to_speech(text):
    speech_engine = pyttsx3.init()
    voice = speech_engine.getProperty('voices')
    #here you can select male or female voice, 0 = male, 1 = female
    speech_engine.setProperty('voice', voice[0].id)
    speech_engine.setProperty('voice', 4)
    speech_engine.setProperty('rate', 150)
    speech_engine.setProperty('volume', 1.0)
    speech_engine.say(text)
    speech_engine.runAndWait()
    print("ikuzo!!!")

value = input("put your words here, i would turn it to magic:")
text_to_speech(value)
#dont forget to install pip and the pyttsx3 package in your terminal
