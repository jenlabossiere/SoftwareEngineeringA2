import os
import JenDatabaseQueryTechnique
import cherrypy
import parsingStringFunctions
import threading
import socket

PATH = os.path.abspath(os.path.dirname(__file__))

sOrQ = "statement"
feeling = "nothing"
subject = "normal"
questionNum = 1
socketMessages = []

def sendData(data, IP, server):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, server))
        s.sendall(data.encode())
        s.close()

def receiveData(IP, server):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((IP, server))
        s.listen(5)
        while True:
            c, addr = s.accept()
            dataTaken = c.recv(1024).decode()
            c.close()
            socketMessages.append(dataTaken)

threading.Thread(target=receiveData, args=('206.87.3.89', 65432)).start()

class Root(object):
    @cherrypy.expose
    def index(self):
        return open('static/index.html')

    # Method that is invoked on a post request. The .ajax in index.html points to this method
    @cherrypy.expose
    @cherrypy.tools.allow(methods=('POST'))
    def listenSocketMessages(self):
        if len(socketMessages) != 0:
            return socketMessages.pop()
        else:
            return None
 
    @cherrypy.expose
    @cherrypy.tools.allow(methods=('POST'))
    def therapistJenResponce(self, **data):
        #declare theses as global variables. I would think there is another way to do this
        global sOrQ
        global feeling
        global subject
        global questionNum
        #if this isnt the first message, check if the user asked a question
        if questionNum != 1 or subject != "normal":
            userInput = data.get("userInput")
            try:
                sendData(userInput, '142.329.81.167', 65432)
            except:
                print("Connection does not work.")
            isQuestion = parsingStringFunctions.questionOrStatement(userInput)
            #if the user asked a question, reset
            if(isQuestion == "question"):
                questionNum = 1
                subject = "normal"
                sOrQ = "question"
            else:
                sOrQ = "statement"
        #if its after greetings,  if you are being asked if you a suicidial, check the user feeling, or if its the start of a new distinct topic
        if (questionNum == 2) or (questionNum == 7 and subject == "normal") or (questionNum == 3 and subject != "normal"):
            userInput = data.get("userInput")
            feeling = JenDatabaseQueryTechnique.getFeeling(userInput)
            #if you are being asked to change topics, check what the user wants
        if (subject == "normal" and questionNum == 8) or (subject == "goal" and questionNum == 7) or (subject =="negative" and questionNum == 7):
            userInput = data.get("userInput")
            #if the subject changed, go back to question 1 for that subject
            oldSubject = subject
            subject = parsingStringFunctions.negativeThoughtsOrGoals(userInput)
            if subject != oldSubject:
                questionNum = 1
        #if the user enters end the conversation, go to the end of normal
        if subject == "end the conversation":
            questionNum = 11
            subject = "normal"

        response = JenDatabaseQueryTechnique.getResponse(sOrQ, feeling, subject, questionNum)
        questionNum += 1
        print("(" + sOrQ + ", " + subject + ", " + feeling + ", " + str(questionNum) + ")")
        return response



if __name__ == '__main__':
    config={
        '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': PATH,
                'tools.staticdir.index': 'index.html',
            },
    }
    cherrypy.quickstart(Root(), '/', config)