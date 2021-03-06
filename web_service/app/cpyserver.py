from app import app

# Import CherryPy
import cherrypy
from simplejson import JSONEncoder 
import json 

if __name__ == '__main__':


    cherrypy.tree.graft(app, "/add")
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "172.17.0.28:80"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "POST", "GET"
    cherrypy.response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept, Authorization"
    #cherrypy.response.headers["Allow"] = "POST"
    #input_json = cherrypy.request.json
    cherrypy.response.headers["Content-Type"] = "application/json"
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def get_data(self):
    	cherrypy.response.headers['Content-Type'] = 'application/json'
    	datas = {"ABCDEF"}
    	return datas
    # Unsubscribe the default server
    cherrypy.server.unsubscribe()

    
    server = cherrypy._cpserver.Server()
 
    
    server.socket_host = "172.17.0.29"
    server.socket_port = 8000
    server.thread_pool = 30
     
    config = {
        'global': {
            'server.socket_host':'0.0.0.0',
            'server.socket_port': 8000,
            'log.error_file' : 'Web.log',
            'log.access_file' : 'Access.log'
        },
        '/': {
            'tools.CORS.on': True
        }
    }
   
   
    server.subscribe()
    
    

    cherrypy.engine.start()
    cherrypy.engine.block()
