from flask import request
from flask import abort
from flask import Flask, jsonify

app = Flask(__name__)

about = {
        'author': u'Gared',
        'methods': u'Insert, Bubble, Ramdom'
        }

@app.route('/solver', methods=['GET'])
def get_tasks():
    return jsonify({'about': about})

@app.route('/solver', methods=['POST'])
def create_task():
    if 'file' in request.json:
        print(request.json['file'])
        return jsonify({'file': True}), 201
    if 'method' in request.json:
        print(request.json['method'])
        print(request.json['samples'])
        return jsonify({'solve': True}), 201
    return abort(404)
if __name__ == '__main__':
    app.run(debug=True)

