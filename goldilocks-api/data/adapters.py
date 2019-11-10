import csv

import json

from data.models import Flight, Airport, Weather
from external_api.amadeus_api import request_flight_delay
from external_api.here_api import request_weather_for_location

_flights = dict()
_airports = dict()


def _source_flights_from_amadeus():
    # data = get_flights('LON', 'MIA')
    f = open('resources/flights.json')
    data = json.load(f)
    flights = [_adapt_to_domain_flight(d.get('itineraries')[0]) for d in data]
    return {(f.carrier_code + f.carrier_number): f for f in flights}


def _adapt_to_domain_flight(data: dict):
    meta_data = data.get('segments')[0]
    return Flight(duration=data.get('duration'),
                  carrier_code=meta_data.get('carrierCode'),
                  carrier_number=meta_data.get('number'),
                  aircraft=meta_data.get('aircraft').get('code'),
                  departure=meta_data.get('departure'),
                  arrival=meta_data.get('arrival'))


def _source_airports_from_csv():
    airports = dict()
    with open('resources/airports.csv', encoding="utf8") as data_file:
        reader = csv.reader(data_file)
        next(reader)

        for r in reader:
            airports[r[0]] = Airport(r[0], r[1], r[2], r[3], r[4], float(r[5]), float(r[6]))
        return airports


def _adapt_to_domain_weather(response: dict):
    weather_data = response.get('observations').get('location')[0].get('observation')[0]
    return Weather(temperature=float(weather_data.get('temperature')),
                   description=weather_data.get('description'))


class DataController:

    def __init__(self):
        self._flights = _source_flights_from_amadeus()
        self._airports = _source_airports_from_csv()

    def get_flight(self, flight_code: str):
        return self._flights.get(flight_code)

    def get_weather(self, location: str):
        response = request_weather_for_location(location)
        return _adapt_to_domain_weather(response) if response else None

    def get_route_information(self, flight_code: str):
        flight = self._flights.get(flight_code)
        if not flight:
            return None

        delay = request_flight_delay(flight)

        airport = _airports.get(flight.departure.get('iataCode'))
        return None
