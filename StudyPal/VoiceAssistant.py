import speech_recognition as sr
import pyttsx3
import datetime
import random
import time
import schedule
import threading
import requests
import json
import wikipedia
from PyDictionary import PyDictionary  # Install this library using: pip install wordsapi
import pyowm

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to get audio input from the user
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print("User: " + said)
        except Exception as e:
            print("I'm sorry. I didn't quite get that." + str(e))
            get_audio()
    return said

# Function to display study timetable
def display_study_timetable(weak_subject, strong_subject):
    # Implement your study timetable logic here
    print(f"Study Timetable: Weak Subject - {weak_subject}, Strong Subject - {strong_subject}")

# Function to perform calculations
def calculator():
    speak("Sure! Let's do some calculations. Please provide the arithmetic expression.")
    expression = get_audio().lower()

    try:
        result = eval(expression)
        speak(f"The result of {expression} is {result}")
    except Exception as e:
        speak(f"I'm sorry, I couldn't calculate that. Error: {e}")

def get_live_weather():
    try:
        owm = pyowm.OWM('your_owm_api_key')  # Replace 'your_owm_api_key' with your actual OpenWeatherMap API key
        observation = owm.weather_at_place('Ajman, AE') 
        w = observation.get_weather()
        wind = w.get_wind() 
        speed = wind["speed"] 
        deg = wind["deg"] 
        humidity = w.get_humidity() 
        temperature = w.get_temperature('celsius') 
        temp = temperature["temp"] 
        rain = w.get_rain() 

        if len(rain) == 0: 
            lastrain = 0
        else:
            lastrain = rain["3h"]

        speak("The current temperature is {} degree celsius. Current humidity is {} percent, and the precipitation is {} millimeters. The wind direction is at {} degrees, and the wind speed is currently at {} meters per second.".format(temp, humidity, lastrain, deg, speed))
    except Exception as e:
        speak("Weather data inaccessible. Please check your network connection.")

def search_on_wikipedia(query):
    try:
        wpsummary = wikipedia.summary(query, sentences=1)
        speak(wpsummary)
        speak("Would you like to know more?")
        reply1 = get_audio().lower()
        if reply1 in ["yes", "yeah", "sure"]:
            url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
            speak(f"You can find more information on Wikipedia: {url}")
        else:
            speak("Okay.")
    except Exception as e:
        speak("No article found for {}. {}".format(query, str(e)))

# Function to find word meaning
def find_word_meaning(word):
    dictionary = PyDictionary()
    
    try:
        meaning = dictionary.meaning(word)
        if meaning:
            speak(f"The meaning of {word} is: {meaning}")
        else:
            speak(f"No definition found for {word}")
    except Exception as e:
        speak(f"Error fetching definition for {word}. {str(e)}")

# Reminders and Notifications
def set_reminder(reminder_text, time_str):
    speak(f"Reminder: {reminder_text}")
    schedule.every().day.at(time_str).do(lambda: speak(f"Reminder: {reminder_text}"))

def set_daily_reminders():
    speak("Let's set up some daily reminders. What would you like to be reminded of?")
    reminder_text = get_audio()
    speak("At what time should I remind you? (e.g., 3:00 PM)")
    time_str = get_audio()

    try:
        datetime.datetime.strptime(time_str, "%I:%M %p")
        set_reminder(reminder_text, time_str)
        speak("Reminder set successfully.")
    except ValueError:
        speak("Sorry, I couldn't understand the time format. Please try again.")

# Time Management and Healthy Habits
def manage_time():
    speak("Let's talk about time management. How many hours do you plan to study today?")
    study_hours = int(get_audio())

    if study_hours <= 0:
        speak("That's not a valid study duration. Please enter a positive number of hours.")
    else:
        study_minutes = study_hours * 60
        speak(f"Great! Let's break it down. Divide your time among different subjects or tasks. Aim for {study_minutes} minutes of focused study.")

def remind_healthy_habits():
    speak("Don't forget to take breaks, stay hydrated, and maintain good posture during your study sessions. Your health is important!")

# Motivational Quotes
def display_motivational_quote():
    motivational_quotes = [
        "Believe you can and you're halfway there. -Theodore Roosevelt",
        "The only limit to our realization of tomorrow will be our doubts of today. -Franklin D. Roosevelt",
        "Don't watch the clock; do what it does. Keep going. -Sam Levenson",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. -Christian D. Larson",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. -Winston Churchill"
    ]

    quote = random.choice(motivational_quotes)
    speak("Here's a motivational quote for you:")
    speak(quote)

def daily_study_plan():
    set_daily_reminders()
    manage_time()
    remind_healthy_habits()
    display_motivational_quote()

# Studypal with Features
def studypal_with_features():
    speak("Hello! I am your enhanced study companion Studypal. Let's make studying even more productive!")

    while True:
        user_input = get_audio().lower()

        if "hello" in user_input:
            speak("Hi there! How can Studypal help you with your studies today?")
        elif "study timetable" in user_input:
            speak("Great! Let's create your study timetable. What is your weak subject?")
            weak_subject = get_audio()
            speak("Good choice! Now, what is your strong subject?")
            strong_subject = get_audio()
            display_study_timetable(weak_subject, strong_subject)
        elif "study tip" in user_input:
            speak("Sure! Here's a study tip: Take short breaks during your study sessions to stay focused.")
        elif "calculator" in user_input or "calculate" in user_input:
            calculator()
        elif "weather" in user_input:
            get_live_weather()
        elif "meaning of" in user_input:
            word_to_define = user_input.split("meaning of")[1].strip()
            find_word_meaning(word_to_define)
        elif "search" in user_input:
            query_to_search = user_input.split("search")[1].strip()
            search_on_wikipedia(query_to_search)
        elif "set daily reminders" in user_input:
            set_daily_reminders()
        elif "time management" in user_input:
            manage_time()
        elif "healthy habits" in user_input:
            remind_healthy_habits()
        elif "motivational quote" in user_input:
            display_motivational_quote()
        elif "daily study plan" in user_input:
            daily_study_plan()
        elif "quit" in user_input or "exit" in user_input:
            speak("Goodbye! Have a successful study session.")
            break
        else:
            speak("I'm sorry. I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    studypal_with_features()
