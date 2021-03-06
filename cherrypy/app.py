import cherrypy

from cherrypy import expose
import json
import cherrypy_cors

server = cherrypy._cpserver.Server()
cherrypy.server.unsubscribe()
server.socket_host = "0.0.0.0"
server.socket_port = 8000
server.thread_pool = 30
server.subscribe()



def CORS():
    # Access-Control-Allow-Origin
    cherrypy.response.headers["Allow"] = "POST, GET"
    cherrypy.response.headers["Access-Control-Request-Headers"] = "x-requested-with"    
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
    cherrypy.response.headers["Content-Type"] = "application/json"

class cal:
	@expose
	@cherrypy.tools.json_out()
        @cherrypy.tools.json_in()
	def add(self):
		input_json = cherrypy.request.json
		no1 = input_json['argument1']
		no2 = input_json['argument1']
		answer = no1 + no2
		return answer
	add.exposed = True
if __name__ == '__main__':



 config = {
     '/': {
         'tools.CORS.on': True
     }
 }

cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)

cherrypy.engine.start()
cherrypy.engine.block()
		

