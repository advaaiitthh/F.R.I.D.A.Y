def main():
    # import statements------------------------------------------------------------------------------------------------------------------
    import os
    import time
    import playsound
    import speech_recognition as sr
    from gtts import gTTS
    import pyttsx3
    import datetime
    from datetime import datetime
    import subprocess
    import pyowm
    import random
    import webbrowser
    import requests
    import json
    import wikipedia
    from prettytable import PrettyTable as table

    from friday_reminders import reminder_sunday, reminder_monday, reminder_tuesday, reminder_wednesday, reminder_thursday, reminder_friday, reminder_saturday
    from friday_calculator import Calc

    # global variables-------------------------------------------------------------------------------------------------------------------
    ttmondayperiods = ["JAVA", "DATA_STRUCTURES", "LSD", "MINOR", "DATA_STRUCTURES", "LSD", "JAVA"]
    tttuesdayperiods = ["MATHEMATICS", "JAVA", "SUSTAINABLE_ENGINEERING", "MINOR", "PLACEMENT", "LSD", "DATA_STRUCTURES"]
    ttwednesdayperiods = ["LAB", "LAB", "LAB", "MINOR", "JAVA", "MATHEMATICS", "DESING&ENGINEERING"]
    ttthursdayperiods = ["DATA_STRUCTURES", "MATHEMATICS", "LSD", "MINOR", "LAB", "LAB", "LAB"]
    ttfridayperiods = ["DATA_STRUCTURES", "JAVA", "SUSTAINABLE_ENGINEERING", "MENTORING", "DESING&ENGINEERING", "LSD", "MATHEMATICS"]
    yesList = ["yes", "yeah", "yash", "yep,", "uh huh", "yas", "yos", "yah", "yess", "y=yes", "eyus", "ye s", "hyesb", "yes", "of course", "definitely"]
    noList = ["no", "nah", "nash", "nope", "nuh uh", "nas", "nos", "n"]
    default = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    wotdwords = [
        "Elysian", 
        "Hegemony", 
        "Extenuate", 
        "Emporium", 
        "Spitzunburg", 
        "Maugre", 
        "Viridity", 
        "Simper", 
        "Lalochezia", 
        "Rodomontade"
        ]
    wotdmeanings = [
        "relating to, or characteristics of heaven or paradise.",
        "leadership or dominance, especially by one state or social group, over others.", 
        "cause an offense to seem less serious.", 
        "a large store selling a wide variety of goods.", 
        "any of several red or yellow varieties of apple that ripen in the autumn.",
        "in spite of; notwithstanding.",
        "youth; innocence; inexperience",
        "to smile in a silly, self-conscious way.",
        "emotional relief gained by using indecent or vulgar language.",
        "boastful or inflated talk or behaviour."
        ]

    dailygoals = [
        "Speak in front of a mirror for 10 minutes today; watch yourself and tell yourself: All is well. There is nothing you can't do. I'm going to make the most out of today.",
        "Today, smile and say hello to 10 people. Watch how they respond.",
        "Watch a motivational video today, and write down what you have learnt.",
        "Write a diary entry, expressing your thoughts about last week.",
        "Today, go up to your parents, talk to them and appreciate them for everything they have done for you."
    ]

    # functions--------------------------------------------------------------------------------------------------------------------------
    
    # essentials
    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                audio = r.listen(source)
                said = ""
                try:
                    said = r.recognize_google(audio)
                    print("User: " + said)
                except Exception as e:
                    print ("I'm sorry. I didn't quite get that." + str(e))
                    get_audio()
        return said
    def fridaysays(text):
        print("Friday: " + text)
        speak(text)
    # reference
    def define(word):
            try:
                app_id = '038f0801'
                app_key = 'd7c43cea711bf14fc6ef496966c51544'
                language = 'en-gb'
                word_id = word
                fields = 'definitions'
                strictMatch = 'false'
                url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch
                r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
                definition = r.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
                fridaysays(word + " means: " + definition)
            except:
                fridaysays("No definition for " + word + " found.")
    def wiki(query):
        try:
            wpsummary = wikipedia.summary(query, sentences=1)
            fridaysays(wpsummary)
            fridaysays("Would you like to know more?")
            reply1 = input("User: ").lower()
            if reply1 in yesList:
                url = ("https://wikipedia.org/wiki/" + query)
                webbrowser.open(url, new=2)
            else:
                fridaysays("Okay.")
                pass
        except:
            try:
                wpsuggest = wikipedia.suggest(query)
                fridaysays("Did you mean " + wpsuggest + " ?")
                reply1 = input("User: ").lower()
                if reply1 in yesList:
                    wpsummary = wikipedia.summary(wpsuggest, sentences=1)
                    fridaysays(wpsummary)
                    fridaysays("Would you like to know more?")
                    reply2 = input("User: ").lower()
                    if reply2 in yesList:
                        url = ("https://wikipedia.org/wiki/" + wpsuggest)
                        webbrowser.open(url, new=2)
                    else:
                        fridaysays("Okay.")
                        pass
                else:
                    fridaysays("Okay.")
                    pass
            except:
                fridaysays("No article found for " + query)
                pass         
    def google(query):
        url = ("https://www.google.com/search?q=" + query)
        webbrowser.open(url, new=2)
    def brainly(query):
        url = ("https://brainly.in/app/ask?entry=hero&q=" + query)
        webbrowser.open(url, new=2)
    def wotd():
        n = len(wotdwords) - 1
        rand = random.randint(0,n)
        wotdword = wotdwords[rand]
        wotdmeaning = wotdmeanings[rand]
        fridaysays("Today's word of the day is: " + wotdword + ". It means: " + wotdmeaning)
    def dailygoal():
        n = len(dailygoals) - 1
        dgrand = random.randint(0,n)
        dgtoday = dailygoals[dgrand]
        fridaysays("Are you up for today's challenge?")
        dgreply = input("User: ").lower()
        if dgreply in yesList:
            fridaysays("Today's task for you is: " + dgtoday)
        else:
            fridaysays("Okay.")
            
    def weather():
        try:
            owm = pyowm.OWM('6a417670b49ae90b910a62efc4c87fda') 
            observation = owm.weather_at_place('Ajman, AE') 
            w = observation.get_weather()
            wind = w.get_wind() 
            speed = wind ["speed"] 
            deg = wind ["deg"] 
            humidity = w.get_humidity() 
            temperature = w.get_temperature('celsius') 
            temp = temperature["temp"] 
            rain = w.get_rain() 
            if len(rain) == 0: 
                lastrain = 0
            else:
                lastrain = rain["3h"]
            fridaysays("The current temperature is " + str(temp) + " degree celsius. Current humidity is " + str(humidity) + " percent and the precipitation is " + str(lastrain) + " millimetres. The wind direction is at " + str(deg) + " degrees and the wind speed is currently at " + str(speed) + " metres per second.")
        except:
            fridaysays("Weather data inaccessible. Please check your network connection.")
    # timetable
    def ttmonday():
        line0 = ("Monday's time table goes as follows:")
        fridaysays(line0)
        line1 = ("First period: " + ttmondayperiods[0])
        fridaysays(line1)
        line2 = ("Second period: " + ttmondayperiods[1])
        fridaysays(line2)
        line3 = ("Third period: " + ttmondayperiods[2])
        fridaysays(line3)
        line4 = ("Fourth period: " + ttmondayperiods[3])
        fridaysays(line4)
        line5 = ("Fifth period: " + ttmondayperiods[4])
        fridaysays(line5)
        line6 = ("Sixth period: " + ttmondayperiods[5])
        fridaysays(line6)
        line7 = ("Seventh period: " + ttmondayperiods[6])
        fridaysays(line7)
    def tttuesday():
        line0 = ("Tuesday's time table goes as follows:")
        fridaysays(line0)
        line1 = ("First period: " + tttuesdayperiods[0])
        fridaysays(line1)
        line2 = ("Second period: " + tttuesdayperiods[1])
        fridaysays(line2)
        line3 = ("Third period: " + tttuesdayperiods[2])
        fridaysays(line3)
        line4 = ("Fourth period: " + tttuesdayperiods[3])
        fridaysays(line4)
        line5 = ("Fifth period: " + tttuesdayperiods[4])
        fridaysays(line5)
        line6 = ("Sixth period: " + tttuesdayperiods[5])
        fridaysays(line6)
        line7 = ("Seventh period: " + tttuesdayperiods[6])
        fridaysays(line7)
    def ttwednesday():
        line0 = ("Wednesday's time table goes as follows:")
        fridaysays(line0)
        line1 = ("First period: " + ttwednesdayperiods[0])
        fridaysays(line1)
        line2 = ("Second period: " + ttwednesdayperiods[1])
        fridaysays(line2)
        line3 = ("Third period: " + ttwednesdayperiods[2])
        fridaysays(line3)
        line4 = ("Fourth period: " + ttwednesdayperiods[3])
        fridaysays(line4)
        line5 = ("Fifth period: " + ttwednesdayperiods[4])
        fridaysays(line5)
        line6 = ("Sixth period: " + ttwednesdayperiods[5])
        fridaysays(line6)
        line7 = ("Seventh period: " + ttwednesdayperiods[6])
        fridaysays(line7)
    def ttthursday():
        line0 = ("Thursday's time table goes as follows:")
        fridaysays(line0)
        line1 = ("First period: " + ttthursdayperiods[0])
        fridaysays(line1)
        line2 = ("Second period: " + ttthursdayperiods[1])
        fridaysays(line2)
        line3 = ("Third period: " + ttthursdayperiods[2])
        fridaysays(line3)
        line4 = ("Fourth period: " + ttthursdayperiods[3])
        fridaysays(line4)
        line5 = ("Fifth period: " + ttthursdayperiods[4])
        fridaysays(line5)
        line6 = ("Sixth period: " + ttthursdayperiods[5])
        fridaysays(line6)
        line7 = ("Seventh period: " + ttthursdayperiods[6])
        fridaysays(line7)
    def ttfriday():
        line0 = ("Friday's time table goes as follows:")
        fridaysays(line0)
        line1 = ("First period: " + ttfridayperiods[0])
        fridaysays(line1)
        line2 = ("Second period: " + ttfridayperiods[1])
        fridaysays(line2)
        line3 = ("Third period: " + ttfridayperiods[2])
        fridaysays(line3)
        line4 = ("Fourth period: " + ttfridayperiods[3])
        fridaysays(line4)
        line5 = ("Fifth period: " + ttfridayperiods[4])
        fridaysays(line5)
        line6 = ("Sixth period: " + ttfridayperiods[5])
        fridaysays(line6)
        line7 = ("Seventh period: " + ttfridayperiods[6])
        fridaysays(line7)
    def tttoday():
        day = datetime.today().strftime('%A')
        if day == ('Monday'):
            ttsunday()
        elif day == ('Tuesday'):
            ttmonday()
        elif day == ('Wednesday'):
            tttuesday()
        elif day == ('Thursday'):
            ttwednesday()
        elif day == ('Friday'):
            ttthursday()
        else:
            ttunscheduled = ("Today appears to be a holiday. No time table scheduled.")
            fridaysays(ttunscheduled)
    def tttomorrow():
        day = datetime.today().strftime('%A')
        if day == ('Sunday'):
            ttmonday()
        elif day == ('Monday'):
            tttuesday()
        elif day == ('Tuesday'):
            ttwednesday()
        elif day == ('Wednesday'):
            ttthursday()
        elif day == ('Thursday'):
            ttfriday()
        else:
            ttunscheduled = ("Tomorrow appears to be a holiday. No time table scheduled.")
            fridaysays(ttunscheduled)
    def ttall():
        fridaysays("Here's the time table for the whole week:")
        classtt = table(['Day', '1st Period', '2nd Period', '3rd Period', '4th Period', '5th Period', '6th Period', '7th Period'])
        classtt.add_row(['Monday', ttmondayperiods[0], ttmondayperiods[1], ttmondayperiods[2], ttmondayperiods[3], ttmondayperiods[4], ttmondayperiods[5], ttmondayperiods[6]])
        classtt.add_row(['Tuesday', tttuesdayperiods[0], tttuesdayperiods[1], tttuesdayperiods[2],tttuesdayperiods[3], tttuesdayperiods[4], tttuesdayperiods[5], tttuesdayperiods[6]])
        classtt.add_row(['Wednesday', ttwednesdayperiods[0],  ttwednesdayperiods[1],  ttwednesdayperiods[2],  ttwednesdayperiods[3],  ttwednesdayperiods[4],  ttwednesdayperiods[5],  ttwednesdayperiods[6]])
        classtt.add_row(['Thursday', ttthursdayperiods[0], ttthursdayperiods[1], ttthursdayperiods[2], ttthursdayperiods[3], ttthursdayperiods[4], ttthursdayperiods[5], ttthursdayperiods[6]])
        classtt.add_row(['Friday', ttfridayperiods[0], ttfridayperiods[1], ttfridayperiods[2], ttfridayperiods[3], ttfridayperiods[4], ttfridayperiods[5], ttfridayperiods[6]])
        print(classtt)
    def examtt():
        fridaysays("Exam time? Let's get started!")
        fridaysays("Enter three of your strongest subjects:")
        strongsubject1 = input("User: Strong subject 1 - ")
        strongsubject2 = input("User: Strong subject 2 - ")
        strongsubject3 = input("User: Strong subject 3 - ")
        fridaysays("Great! Now enter three of your rather weak subjects:")
        weaksubject1 = input("User: Weak subject 1 - ")
        weaksubject2 = input("User: Weak subject 2 - ")
        weaksubject3 = input("User: Weak subject 3 - ")
        fridaysays("Generating schedule...")
        examtt = table(['Day', 'Hour 1', 'Hour 2', 'Hour 3', 'Hour 4'])
        examtt.add_row(['Day 1', strongsubject3, strongsubject3, strongsubject3, weaksubject2])
        examtt.add_row(['Day 2', weaksubject2, weaksubject2, weaksubject2, strongsubject3])
        examtt.add_row(['Day 3', weaksubject1, weaksubject1, weaksubject1, weaksubject3])
        examtt.add_row(['Day 4', weaksubject3, weaksubject3, weaksubject3, weaksubject1])
        examtt.add_row(['Day 5', strongsubject2, strongsubject2, weaksubject2 + " (Revision)", weaksubject2 + " (Revision)"])
        examtt.add_row(['Day 6', strongsubject1, strongsubject1, weaksubject1 + " (Revision)", weaksubject1 + " (Revision)"])
        examtt.add_row(['Day 7', weaksubject3 + " (Revision)", weaksubject3 + " (Revision)", strongsubject3 + " (Revision)", strongsubject3 + " (Revision)"])
        print(examtt)
        fridaysays("Here goes your prescribed time table. Best of luck!")
    # set reminder
    def srsunday():
        fridaysays("What would you like to be reminded?")
        reminder_task = input("User: ").lower()
        if reminder_sunday[0] == "1":
            reminder_sunday[0] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Sunday.")
        elif reminder_sunday[1] == "2":
            reminder_sunday[1] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Sunday.")
        elif reminder_sunday[2] == "3":
            reminder_sunday[2] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Sunday.")
        elif reminder_sunday[3] == "4":
            reminder_sunday[3] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Sunday.")
        elif reminder_sunday[4] == "5":
            reminder_sunday[4] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Sunday.")
        elif reminder_sunday[5] == "6":
            reminder_sunday[5] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Sunday.")
        elif reminder_sunday[6] == "7":
            reminder_sunday[6] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Sunday.")
        elif reminder_sunday[7] == "8":
            reminder_sunday[7] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Sunday.")
        elif reminder_sunday[8] == "9":
            reminder_sunday[8] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Sunday.")
        elif reminder_sunday[9] == "10":
            reminder_sunday[9] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Sunday.")
    def srmonday():
        fridaysays("What would you like to be reminded?")
        reminder_task = input("User: ").lower()
        if reminder_monday[0] == "1":
            reminder_monday[0] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Monday.")
        elif reminder_monday[1] == "2":
            reminder_monday[1] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Monday.")
        elif reminder_monday[2] == "3":
            reminder_monday[2] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Monday.")
        elif reminder_monday[3] == "4":
            reminder_monday[3] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Monday.")
        elif reminder_monday[4] == "5":
            reminder_monday[4] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Monday.")
        elif reminder_monday[5] == "6":
            reminder_monday[5] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Monday.")
        elif reminder_monday[6] == "7":
            reminder_monday[6] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Monday.")
        elif reminder_monday[7] == "8":
            reminder_monday[7] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Monday.")
        elif reminder_monday[8] == "9":
            reminder_monday[8] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Monday.")
        elif reminder_monday[9] == "10":
            reminder_monday[9] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Monday.")
    def srtuesday():
        fridaysays("What would you like to be reminded?")
        reminder_task = input("User: ").lower()
        if reminder_tuesday[0] == "1":
            reminder_tuesday[0] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Tuesday.")
        elif reminder_tuesday[1] == "2":
            reminder_tuesday[1] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Tuesday.")
        elif reminder_tuesday[2] == "3":
            reminder_tuesday[2] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Tuesday.")
        elif reminder_tuesday[3] == "4":
            reminder_tuesday[3] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Tuesday.")
        elif reminder_tuesday[4] == "5":
            reminder_tuesday[4] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Tuesday.")
        elif reminder_tuesday[5] == "6":
            reminder_tuesday[5] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Tuesday.")
        elif reminder_tuesday[6] == "7":
            reminder_tuesday[6] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Tuesday.")
        elif reminder_tuesday[7] == "8":
            reminder_tuesday[7] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Tuesday.")
        elif reminder_tuesday[8] == "9":
            reminder_tuesday[8] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Tuesday.")
        elif reminder_tuesday[9] == "10":
            reminder_tuesday[9] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Tuesday.")
    def srwednesday():
        fridaysays("What would you like to be reminded?")
        reminder_task = input("User: ").lower()
        if reminder_wednesday[0] == "1":
            reminder_wednesday[0] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Wednesday.")
        elif reminder_wednesday[1] == "2":
            reminder_wednesday[1] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Wednesday.")
        elif reminder_wednesday[2] == "3":
            reminder_wednesday[2] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Wednesday.")
        elif reminder_wednesday[3] == "4":
            reminder_wednesday[3] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Wednesday.")
        elif reminder_wednesday[4] == "5":
            reminder_wednesday[4] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Wednesday.")
        elif reminder_wednesday[5] == "6":
            reminder_wednesday[5] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Wednesday.")
        elif reminder_wednesday[6] == "7":
            reminder_wednesday[6] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Wednesday.")
        elif reminder_wednesday[7] == "8":
            reminder_wednesday[7] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Wednesday.")
        elif reminder_wednesday[8] == "9":
            reminder_wednesday[8] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Wednesday.")
        elif reminder_wednesday[9] == "10":
            reminder_wednesday[9] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Wednesday.")
    def srthursday():
        fridaysays("What would you like to be reminded?")
        reminder_task = input("User: ").lower()
        if reminder_thursday[0] == "1":
            reminder_thursday[0] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Thursday.")
        elif reminder_thursday[1] == "2":
            reminder_thursday[1] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Thursday.")
        elif reminder_thursday[2] == "3":
            reminder_thursday[2] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Thursday.")
        elif reminder_thursday[3] == "4":
            reminder_thursday[3] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Thursday.")
        elif reminder_thursday[4] == "5":
            reminder_thursday[4] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Thursday.")
        elif reminder_thursday[5] == "6":
            reminder_thursday[5] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Thursday.")
        elif reminder_thursday[6] == "7":
            reminder_thursday[6] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Thursday.")
        elif reminder_thursday[7] == "8":
            reminder_thursday[7] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Thursday.")
        elif reminder_thursday[8] == "9":
            reminder_thursday[8] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Thursday.")
        elif reminder_thursday[9] == "10":
            reminder_thursday[9] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Thursday.")
    def srfriday():
        fridaysays("What would you like to be reminded?")
        reminder_task = input("User: ").lower()
        if reminder_friday[0] == "1":
            reminder_friday[0] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Friday.")
        elif reminder_friday[1] == "2":
            reminder_friday[1] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Friday.")
        elif reminder_friday[2] == "3":
            reminder_friday[2] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Friday.")
        elif reminder_friday[3] == "4":
            reminder_friday[3] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Friday.")
        elif reminder_friday[4] == "5":
            reminder_friday[4] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Friday.")
        elif reminder_friday[5] == "6":
            reminder_friday[5] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Friday.")
        elif reminder_friday[6] == "7":
            reminder_friday[6] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Friday.")
        elif reminder_friday[7] == "8":
            reminder_friday[7] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Friday.")
        elif reminder_friday[8] == "9":
            reminder_friday[8] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Friday.")
        elif reminder_friday[9] == "10":
            reminder_friday[9] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Friday.")
    def srsaturday():
        fridaysays("What would you like to be reminded?")
        reminder_task = input("User: ").lower()
        if reminder_saturday[0] == "1":
            reminder_saturday[0] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Saturday.")
        elif reminder_saturday[1] == "2":
            reminder_saturday[1] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Saturday.")
        elif reminder_saturday[2] == "3":
            reminder_saturday[2] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Saturday.")
        elif reminder_saturday[3] == "4":
            reminder_saturday[3] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Saturday.")
        elif reminder_saturday[4] == "5":
            reminder_saturday[4] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Saturday.")
        elif reminder_saturday[5] == "6":
            reminder_saturday[5] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Saturday.")
        elif reminder_saturday[6] == "7":
            reminder_saturday[6] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Saturday.")
        elif reminder_saturday[7] == "8":
            reminder_saturday[7] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Saturday.")
        elif reminder_saturday[8] == "9":
            reminder_saturday[8] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Saturday.")
        elif reminder_saturday[9] == "10":
            reminder_saturday[9] = reminder_task
            fridaysays("Done! " + reminder_task + " set for Saturday.")
    def srtoday():
        day = datetime.today().strftime('%A')
        if day == ('Sunday'):
            srsunday()
        elif day == ('Monday'):
            srmonday()
        elif day == ('Tuesday'):
            srtuesday()
        elif day == ('Wednesday'):
            srwednesday()
        elif day == ('Thursday'):
            srthursday()
        elif day == ('Friday'):
            srfriday()
        elif day == ('Saturday'):
            srsaturday()
    def srtomorrow():
        day = datetime.today().strftime('%A')
        if day == ('Sunday'):
            srmonday()
        elif day == ('Monday'):
            srtuesday()
        elif day == ('Tuesday'):
            srwednesday()
        elif day == ('Wednesday'):
            srthursday()
        elif day == ('Thursday'):
            srfriday()
        elif day == ('Friday'):
            srsaturday()
        elif day == ('Saturday'):
            srsunday()
    # remind me
    def rmsunday():
        for x in reminder_sunday:
            if x not in default:
                fridaysays(x)
            else:
                fridaysays("End of reminders for this day.")
                break
    def rmmonday():
        for x in reminder_monday:
            if x not in default:
                fridaysays(x)
            else:
                fridaysays("End of reminders for this day.")
                break
    def rmtuesday():
        for x in reminder_tuesday:
            if x not in default:
                fridaysays(x)
            else:
                fridaysays("End of reminders for this day.")
                break
    def rmwednesday():
        for x in reminder_wednesday:
            if x not in default:
                fridaysays(x)
            else:
                fridaysays("End of reminders for this day.")
                break
    def rmthursday():
        for x in reminder_thursday:
            if x not in default:
                fridaysays(x)
            else:
                fridaysays("End of reminders for this day.")
                break
    def rmfriday():
        default = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for x in reminder_friday:
            if x not in default:
                fridaysays(x)
            else:
                fridaysays("End of reminders for this day.")
                break
    def rmsaturday():
        for x in reminder_saturday:
            if x not in default:
                fridaysays(x)
            else:
                fridaysays("End of reminders for this day.")
    def rmtoday():
        day = datetime.today().strftime('%A')
        if day == ('Sunday'):
            rmsunday()
        elif day == ('Monday'):
            rmmonday()
        elif day == ('Tuesday'):
            rmtuesday()
        elif day == ('Wednesday'):
            rmwednesday()
        elif day == ('Thursday'):
            rmthursday()
        elif day == ('Friday'):
            rmfriday()
        elif day == ('Saturday'):
            rmsaturday()
    def rmtomorrow():
        day = datetime.today().strftime('%A')
        if day == ('Sunday'):
            rmmonday()
        elif day == ('Monday'):
            rmtuesday()
        elif day == ('Tuesday'):
            rmwednesday()
        elif day == ('Wednesday'):
            rmthursday()
        elif day == ('Thursday'):
            rmfriday()
        elif day == ('Friday'):
            rmsaturday()
        elif day == ('Saturday'):
            rmsunday()

    # initial conversation---------------------------------------------------------------------------------------------------------------
    greeting = ("What can I help you with?")
    fridaysays(greeting)

    text = input("User: ").lower()
  
    # user commands----------------------------------------------------------------------------------------------------------------------
    
    # 1
    GOODMORNING_STRS = ["morning", "good morning", "mourning", "morn"]
    for phrase in GOODMORNING_STRS:
        if phrase in text:
            fridaysays("Good morning! Would you like me to get you started for the day?")
            choice = input("User:").lower()
            if choice in yesList:
                wotd()
                rmtoday()
                dailygoal()
                break
            else:
                fridaysays("Okay. Have a nice day today!")
                break
    # 2
    TIMETABLE_STRS = ["time table", "timetable", "periods"]
    for phrase in TIMETABLE_STRS:
        if phrase in text:
            fridaysays("What day?")
            ttday = input("User: ").lower()
            if "monday" in ttday:
                ttmonday()
            elif "tuesday" in ttday:
                tttuesday()
            elif "wednesday" in ttday:
                ttwednesday()
            elif "thursday" in ttday:
                ttthursday()
            elif "friday" in ttday:
                ttfriday()
            elif "today" in ttday:
                tttoday()
            elif "tomorrow" in ttday:
                tttomorrow()
            elif "all" in ttday:
                ttall()
            elif "full" in ttday:
                ttall()
            elif "entire" in ttday:
                ttall()
            else:
                fridaysays("No time table for that day.")
    # 9
    HELLO_STRS = ["hello", "hey", "whats up", "how are you", "hi"]
    for phrase in HELLO_STRS:
        if phrase in text:
            reply = "Hello!"
            fridaysays(reply)
            break
    # 10
    NAME_STRS = ["what is your name,", "your name", "what is name"]
    for phrase in NAME_STRS:
        if phrase in text:
            reply = "My name is Friday, pleased to meet you."
            fridaysays(reply)
            break
    # 11
    WHOAMI_STRS = ["who am I", "who", "who i am"]
    for phrase in WHOAMI_STRS:
        if phrase in text:
            fridaysays("Your name is Advaith.")
            break
    # 12
    GOOGLE_STRS = ["google search", "search", "google"]
    for phrase in GOOGLE_STRS:
        if phrase in text:
            fridaysays("What would you like to search for?")
            query = input("User: ")
            fridaysays("Searching for " + query + "...")
            google(query)
            break
    # 13
    WIKIPEDIA_STRS = ["wikipedia", "wiki"]
    for phrase in WIKIPEDIA_STRS:
        if phrase in text:
            fridaysays("What would you like to search on Wikipedia?")
            query = input("User: ")
            fridaysays("Searching for " + query + " on Wikipedia...")
            wiki(query)
            break
    # 14
    WEATHER_STRS = ["current weather", "weather", "current temperature", "temperature"]
    for phrase in WEATHER_STRS:
        if phrase in text:
            weather()
            break
    # 15
    WOTD_STRS = ["word of the day", "word of the day today", "word today", "word for the day"]
    for phrase in WOTD_STRS:
        if phrase in text:
            wotd()
            break
    # 16
    SINGSONG_STRS = ["sing a song", "song"]
    for phrase in SINGSONG_STRS:
        if phrase in text:
            fridaysays("La La La La La La La La.... yup I do not know how to sing.")
            break
    # 17
    DEFINITION_STRS = ["define", "definition", "dictionary", "find meaning"]
    for phrase in DEFINITION_STRS:
        if phrase in text:
            fridaysays("Which word would you like to define?")
            text = input("User: ").lower()
            define(text)
            break
    # 18
    SETREMINDER_STRS = ["set reminder", "set a reminder", "keep reminder", "keep a reminder", "make reminder", "make a reminder", "put reminder", "put a reminder"]
    for phrase in SETREMINDER_STRS:
        if phrase in text:
            fridaysays("When would you like to set the reminder for?")
            srday = input("User: ").lower()
            if "sunday" in srday:
                srsunday()
            elif "monday" in srday:
                srmonday()
            elif "tuesday" in srday:
                srtuesday()
            elif "wednesday" in srday:
                srwednesday()
            elif "thursday" in srday:
                srthursday()
            elif "friday" in srday:
                srfriday()
            elif "saturday" in srday:
                srsaturday()
            elif "today" in srday:
                srtoday()
            elif "tomorrow" in srday:
                srtomorrow()
            else:
                print("Error: Unspecified date!")
            break
    # 19
    REMINDME_STRS = ["remind me", "show tasks", "show reminders", "what reminders", "what are reminders", "what are my reminders", "do i have any reminders", "do i have reminders"]
    for phrase in REMINDME_STRS:
        if phrase in text:
            fridaysays("Which day?")
            rmday = input("User: ").lower()
            if "sunday" in rmday:
                rmsunday()
            elif "monday" in rmday:
                rmmonday()
            elif "tuesday" in rmday:
                rmtuesday()
            elif "wednesday" in rmday:
                rmwednesday()
            elif "thursday" in rmday:
                rmthursday()
            elif "friday" in rmday:
                rmfriday()
            elif "saturday" in rmday:
                rmsaturday()
            elif "today" in rmday:
                rmtoday()
            elif "tomorrow" in rmday:
                rmtomorrow()
            else:
                print("Error: Unspecified date!")
            break
    # 20
    EXAM_STRS = ["exam"]
    for phrase in EXAM_STRS:
        if phrase in text:
            examtt()
            break
    # 21
    CALCULATE_STRS = ["calculate", "calculator", "calculus", "add", "subtract", "multiply", "divide"]
    for phrase in CALCULATE_STRS:
        if phrase in text:
            fridaysays("Okay, give me an equation!")
            ccquery = (input("User: "))
            try:
                fridaysays("The answer to that is " + str(Calc.evaluate(ccquery)) + ".")
            except Exception as e:
                fridaysays("An error occured; couldn't solve equation.")
                print(str(e))
    # 22
    HOMEWORK_STRS = ["homework", "home work"]
    for phrase in HOMEWORK_STRS:
        if phrase in text:
            fridaysays("What subject would you like help with?")
            hhsubject = input("User: ").lower()
            fridaysays("I see... What are you having trouble with?")
            hhquery = input("User: ").lower()
            if "math" in hhsubject:
                fridaysays("Oooh... Let me see if I can search something up on Brainly!")
                brainly(hhquery)
            elif "sci" in hhsubject:
                fridaysays("Oooh... Let me see if I can search something up on Brainly!")
                brainly(hhquery)
            elif "social" in hhsubject:
                fridaysays("Maybe a Wikipedia search would assist you?")
                wiki(hhquery)
            else:
                fridaysays("Ah! Let me search that up for you...")
                google(hhquery)
                break
            fridaysays("Did that help?")
            hhrestart = input("User: ").lower()
            if hhrestart in noList:
                fridaysays("Oh... let me do a web search then.")
                google(hhquery)
            else:
                break

    # 23
    DAILYGOALS_STRS = ["daily goal"]
    for phrase in DAILYGOALS_STRS:
        if phrase in text:
            dailygoal()
            break

    #restart conversation----------------------------------------------------------------------------------------------------------------
    fridaysays("Is there anything else I can help you with?")
    print("Please answer with 'yes' or 'no'.")
    restart = input("User: ").lower()
    if restart in yesList:
        main()
    elif restart == (""):
        main()
    else:
        fridaysays("Thank you for using Friday. Have a nice day!")
        exit

main()  