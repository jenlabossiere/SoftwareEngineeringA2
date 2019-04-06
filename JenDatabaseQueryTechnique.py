import pyodbc
import re
import sys

server = "getrekt.database.windows.net"
database = "db_jlabossi"
username = "lindstorm"
password = "COSC310sucks"

feelingType = {

        "overwhelmed": ["overwhelm", "submerge", "overpower", "grieve", "change", "detriment", "damage", "distortion", "run", "battle damage", "operational damage", "casualty", "change of integrity", "impairment", "defacement", "wound", "burn", "defloration", "cost", "price", "asking price", "bid price", "closing price", "factory price", "highway robbery", "purchase price", "spot price", "support level", "valuation", "wrong", "injury", "concern", "worldly concern", "matter", "personal business", "part", "point of honor", "interest", "anxiety", "solicitude", "softheartedness", "sympathy", "negative stimulus", "bugaboo", "burden", "business", "enterprise", "agency", "brokerage", "carrier", "chain", "firm", "franchise", "manufacturer", "partnership", "processor", "shipbuilder", "underperformer", "refer", "fear", "alarm", "automobile horn", "burglar alarm", "device", "fire alarm", "horn", "siren", "torpedo", "signal", "air alert", "foghorn", "red flag", "tocsin", "alarm clock", "clock", "dismay", "amaze", "baffle", "diffuser", "plate", "perplex", "thwart"],
        "sad" : ["sad", "bitter", "dismal", "heartbroken", "mournful", "somber", "sorry", "wistful", "despair", "distress", "down", "hurt", "glum", "gloomy", "grieve", "heartsick", "heavyheart", "morbid", "forlorn", "ale", "bitter", "taste", "taste property", "bitterness", "acerbity", "acridity", "condition", "despair", "feeling", "hopelessness", "resignation", "discouragement", "pessimism", "pain", "distress", "anguish", "self-torture", "tsoris", "wound", "adversity", "pressure", "throe", "seizure", "straiten", "feather", "down", "duck down", "goose down", "swan", "plumule", "turn", "doctor", "highland", "hair", "lanugo", "toss off", "devour", "polish", "ill health", "brain damage", "injury", "birth trauma", "blast trauma", "bleeding", "blunt trauma", "bruise", "bump", "burn", "dislocation", "electric shock", "fracture", "frostbite", "intravasation", "penetrating trauma", "pinch", "rupture", "sting", "strain", "whiplash", "wale", "wound", "wrench", "pain", "distress", "anguish", "self-torture", "tsoris", "suffering", "agony", "throes", "discomfort", "detriment", "expense", "damage", "change of integrity", "impairment", "defacement", "defloration", "ache", "hurt", "suffer", "grieve" ],
        "angry" : ["angry","annoyed", "bitter", "enraged", "exasperated", "furious", "heated", "indignant", "offend", "resent", "sullen", "uptight", "irritate", "irratable", "mad", "fuming", "huffy", "infuriate", "raging", "rage", "sulky", "sore", "incense", "annoy", "ale", "bitter", "taste", "taste property", "bitterness", "acerbity", "acridity", "enrage", "exacerbate", "infuriate", "worsen", "heat", "inflame", "pique", "transgress", "shock", "hurt", "resent", "begrudge", "annoy", "irritate", "fume", "fumigate", "reek", "infuriate", "ramp", "rage", "torment", "annoy", "rag", "tease", "call on the carpet", "anger", "wrath", "fury", "lividity", "rage", "desire", "violence", "fashion", "fad", "ramp", "horse-drawn vehicle", "sulky", "infection", "sore", "blain", "chancre", "fester", "gall", "compound", "incense", "joss stick", "aroma", "cense", "infuriate", "container", "empty", "vacate", "evacuate"],
        "empty" : ["bare", "blank", "desert", "devoid", "dry", "hollow", "empty", "abandoned", "dead", "deflate", "deplete", "exhausted", "lacking", "lack", "vacate", "void", "bare", "publicize", "denude", "character", "space", "gap", "lacuna", "blank", "sheet", "cartridge", "biome", "desert", "tract", "arabian desert", "atacama desert", "australian desert", "black rock desert", "chihuahuan desert", "colorado desert", "dasht-e-kavir", "dasht-e-lut", "death valley", "gibson desert", "gila desert", "gobi", "great sandy desert", "great victoria desert", "kalahari", "kara kum", "kyzyl kum", "libyan desert", "mojave", "namib desert", "nefud", "negev", "nubian desert", "painted desert", "patagonian desert", "rub al-khali", "sahara", "simpson desert", "sinai", "sonoran desert", "syrian desert", "taklimakan desert", "thar desert", "abandon", "defect", "dry", "reformer", "nation", "willard", "hollow", "cavity", "dell", "valley", "burrow", "gopher hole", "hole", "kettle hole", "natural depression", "pit", "pothole", "rabbit burrow", "wormhole", "excavate", "container", "empty", "vacate", "evacuate", "abandon", "vacate", "people", "dead", "slain", "time", "deflate", "consume", "exhaust", "consume", "run down", "miss", "absence", "need", "lack", "dearth", "deficit", "mineral deficiency", "shortness", "stringency", "miss", "vacate", "revoke", "nonexistence", "nothingness", "thin air", "void", "space", "invalidate", "evacuate"],
        "suicidal" : ["dangerous", "suicide", "suicidal", "destructive", "destruct", "kill myself", "kill me", "dead", "killing", "suicide", "assisted suicide", "felo-de-se", "harakiri", "suttee", "killer", "destruct", "destroy", "termination", "killing", "deathblow", "death", "euthanasia", "homicide", "dispatch", "fell", "suicide", "slaughter", "poisoning", "suffocation", "sacrifice", "electrocution", "decapitation", "genocide", "destruction", "kill", "stamp out", "toss off", "people", "dead", "slain", "time", "frighten", "daunt", "scar"],
        "scared" : ["scared", "scare", "afraid", "fearful", "fear", "scare", "startle", "petrified", "petrify", "shaken", "terrified", "terrify", "aghast", "frighten", "daunt", "scar", "anxiety", "panic", "red scare", "fear", "scare", "frighten", "daunt", "emotion", "fear", "alarm", "creeps", "frisson", "horror", "hysteria", "panic", "scare", "stage fright", "apprehension", "timidity", "intimidation", "anxiety", "concern", "reverence", "reflex", "startle response", "startle reflex", "wince", "startle", "petrify", "lapidify", "rigidify", "petrify", "lapidify", "rigidify", "shake", "judder", "rock", "stimulate", "terrify"],
        "anxious" : ["anxious", "apprehensive", "concern", "concerned", "distressed", "distress", "fidget", "jittery", "nervous", "restless", "uneasy", "uptight", "aghast", "antsy", "disturb", "fretful", "hyper", "jumpy", "shaking", "shiver", "troubled", "wired", "concern", "worldly concern", "matter", "personal business", "part", "point of honor", "interest", "anxiety", "solicitude", "softheartedness", "sympathy", "negative stimulus", "bugaboo", "burden", "business", "enterprise", "agency", "brokerage", "carrier", "chain", "firm", "franchise", "manufacturer", "partnership", "processor", "shipbuilder", "underperformer", "refer", "concern", "straiten", "distress", "pain", "distress", "anguish", "self-torture", "tsoris", "wound", "adversity", "pressure", "throe", "seizure", "straiten", "agitation", "fidget", "impatience", "disturb", "agitate", "touch", "interrupt", "agitation", "shaking", "joggle", "motion", "tremolo", "tremor", "shake", "judder", "rock", "stimulate", "reflex", "tremble", "fear", "frisson", "shudder", "shiver", "disturb", "trouble", "perturb", "trouble oneself", "wire", "cable", "electrify"],
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

