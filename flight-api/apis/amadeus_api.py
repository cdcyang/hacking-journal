from amadeus import Client, ResponseError

amadeus = Client(
    client_id='HYoY3FbJAuqjjx6y2dTaHkVfZ32fhmgm',
    client_secret='5egyBj6ykDqD1TmU'
)

def get_flight_delay_info():
    try:
        response = amadeus.get('/v1/airport/predictions/on-time', airportCode='JFK', departureDate='2020-01-01')
        print(response.data)
    except ResponseError as error:
        print(error)

def main():
    try:
        response = amadeus.reference_data.urls.checkin_links.get(airlineCode='BA')
        print(response.data)
    except ResponseError as error:
        print(error)


if __name__ == '__main__':
    main()


