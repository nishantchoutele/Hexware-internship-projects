import pyttsx3
import speech_recognition as sr
import wikipedia

myName = 'Firangan'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  

recognizer = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Clearing background noises... Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=1)  
        print("Ask me anything...")
        recordedaudio = recognizer.listen(source, timeout=5)  
        print("Done recording")

    print("Processing your message... Please wait")
    text = recognizer.recognize_google(recordedaudio, language='en-US')  
    print(f'Your Message: {text}')  

    try:
        wikisearch = wikipedia.summary(text, sentences=2)  
        print(f"Wikipedia Summary: {wikisearch}")
        engine.say(wikisearch) 
    except wikipedia.exceptions.DisambiguationError as e:
        print("There are multiple results for your query. Please be more specific.")
        engine.say("There are multiple results for your query. Please be more specific.")
    except wikipedia.exceptions.PageError:
        print("Sorry, I couldn't find any information on Wikipedia for your query.")
        engine.say("Sorry, I couldn't find any information on Wikipedia for your query.")
except sr.UnknownValueError:
    print("Sorry, I didn't catch that. Please speak clearly.")
    engine.say("Sorry, I didn't catch that. Please speak clearly.")
except sr.RequestError:
    print("Could not request results from Google Speech Recognition service; check your internet connection.")
    engine.say("Could not request results from Google Speech Recognition service. Please check your internet connection.")
except Exception as ex:
    print(f"An error occurred: {ex}")
    engine.say("An error occurred while processing your request.")

engine.runAndWait()
