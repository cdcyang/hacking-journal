import urllib

from amadeus import Client, ResponseError
from datetime import date, timedelta

from data.adapters import Flight

amadeus = Client(
    client_id='HYoY3FbJAuqjjx6y2dTaHkVfZ32fhmgm',
    client_secret='5egyBj6ykDqD1TmU',
    log_level='debug'
)


def request_flight_delay(flight: Flight):
    response = amadeus.get('/v1/travel/predictions/flight-delay',
                           originLocationCode=flight.departure.get('iataCode'),
                           destinationLocationCode=flight.arrival.get('iataCode'),
                           departureDate=flight.departure.get('at').split('T')[0],
                           departureTime=flight.departure.get('at').split('T')[1],
                           arrivalDate=flight.arrival.get('at').split('T')[0],
                           arrivalTime=flight.arrival.get('at').split('T')[1],
                           aircraftCode=flight.aircraft,
                           carrierCode=flight.carrier_code,
                           flightNumber=flight.carrier_number,
                           duration=flight.duration)
    return response.data


def request_flights(source: str, destination: str, departure_date: date = date.today() + timedelta(days=1)):
    response = amadeus.get('/v2/shopping/flight-offers',
                           originLocationCode=source,
                           destinationLocationCode=destination,
                           departureDate=departure_date,
                           adults='1',
                           nonStop='true')
    return response.data
