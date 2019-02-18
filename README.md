# 310-Software-Engineering

Welcome to the world enriched by the wonderful TherapistJen!
Therapist Jen is here as a companion to help you work through negative feelings and thoughts, and help you work towards your positive goals!

Disclaimer: TherapistJen is a tool meant to help encourage positive behaviour and is designed to work alongside other methods such as professional therapy.

#Dependencies:

re, cherrypy, pyodbc, spacy, tensorflow, keras, numpy

#Components:
The functionality of the program is divided into four sections:

Web-based Platform Use - located in the "static" folder

Natural Language Processing - located in the "NLP" folder, this is used to process the user input into usable data.

Neural Network - based Machine Learning - located in the "NN+Support" folder, this is used to associate the useable data from the NLP with the feelings of the one writing the input

SQL Database Queries - located in the "JenDatabaseQueryTechniques.py" file, this is used to access the database of responses that TherapistJen has available.


#Classes:
parsingStringFunction.negativeThoughtsOrGoals(userMessage) - returns 'negative' or 'goals' as the user responds to TherapistJen

parsingStringFunction.questionOrStatement(userMessage) - determines if the userMessage is a question or a statement and returns 'question' or 'statement'

NLP_For_Training.main(userInput) - analyses the userInput and returns a matrix counting the presneces of each flagged word. Formatted for use as input for the Neural Network

JenDatabaseQueryTechniques.






