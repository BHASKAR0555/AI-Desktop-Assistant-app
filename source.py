import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
