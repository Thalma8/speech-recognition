import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(command):

    engine.say(command)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' +song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("the current time is "+ time)
        print(time)
    elif  'who is' in command:
        person = command.replace('who is', ' ')
        info = wikipedia.summary(person, 1)
        print(info)
        talk (info)
    elif 'do you have a friend' in command:
        talk("you are my friend, i enjoy spending time with you")
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    else :
        url = 'https://www.google.com/search?q='  # Search Query Url

        search_words = command  # User inputs data as per search requirements

        webbrowser.open(url + search_words)



run_alexa()
