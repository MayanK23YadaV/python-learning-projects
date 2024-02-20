import openai
from apikey import api_data
import pyttsx3
import speech_recognition as sr
import webbrowser


openai.api_key=api_data

completion=openai.Completion()

def Reply(question):
    prompt=f'02: {question}\n Jarvis: '
    response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\02'], max_tokens=200)
    answer=response.choices[0].text.strip()
    return answer

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Namaste what can i help you ?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening......')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("samajhne ki koshish===>")
        query=r.recognize_google(audio, language='en-in')
        print("02 Said: {} \n".format(query))
    except Exception as e:
        print("dubara boliye===>")
        return "None"
    return query


if __name__ == '__main__':
    while True:
        query=takeCommand().lower()
        ans=Reply(query)
        print(ans)
        speak(ans)
        if 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        if 'open google' in query:
            webbrowser.open("www.google.com")
        if 'thank you' in query:
            break
