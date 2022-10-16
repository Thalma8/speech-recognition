import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', ' ')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play ' in command:
        song = command.replace('play', ' ')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("the current time is " + time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', ' ')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'what is' in command:
        thing = command.replace('what is ', ' ')
        infom = wikipedia.summary(thing, 4)
        print(infom)
        talk (infom)
    elif 'do you have a friend' in command:
        talk("you are my friend, i enjoy spending time with you")
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    else:
        url = 'https://www.google.com/search?q='  # Search Query Url

        search_words = command  # User inputs data as per search requirements

        webbrowser.open(url + search_words)


run_alexa()
