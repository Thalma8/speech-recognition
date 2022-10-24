import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
<<<<<<< HEAD
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(command):

    engine.say(command)
=======
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)


def talk(text):
    engine.say(text)
>>>>>>> 518289f415d868d7fd3233837010915293ef3c2d
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
<<<<<<< HEAD
            print('listening....')
=======
            print('listening...')
>>>>>>> 518289f415d868d7fd3233837010915293ef3c2d
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
<<<<<<< HEAD
                command = command.replace('alexa', '')
=======
                command = command.replace('alexa', ' ')
                print(command)
>>>>>>> 518289f415d868d7fd3233837010915293ef3c2d
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
<<<<<<< HEAD
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
=======
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
>>>>>>> 518289f415d868d7fd3233837010915293ef3c2d
    elif 'do you have a friend' in command:
        talk("you are my friend, i enjoy spending time with you")
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
<<<<<<< HEAD
    else :
=======
    else:
>>>>>>> 518289f415d868d7fd3233837010915293ef3c2d
        url = 'https://www.google.com/search?q='  # Search Query Url

        search_words = command  # User inputs data as per search requirements

        webbrowser.open(url + search_words)


<<<<<<< HEAD

=======
>>>>>>> 518289f415d868d7fd3233837010915293ef3c2d
run_alexa()
