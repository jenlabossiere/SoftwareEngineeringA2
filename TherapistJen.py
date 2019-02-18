import os
import JenDatabaseQueryTechnique
import cherrypy

PATH = os.path.abspath(os.path.dirname(__file__))

sOrQ = "statement"
feeling = "nothing"
subject = "normal"
questionNum = 1

class Root(object):
    @cherrypy.expose
    def index(self):
        return open('static/index.html')

    # Method that is invoked on a post request. The .ajax in index.html points to this method
    @cherrypy.expose
    @cherrypy.tools.allow(methods=('POST'))
    def therapistJenResponce(self, **data):
        global sOrQ
        global feeling
        global subject
        global questionNum

        if questionNum != 1:
            userInput = data.get("userInput")
            print(userInput)
            feeling = JenDatabaseQueryTechnique.getFeeling(userInput)
        response = JenDatabaseQueryTechnique.getResponse(sOrQ, feeling, subject, questionNum)
        questionNum += 1
        if subject == "normal" and questionNum == 7:

            questionNum = 1
        if subject == "goals" and questionNum == 6:
            questionNum = 1
        if subject == "negative thoughts" and questionNum == 6:
            questionNum = 1
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