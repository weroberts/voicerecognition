#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import os


def launchApp(app):
    app=app.lower()
    print("opening " + app)
    if (app == "notepad"):
        os.system("notepad.exe")
    elif (app in ["chrome", "google chrome"]):
        os.system("start chrome")
    elif (app == "notepad plus plus"):
        os.system('"C:/Program Files/Notepad++/notepad++.exe"')
    elif (app in ["firefox", "fire fox"]):
        os.system('"C:/Program Files/Mozilla Firefox/firefox.exe"')

def search(searchTerm):
    os.system("start chrome " + searchTerm)

def callCommand(audioString):
    try:
        command = audioString.split(' ', 1)[0]
        arguments = audioString.split(' ', 1)[1]

        if (command == "open"):
            launchApp(arguments)
        elif (command == "search"):
            search(arguments)
    except:
        print("that wasn't a valid command")

# obtain audio from the microphone
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        audioString = r.recognize_google(audio)
        print(audioString)
        callCommand(audioString)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


