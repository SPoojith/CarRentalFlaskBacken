from flask import Flask, jsonify, request
from flask_cors import CORS

BasicCar = [
    {
        'carId' :1,
        'carNumber' :1111,
        'carModel':'Santro',
        'carColor':'Red'
    },
    {
        'carId' :2,
        'carNumber' :1112,
        'carModel':'omni',
        'carColor':'grey'
    },
    {
        'carId' :3,
        'carNumber' :1113,
        'carModel':'Swift',
        'carColor':'white'
    }
]
sportsCar = [
    {
        'carId' :11,
        'carNumber' :2221,
        'carModel':'GTR',
        'carColor':'Red'
    },
    {
        'carId' :12,
        'carNumber' :2222,
        'carModel':'BMW',
        'carColor':'grey'
    },
    {
        'carId' :13,
        'carNumber' :2223,
        'carModel':'lamborgini',
        'carColor':'white'
    }
]
luxuryCar = [
    {
        'carId' :21,
        'carNumber' :3331,
        'carModel':'audi',
        'carColor':'Red'
    },
    {
        'carId' :22,
        'carNumber' :3332,
        'carModel':'benz',
        'carColor':'grey'
    },
    {
        'carId' :23,
        'carNumber' :3333,
        'carModel':'ferari',
        'carColor':'white'
    }
]
periumCar = [
    {
        'carId' :31,
        'carNumber' :4441,
        'carModel':'bently',
        'carColor':'Red'
    },
    {
        'carId' :32,
        'carNumber' :4442,
        'carModel':'rollsroys',
        'carColor':'grey'
    },
    {
        'carId' :33,
        'carNumber' :4443,
        'carModel':'bugati',
        'carColor':'white'
    }
]

carType = {
    'Basic':BasicCar,
    'Sports':sportsCar,
    'Luxury':luxuryCar,
    'Premium':periumCar
}

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Route to fetch all data
@app.route('/', methods=['GET'])
def get_data():
    data = {
        'msg':'hi'
    }
    return jsonify(data), 200


def getCars(type):
    print(type)
    return (carType[type])


@app.route('/GetCarList', methods=['GET'])
def get_car_data():
    # Retrieve parameters from the request query string
    car_type = request.args.get('car_type')
    # You can retrieve more parameters similarly

    # Example: Simulate fetching data based on the parameters
    if car_type:
        # Assume fetching data based on car_type
        car_list = getCars(car_type)
        return jsonify(car_list), 200
    else:
        # Handle case where parameter is missing
        return jsonify(error="Missing car_type parameter"), 400
    

# Route to add new data
@app.route('/add', methods=['GET'])
def add_data():
    car_type = request.args.get('car_type')
    new_data = {
        'carId' :'new',
        'carNumber' :0000,
        'carModel':'new bugati',
        'carColor':'new'
    }
    carType[car_type].append(new_data)
    return jsonify(carType[car_type]), 200
# Route to add new data
@app.route('/addCar', methods=['POST'])
def addCar():
    car_type = request.form.get('carType')
    car_id = request.form.get('carId')
    car_number = request.form.get('carNumber')
    car_model = request.form.get('carModel')
    car_color = request.form.get('carColor')

    # Example data handling (you may store in a database or process as needed)
    new_data = {
        'carId': car_id,
        'carNumber': car_number,
        'carModel': car_model,
        'carColor': car_color
    }
    carType[car_type].append(new_data)
    return jsonify(carType[car_type]), 200

# Example route with CORS enabled
@app.route('/api/data', methods=['GET'])
def get_api_data():
    data = {'message': 'Hello, CORS!'}
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
