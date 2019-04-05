import pyodbc
import re
import sys

server = "sql04.ok.ubc.ca"
database = "db_jlabossi"
username = "jlabossi"
password = "23976160"

feelingType = {

        "overwhelmed": ["overwhelm", "grieve", "damage", "overwrought", "concern", "alarm", "astonish", "baffle"],
        "sad" : ["sad", "bitter", "dismal", "heartbroken", "mournful", "somber", "sorry", "wistful", "despair", "distress", "down", "hurt", "glum", "gloomy", "grieve", "heartsick", "heavyheart", "morbid", "forlorn"],
        "angry" : ["angry","annoyed", "bitter", "enraged", "exasperated", "furious", "heated", "indignant", "offend", "resent", "sullen", "uptight", "irritate", "irratable", "mad", "fuming", "huffy", "infuriate", "raging", "rage", "sulky", "sore", "incense"],
        "empty" : ["bare", "blank", "desert", "devoid", "dry", "hollow", "empty", "abandoned", "dead", "deflate", "deplete", "exhausted", "lacking", "lack", "vacate", "void"],
        "suicidal" : ["dangerous", "suicide", "suicidal", "destructive", "destruct", "kill myself", "kill me", "dead"],
        "scared" : ["scared", "scare", "afraid", "fearful", "fear", "scare", "startle", "petrified", "petrify", "shaken", "terrified", "terrify", "aghast"],
        "anxious" : ["anxious", "apprehensive", "concern", "concerned", "distressed", "distress", "fidget", "jittery", "nervous", "restless", "uneasy", "uptight", "aghast", "antsy", "disturb", "fretful", "hyper", "jumpy", "shaking", "shiver", "troubled", "wired"],
    }


def getResponse(sOrQ, feeling, subject, questionNum):
    if questionNum <= 30:
        dbstring = ('{ODBC Driver 17 for SQL Server}', '{SQL Server}') [sys.platform == 'win32']
        cnxn = pyodbc.connect(driver=dbstring, host=server, database=database, user=username, password=password)
        cursor = cnxn.cursor()
        if sOrQ == "question":
            cursor.execute('SELECT response FROM ChatBot WHERE sOrQ = \'question\'')
        else:
            cursor.execute('SELECT response FROM ChatBot WHERE sOrQ = \'statement\' AND questionNum = \'' + str(questionNum) + '\'AND feeling = \'' + feeling + '\' AND subject = \'' + subject + '\'')
        for row in cursor:
            return row[0]

def searchStringFor(userMessage, synonym):
    matchAsRegex = re.search(synonym, userMessage)
    return bool(matchAsRegex)

def getFeeling(userMessage):
    for feeling in feelingType :
        synonyms = feelingType.get(feeling, "default")
        for synonym in synonyms:
            if searchStringFor(userMessage, synonym):
                return feeling
    return "nothing"

