import time
from flask import Flask, render_template,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


a = 100
b = 10
c = ['a','b','c','d'] #list
d = {
    'key':'a',
    'key1':'b',
    'key2':'c',
    'key3':'d',
}

@app.route('/', methods=['GET'])
def defaults():
    return render_template('dummy.html')

@app.route('/a', methods=['GET'])
def ca():
    if 10 == 110:
        return "yes 10 is equal to 10"
    
    a = {
        'msg':'this is get'
    }
    return jsonify(a),202

@app.route('/a', methods=['POST'])
def da():
    return "this is post"

if __name__ == '__main__':
    print(0)
    app.run(host='0.0.0.0',port=3002,debug=True)
