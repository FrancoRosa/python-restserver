from flask import request
from flask import abort
from flask import Flask, jsonify
from flask import make_response
from flask_cors import CORS, cross_origin
from filemanagement import read_file
from algorithms import orderMethod
from time import time, sleep
import json


unordered = []
ordered = []   

app = Flask(__name__)
CORS(app)

about = {
        'author': u'Gared',
        'methods': u'Insert, Bubble, Ramdom'
        }

@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'about': about})

@app.route('/', methods=['POST'])
def create_task():
    global orderMethod, unordered
    jsonpost = json.loads(request.data)

    if 'file' in jsonpost:
        start = time()
        unordered = read_file(jsonpost['file'])
        end = time()
        elapsed = end - start
        message = 'Archivo con !<%d muestras!> cargadas con exito'%(len(unordered))
        message = message.replace('!<','<span class="has-text-info">')
        message = message.replace('!>','</span class="has-text-info">')
        return jsonify({'message': message, 'time':elapsed, 'samples': unordered})
    if 'method' in jsonpost:
        method = jsonpost['method']
        samples = jsonpost['samples']
        start = time()
        ordered = orderMethod(method, unordered, samples)
        end = time()
        elapsed = end - start
        message = '!<%s muestras!> ordenadas en !<%2.3f sec!>, con el metodo !<%s!>.'%(samples, elapsed, method)
        message = message.replace('!<','<span class="has-text-info">')
        message = message.replace('!>','</span class="has-text-info">')
        print(message)
        return jsonify({'message': message, 'time': elapsed, 'samples': ordered}) 
    
    return jsonify({'error': 'Not found'}) 
if __name__ == '__main__':
    app.run(debug=True)

