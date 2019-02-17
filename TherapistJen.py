import os
import cherrypy

PATH = os.path.abspath(os.path.dirname(__file__))


class Root(object):
    @cherrypy.expose
    def index(self):
        return open('static/index.html')


    @cherrypy.expose
    def therapistJenResponce(self):
        return "Therapist Jen is still at school getting her degree in Psychology"


if __name__ == '__main__':
   # config = {
    #    '/': {
     #       'tools.staticdir.on': True,
     #       'tools.staticdir.dir': PATH,
      #      'tools.staticdir.index': 'index.html',
      #  },
   # }
    cherrypy.quickstart(Root(), '/')

cherrypy.quickstart()
