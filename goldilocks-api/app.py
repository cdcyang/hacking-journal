from flask import Flask, request
import json

from data.adapters import DataController

app = Flask(__name__)
controller = DataController()


@app.route('/')
def hello_world():
    return 'The Goldilocks Experience'


@app.route('/flight', methods=['GET'])
def get_flights():
    flight_code = request.args.get('code', '').upper()
    result = controller.get_flight(flight_code)
    return return_response(result, f'Unable to find flight information for [flight={flight_code}]')


@app.route('/airport', methods=['GET'])
def get_airport():
    airport_code = request.args.get('code', '').upper()
    result = controller.get_airport(airport_code)
    return return_response(result, f'Unable to find airport information for [airport={airport_code}]')


@app.route('/route', methods=['GET'])
def get_route():
    start_lat = 51.5218
    start_lon = -0.0844
    flight_code = request.args.get('code', '').upper()
    result = controller.get_route_information(start_lat, start_lon, flight_code)
    return app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json')


@app.route('/weather')
def get_weather():
    location = request.args.get('location', '')
    weather = controller.get_weather(location)
    return return_response(weather, f'Unable to find weather information for [location={location}]')


def return_response(data, error_message):
    if data:
        return app.response_class(
            response=json.dumps(data.__dict__),
            status=200,
            mimetype='application/json')
    else:
        return app.response_class(
            response=error_message,
            status=400)


if __name__ == '__main__':
    app.run()
