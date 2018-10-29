from app import app
from flask import jsonify

@app.route('/', methods=['GET'])
def helloworld():
    print "Hi"
    return jsonify({'message':"Hello World"})

@app.route('/test', methods=['GET'])
def test():
    print "Test"
    return "Test"