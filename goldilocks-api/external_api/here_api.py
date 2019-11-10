import requests

_URLS = {'WEATHER': 'https://weather.api.here.com/weather/1.0/report.json',
         'ROUTE': 'https://route.api.here.com/routing/7.2/calculateroute.json',
         }

_KEYS = {'app_id': 'rJ7X74cBamfcaE5q6riO',
         'app_code': 'M1ccHgAFGm24WmU32PRh1Q', }


def request_route_for_car(start: str, destination: str):
    params = {**_KEYS,
              'product': 'observation',
              'waypoint0': f'geo!{start}',
              'waypoint1': f'geo!{destination}',
              'mode': 'fastest;car;traffic:disabled', }

    response = requests.get(url=_URLS.get('ROUTE'), params=params)
    return response.json()


def request_route_for_public(start: str, destination: str):
    params = {**_KEYS,
              'product': 'observation',
              'waypoint0': f'geo!{start}',
              'waypoint1': f'geo!{destination}',
              'departure': 'now',
              'mode': 'fastest;publicTransport',
              'combineChange': 'true'}
    response = requests.get(url=_URLS.get('ROUTE'), params=params)
    return response.json()


def request_route_for_bike(start: str, destination: str):
    params = {**_KEYS,
              'product': 'observation',
              'waypoint0': f'geo!{start}',
              'waypoint1': f'geo!{destination}',
              'mode': 'fastest;bicycle', }
    response = requests.get(url=_URLS.get('ROUTE'), params=params)
    return response.json()


def request_weather_for_location(location: str):
    params = {**_KEYS,
              'product': 'observation',
              'name': location.capitalize()}

    response = requests.get(url=_URLS.get('WEATHER'), params=params)
    return response.json()
