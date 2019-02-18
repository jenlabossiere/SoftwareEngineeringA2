import NLP_For_Training
import tensorflow as tf
import numpy as np

import pyodbc
import re

server = "sql04.ok.ubc.ca"
database = "db_jlabossi"
username = "jlabossi"
password = "23976160"

def getResponse(sOrQ, feeling, subject, questionNum):
    if questionNum <= 5:
        cnxn = pyodbc.connect(driver='{SQL Server}', host=server, database=database, user=username, password=password)
        cursor = cnxn.cursor()
        if sOrQ == "question":
            cursor.execute('SELECT response FROM ChatBot WHERE sOrQ = \'question\'')
        else:
            cursor.execute('SELECT response FROM ChatBot WHERE sOrQ = \'statement\' AND questionNum = \'' + str(questionNum) + '\'AND feeling = \'' + feeling + '\' AND subject = \'' + subject + '\'')
        for row in cursor:
            return row[0]




def getResponse(userInput):

    modelFile = open("C:\\Users\\Spencer\\Documents\\Programming\\Python\\310-Software-Engineering\\310-Software-Engineering\\NN+Support\\saved_model", "r")
    modelString = modelFile.read()

    model = tf.keras.models.model_from_json(modelString)

    resp_prob = model.predict(NLP_For_Training.main(userInput))

    np.argmax(resp_prob)
    



