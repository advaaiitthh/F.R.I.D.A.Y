from friday_main import fridaysays

ttsundayperiods = ["English", "Economics-Geography", "Second Language", "Mathematics", "Mathematics", "Chemistry", "History-Politics"]
ttmondayperiods = ["Mathematics", "Second Language", "English", "I.T.", "Moral Science", "History-Politics", "Economics-Geography"]
tttuesdayperiods = ["I.T.", "Arabic", "English", "Hindi", "Economics-Geography", "Mathematics", "Physics"]
ttwednesdayperiods = ["Physics", "Chemistry", "Mathematics", "History-Politics", "Biology", "Hindi", "English"]
ttthursdayperiods = ["Moral Education", "English", "Biology", "Mathematics", "Arabic", "Games", "Hindi"]

def ttsunday():
    line0 = ("Sunday's time table goes as follows:")
    fridaysays(line0)
    line1 = ("First period: " + ttsundayperiods[0])
    fridaysays(line1)
    line2 = ("Second period: " + ttsundayperiods[1])
    fridaysays(line2)
    line3 = ("Third period: " + ttsundayperiods[2])
    fridaysays(line3)
    line4 = ("Fourth period: " + ttsundayperiods[3])
    fridaysays(line4)
    line5 = ("Fifth period: " + ttsundayperiods[4])
    fridaysays(line5)
    line6 = ("Sixth period: " + ttsundayperiods[5])
    fridaysays(line6)
    line7 = ("Seventh period: " + ttsundayperiods[6])
    fridaysays(line7)
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
def tttoday():
    day = datetime.today().strftime('%A')
    if day == ('Sunday'):
        ttsunday()
    elif day == ('Monday'):
        ttmonday()
    elif day == ('Tuesday'):
        tttuesday()
    elif day == ('Wednesday'):
        ttwednesday()
    elif day == ('Thursday'):
        ttthursday()
    else:
        ttunscheduled = ("Today appears to be a holiday. No time table scheduled.")
        fridaysays(ttunscheduled)
def tttomorrow():
    day = datetime.today().strftime('%A')
    if day == ('Saturday'):
        ttsunday()
    elif day == ('Sunday'):
        ttmonday()
    elif day == ('Monday'):
        tttuesday()
    elif day == ('Tuesday'):
        ttwednesday()
    elif day == ('Wednesday'):
        ttthursday()
    else:
        ttunscheduled = ("Tomorrow appears to be a holiday. No time table scheduled.")
        fridaysays(ttunscheduled)