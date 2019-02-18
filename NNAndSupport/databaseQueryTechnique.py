import NLP_For_Training
from tensorflow import keras
import numpy as np
import pyodbc
import os

server = "sql04.ok.ubc.ca"
database = "db_jlabossi"
username = "jlabossi"
password = "23976160"


def getResponse( sOrQ,userInput, subject, questionNum):
    fileDir = os.path.dirname(os.path.realpath('__file__'))


    #open, and read the saved model
    filename = os.path.join(fileDir, 'NNAndSupport\\saved_model.h5')
    model = keras.models.load_model(filename)
    input = []
    input.append(NLP_For_Training.main(userInput))

    input = np.array(input)
    #get the probailities with the prediction
    resp_prob = model.predict(input)

    #find the catagory with the max probability
    resp_index = np.argmax(resp_prob)
    filename = os.path.join(fileDir, 'NNAndSupport\\resp_keywords.txt')
    FeelingFile = open(filename,"r")
    feelings = FeelingFile.read()
    feelings = feelings.split()
    feeling = feelings[resp_index]
    print(feeling)

    if questionNum <= 5:
        cnxn = pyodbc.connect(driver='{SQL Server}', host=server, database=database, user=username, password=password)
        cursor = cnxn.cursor()
        if sOrQ == "question":
            cursor.execute('SELECT response FROM ChatBot WHERE sOrQ = \'question\'')
        else:
            cursor.execute('SELECT response FROM ChatBot WHERE sOrQ = \'statement\' AND questionNum = \'' + str(questionNum) + '\'AND feeling = \'' + feeling + '\' AND subject = \'' + subject + '\'')
        for row in cursor:
            return row[0]