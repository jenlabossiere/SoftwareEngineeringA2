import NLP_For_Training
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pyodbc

server = "sql04.ok.ubc.ca"
database = "db_jlabossi"
username = "jlabossi"
password = "23976160"


def getResponse( sOrQ,userInput, subject, questionNum):

    #open, and read the saved model
    model = keras.models.load_model("C:\\Users\\Spencer\\Documents\\Programming\\Python\\310-Software-Engineering\\310-Software-Engineering\\NN+Support\\saved_model.h5")
    input = []
    input.append(NLP_For_Training.main(userInput))

    input = np.array(input)
    #get the probailities with the prediction
    resp_prob = model.predict(input)

    #find the catagory with the max probability
    resp_index = np.argmax(resp_prob)
    FeelingFile = open("C:\\Users\\Spencer\\Documents\\Programming\\Python\\310-Software-Engineering\\310-Software-Engineering\\NN+Support\\resp_keywords.txt","r")
    feelings = FeelingFile.read()
    feelings = feelings.split()
    feeling = feelings[resp_index]


    if questionNum <= 5:
        cnxn = pyodbc.connect(driver='{SQL Server}', host=server, database=database, user=username, password=password)
        cursor = cnxn.cursor()
        if sOrQ == "question":
            cursor.execute('SELECT response FROM ChatBot WHERE sOrQ = \'question\'')
        else:
            cursor.execute('SELECT response FROM ChatBot WHERE sOrQ = \'statement\' AND questionNum = \'' + str(questionNum) + '\'AND feeling = \'' + feeling + '\' AND subject = \'' + subject + '\'')
        for row in cursor:
            return row[0]

print(getResponse(2, "I feel dull and alnoe, I wish I was dead", "normal", 2))