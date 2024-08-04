from flask import Flask, render_template,jsonify
from flask_cors import CORS
from flask import Flask, request, jsonify
import uuid
import json
from db.connection import get_Client
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('dummy.html')


@app.route('/AdminLogin', methods=['POST'])
def AdminLogin():
    json_data = request.form.get('Data')
    if json_data:
        form_data = json.loads(json_data)
        name = form_data.get('userName')
        password = form_data.get('password')
        if (name != 'Admin'):
            res = {
                'ErrorCode':5001,
                'ErrorMSG':"Wrong username"
            }
            return jsonify(res), 200
        if (password != 'Admin'):
            res = {
                'ErrorCode':5002,
                'ErrorMSG':"Wrong password"
            }
            return jsonify(res), 200
        if (name != 'Admin' and password != 'Admin'):
            res = {
                'ErrorCode':5001,
                'ErrorMSG':"Wrong password"
            }
            return jsonify(res), 200
        if(name == 'Admin' and password == 'Admin'):
            sessionId = uuid.uuid4()
            client = get_Client()
            collection = client.get_collection('AdminSession')
            collection.delete_one({'userName':'admin'})
            collection.insert_one({'userName':'admin','sessionId':str(sessionId)})
            response = {
                'ErrorCode':2002,
                'ErrorMSG':"Login success",
                'sessionId': sessionId
            }
            return jsonify(response), 200
    response = {
                'ErrorCode':5001,
                'ErrorMSG':"Wrong password"
            }
    return jsonify(response), 200



@app.route('/getCars',methods=['POST'])
def getCars():
    json_data = request.form.get('Data')
    if json_data:
        form_data = json.loads(json_data)
        carType = form_data.get('Type')
        if carType:
            client = get_Client()
            collection = client.get_collection('OwnedCars')
            data = collection.find({'type':str(carType)},{'_id' : 0})
            carList = []
            for i in data:
                carList.append(i)
            response = {
                'ErrorCode':2001,
                'CarList': carList
            }
            return jsonify(response),200
        response = {
            'ErrorCode':5001,
            'ErrorMessage': "Formdata missing"
        }
        return jsonify(response),200
    response = {
        'ErrorCode':5002,
        'ErrorMessage': "Something went wrong in server code"
    }
    return jsonify(response),200


@app.route('/AddCars',methods=['POST'])
def AddCars():
    json_data = request.form.get('Data')
    if json_data:
        form_data = json.loads(json_data)
        carType = form_data.get('type')
        carmodel = form_data.get('model')
        carcolor = form_data.get('color')
        carnumber = form_data.get('number')
        carrentCostPerKilometer = form_data.get('rentCostPerKilometer')
        if carType != None and  carmodel != None and carcolor != None and carnumber != None and carrentCostPerKilometer != None:
            client = get_Client()
            collection = client.get_collection('OwnedCars')
            collection.insert_one({
                'type':carType,
                'color':carcolor,
                'model':carmodel,
                'number':carnumber,
                'price':carrentCostPerKilometer
            })
            response = {
                'ErrorCode':2001,
            }
            return jsonify(response),200
        response = {
            'ErrorCode':5001,
            'ErrorMessage': "Formdata missing"
        }
        return jsonify(response),200
    response = {
        'ErrorCode':5002,
        'ErrorMessage': "Something went wrong in server code"
    }
    return jsonify(response),200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5656, debug=True)
