import datetime
import pyttsx3  # this module is for voices
import speech_recognition as sr
import wikipedia
import webbrowser

# import PyAudio

engine = pyttsx3.init('sapi5')  # sapi is speech API for voice recognition and synthesis
voices = engine.getProperty('voices')
# print(voices[0].id)  # 1 for female voice and 0 for male voice
engine.setProperty('voice', voices[0].id)  #


# pyaudio.PyAudio()
def speak(audio):  # function
    """This function when called will speack what ever is written"""  # this is a doc string
    # we can se this by print(speak.__doc__)
    # print([functionKaNaam].__doc__)
    engine.say(audio)
    engine.runAndWait()


def wishMe():  # function
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:  # hour >=0 and hour<12: i.e 0 se 12 k bich
        speak("Good Morning!")

    elif 12 <= hour < 18:  # 12 se 18 k bich agar time h
        speak("Good Afternoon!")


    else:
        speak("Good Evening")

    speak("Hello, i am Babu, How may i  help you sir.")


def takeCommand():
    # takes audio command and returns string

    r = sr.Recognizer()  # recognizer class will help in recognising audio
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # this is for a little pause before taking voice input
        audio = r.listen(source)

    try:
        print("Recognising..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n")

    except Exception as e:
        # print(e)
        print("Say that again please..")
        return "None"
    return query


# def sendEmail(to , content):
if __name__ == "__main__":
    # speak(" Hello this is babu.")
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing our tasks
        if 'wikipedia' in query:
            speak('searching Wikipedia..!')
            # Query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            speak('Opening Google...!')
            webbrowser.open("www.google.com ")

        elif 'open youtube' in query:
            speak('Opening YouTube...!')
            webbrowser.open("www.youtube.com ")

        elif 'stack overflow' in query:
            speak('Opening stackoverflow...!')
            webbrowser.open("stackoverflow.com ")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")
            
         elif "read today's news" in query:
            speak("News for today.. Lets begin")
            url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=d093053d72bc40248998159804e0e67d"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            for article in arts:
                print(article['title'])
                speak(article['title'])

                speak("Moving on to the next news..")

            speak("Thanks for listening...")

        # elif 'email to' in query:
        #     try:
        #         speak("to whom ?")
        #         emailId = input("Enter email id : ")
        #         speak("What should i say ?")
        #         content = takeCommand()
        #         to = emailId
        #         sendEmail(to,content)

        elif 'who are you' in query:
            speak("I am babu, i am jarvis's indian cousin ")
    # pass
