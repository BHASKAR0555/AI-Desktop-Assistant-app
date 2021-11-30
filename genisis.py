# pip install pyttsx3import speech_recognition as sr #pip install speechRecognitionimport datetime
import subprocess
import re
import smtplib
import os
import wikipedia  # pip install wikipediaimport webbrowser
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)        print("Say that again please...")
        return "None" return query


# mailing someone
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bhaskar18@gmail.com', 'Gandhi1997$')
    server.sendmail('bhaskar18@gmail.com', to, content)
    server.close()


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt" with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:        query = takeCommand().lower()

        # Logic for executing tasks based on query wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # open youtube for us
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        # open google
        elif 'open google' in query:
            webbrowser.open("google.com")

        # open stackoverflow

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        # geeksforgeeks open        elif 'open geeksforgeeks' in query:
            webbrowser.open("geeksforgeeks.org")

         # open facebook
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        # play musics for me
        elif 'play music' in query:
            music_dir = 'D:\\hello'            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        # tells the current time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # open sublime text

        elif 'open code' in query:
            codePath = "C:\Program Files\Sublime Text 3\sublime_text.exe"
            os.startfile(codePath)

        # open downloads

        elif 'open downloads' in query:
            codePath = "C:\\Users\\bhaskar\\Downloads"            os.startfile(codePath)

        # open vlc media
        elif 'open vlc' in query:
            codePath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"            os.startfile(codePath)

        # send mails to anyone
        elif 'email to bhaskar' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "bhaskar18@gmail.com"                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend bhaskar. I am not able to send this email")

        # current weather at any city        elif 'current weather' in query:
            reg_ex = re.search('current weather in (.*)', query)
            if reg_ex:
                city = reg_ex.group(1)
                owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
                obs = owm.weather_at_place(city)
                w = obs.get_weather()
                k = w.get_status()
                x = w.get_temperature(unit='celsius')
                speak(
                    'Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (
                        city, k, x['temp_max'], x['temp_min']))

         # tells you the current time        elif 'time' in query:
            now = datetime.datetime.now()
            speak('Current time is %d hours %d minutes' %
                  (now.hour, now.minute))

        # can open anything website what you want        elif 'open' in query:
            reg_ex = re.search('open (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = 'https://www.' + domain
                webbrowser.open(url)
                speak('The website you have requested has been opened for you Sir.')
            else:
                pass
        # closing the chat        elif 'shutdown' in query:
            speak('Bye bye Sir. Have a nice day')
            sys.exit()

        # Your bot can fetch details of almost anything you ask her        elif 'tell me about' in query:
            reg_ex = re.search('tell me about (.*)', query)
            try:
                if reg_ex:
                    topic = reg_ex.group(1)
                    ny = wikipedia.page(topic)
                    speak(ny.content[:500].encode('utf-8'))
            except Exception as e:
                speak(e)
        # make anything note which you want to note        elif 'make a note' in query:
            NOTE_STRS = ["make a note", "write this down", "remember this"]
            for phrase in NOTE_STRS:
                if phrase in query:
                    speak("what would you like me to write?")
                    note_text = takeCommand().lower()
                    note(note_text)
                    speak("I've made a note of that.")
