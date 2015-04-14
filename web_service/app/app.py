from flask import (Flask, jsonify, request, abort, render_template)
import os
import pymongo 
from pymongo import Connection
import math
from flask.ext.cors import CORS 

app = Flask(__name__)
cors = CORS(app)
con = Connection((os.environ['DB_PORT_27017_TCP_ADDR'], os.environ['DB_PORT_27017_TCP_PORT']))
#db = con.test_database
#people = db.people

#people.insert({"name":"Lexa"})
#people.insert({"name":"Ryan"})

            
@app.route('/')
def hello_world():
    #return 'Hello Docker'
    return render_template('index.html')

app.route('/adds', methods=['POST'])
def add_args():
	if not request.json:
		abort(400)
	try:
		#name = request.json['name']
		#arg1 = request.args.get('argument1',0,type=int)
		#arg2 = request.args.get('argument2',0,type=int)
		#arg1 = request.json['argument1']
		#arg2 = request.json['argument2']
		#answer = arg1 + arg2
		#return jsonify(answer)
		con = Connection((os.environ['DB_PORT_27017_TCP_ADDR'], os.environ['DB_PORT_27017_TCP_PORT']))
		#return (jsonify({'name':name}), 200)
		
		db = con.test_database
		people = db.people

		people.insert({'argument1':arg1})
	except KeyError:
		abort(400)

@app.route('/add', methods=['POST'])

def add_args():
	if not request.json:
		abort(400)
	try:
		self.response.headers['Access-Control-Allow-Origin'] = '*'
		self.response.headers['Access-Control-Allow-Methods'] = "POST"
		arg1 = request.json['argument1']
		arg2 = request.json['argument2']
		answer = arg1 + arg2;
		return (jsonify({'answer':answer}), 200)

	except KeyError:
		abort(400)

if __name__ == '__main__':
    app.run(debug='true')
