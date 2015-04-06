from flask import (Flask, jsonify, request, abort, render_template)

import pymongo 
from pymongo import Connection
import math
app = Flask(__name__)

#con = Connection("172.17.0.2:27017")
#db = con.test_database
#people = db.people

#people.insert({"name":"Lexa"})
#people.insert({"name":"Ryan"})
@app.route('/')
def hello_world()
    #return 'Hello Docker'
	return render_template('index.html')

app.route('/adds', methods=['POST'])
def add_args():
	if not request.json:
		abort(400)
	try:
		name = request.json['name']
		arg1 = request.args.get('argument1',0,type=int)
		arg2 = request.args.get('argument2',0,type=int)
		#arg1 = request.json['argument1']
		#arg2 = request.json['argument2']
		answer = arg1 + arg2
		return jsonify(answer)
		con = Connection("172.17.0.2:27017")
		#return (jsonify({'name':name}), 200)
		
		db = con.test_database
		people = db.people

		people.insert({'name':name})
	except KeyError:
		abort(400)

@app.route('/add', methods=['POST'])
def add_args():
	if not request.json:
		abort(400)
	try:
		arg1 = request.json['argument1']
		arg2 = request.json['argument2']
		answer = arg1 + arg2
		return (jsonify({'answer':answer}), 200)
	except KeyError:
		abort(400)

if __name__ == '__main__':
    app.run(debug='true')
