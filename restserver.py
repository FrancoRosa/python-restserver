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
        unordered = read_file(jsonpost['file'])
        sampleStr = ', '.join(str(x) for x in unordered[:10])
        message = 'File with !<%d samples!> was succesfully loaded, !<sample: %s!>'%sampleStr
        message = message.replace('!<','<span class="has-text-info">')
        message = message.replace('!>','</span class="has-text-info">')
        return jsonify({'message': message})
    if 'method' in jsonpost:
        method = jsonpost['method']
        samples = jsonpost['samples']
        start = time()
        ordered = orderMethod(method, unordered, samples)
        sleep(1)
        end = time()
        elapsed = end - start
        sampleStr = ', '.join(str(x) for x in ordered[:10])
        message = '!<%s samples!> ordered in !<%2.3f sec!>, using !<%s!> method. !<%s!>'%(samples, elapsed, method, sampleStr)
        message = message.replace('!<','<span class="has-text-info">')
        message = message.replace('!>','</span class="has-text-info">')
        print(message)
        return jsonify({'message': message}) 
    
    return jsonify({'error': 'Not found'}) 
if __name__ == '__main__':
    app.run(debug=True)

