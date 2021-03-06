# 310-Software-Engineering
Welcome to the world enriched by the wonderful TherapistJen!
Therapist Jen is here as a companion to help you work through negative feelings and thoughts, and help you work towards your positive goals!

Disclaimer: TherapistJen is a tool meant to help encourage positive behaviour and is designed to work alongside other methods such as professional therapy.

*Please note that changes made by me (Jen Labossiere) will be italisized.*


### Compiling and Running TherapistJen
To compile and run TherapistJen, one must first be either on the UBC Okanagan campus and connected to an official UBC network, or connected to myvpn.ok.ubc.ca. This will allow TherapistJen to access her database or responses. 

When running TherapistJen, first run the "TherapistJen.py" file and then follow the hyperlink address that is generated in the terminal. This will bring you to TherapistJens's chatroom.

Proceed to use TherapistJen to aid you in the maintenence of your mental health.


### Dependencies:
- re 
- cherrypy 
- pyodbc 
- spacy 
- tensorflow 
- keras 
- numpy
- *nltk*


### Components:
The functionality of the program is divided into four sections:
- Web-based Platform Use - located in the "static" folder
- Natural Language Processing - *located in the findSynonyms.py file, this is used to get more synonyms the user can say to match with our keywords*
- Neural Network - based Machine Learning - located in the "NN+Support" folder, this is used to associate the useable data from the NLP with the feelings of the one writing the input
- SQL Database Queries - located in the "JenDatabaseQueryTechniques.py" file, this is used to access the database of responses that TherapistJen has available.


### Classes:
- parsingStringFunction.negativeThoughtsOrGoals(userMessage) - returns 'negative' or 'goals' as the user responds to TherapistJen.
- parsingStringFunction.questionOrStatement(userMessage) - determines if the userMessage is a question or a statement and returns 'question' or 'statement'.
- NLP_For_Training.main(userInput) - analyses the userInput and returns a matrix counting the presneces of each flagged word. Formatted for use as input for the Neural Network.
- JenDatabaseQueryTechniques.getResponse(sOrQ, feeling, subject, questionNum) - uses input to query the SQL database for the appropriate response.
- JenDatabaseQueryTechniques.searchStringFor(userMessage, synonym) - searches userMessage for synonym and returns true if the synonym is contained within userMessage. Return false otherwise.
- JenDatabaseQueryTechniques.getFeeling(userMessage) - associates userMessage with a catagory of feeling. Returns string.

# Changes via Jen Labossiere: 

- OpenNLP use: nltk was used, as well as wordnet from nltk. To have this run effieciently, I pre-processed by running a python code and appending all new synonyms in a text file. Instead of the part of the code in JenDatabaseQueryTechnique where synonyms are mapped to a keyword, and then used to query the database, I've copied and pasted the output (a VERY long list of more synonyms) to the code. If it didn't take two hours to run, I would have kept the code in to run it with the program. This allows for the bot to have a conversation with better flow. (10 marks)

- GUI colours changed for a better aesthetic, including the "send" button being changed to "respond". As well as this, when enter is clicked on the keyboard, the message is sent, whereas before the button "send" had to be physically pressed--allows for an easier user experience. (5 marks)

- Code is included to use for sockets, which works when not connected to the UBC server. This has been implemented with another group member, Ethan Godden. Unfortunately due to the firewall with UBCO's VPN, we couldn't make a video for the submission tonight, but we are more than happy to show our work if we need to! All code for this is in TherapistJen.py (15 marks)

- The bot itself can't handle a question, so if the user enters a question mark anywhere in the input, the bot responds to the user to rephrase the question as a statement, and is redirected back to the first question such that user can start over. This improved the bot since, if a question was asked, the bot would not be able to respond directly, hence the conversation can continue. (some marks)