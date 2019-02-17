import os
import cherrypy

PATH = os.path.abspath(os.path.dirname(__file__))


class Root(object):
    # display the index.html
    @cherrypy.expose
    def index(self):
        return open('static/index.html')

    # Method that is invoked on a post request. The .ajax in index.html points to this method
    @cherrypy.expose
    def therapistJenResponce(self):
        return "Therapist Jen is still at school getting her degree in Psychology"


# took out configuration because it seems to work without it
if __name__ == '__main__':
    # config = {
    #    '/': {
    #       'tools.staticdir.on': True,
    #       'tools.staticdir.dir': PATH,
    #      'tools.staticdir.index': 'index.html',
    #  },
    # }
    cherrypy.quickstart(Root(), '/')# start up the server
