
import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        return open('static/index.html')


if __name__ == '__main__':
    cherrypy.quickstart(Root(), '/')