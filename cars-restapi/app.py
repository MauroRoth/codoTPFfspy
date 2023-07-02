from flask import Flask, jsonify, request, render_template
from .resources.cars import Cars

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    pong = jsonify({'message': 'pong!'})
    return render_template('index.html', mensaje=pong.json)

@app.route('/cars', methods=['GET'])
def getCars():
    return jsonify({'cars': Cars, 'message': "Cars List"})
    #return render_template('carsList.html', carsList = carsList.json)

@app.route('/cars/<string:car_name>', methods=['GET'])
def getCar(car_name):
    carsFound = [car for car in Cars if car['car_name'] ==  car_name] 
    return jsonify(carsFound)

@app.route('/cars', methods=['PUT'])
def addCar():
    print(request.json)
    return 'recibido'

if __name__ == '__main__':
    app.run(debug=True)