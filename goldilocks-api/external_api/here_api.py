import requests

_URLS = {'WEATHER': 'https://weather.api.here.com/weather/1.0/report.json',
         'ROUTE': 'https://route.api.here.com/routing/7.2/calculateroute.json',
         }

_KEYS = {'app_id': 'rJ7X74cBamfcaE5q6riO',
         'app_code': 'M1ccHgAFGm24WmU32PRh1Q', }

# defining a params dict for the parameters to be sent to the API
PARAMS = {**_KEYS,
          'waypoint0': 'geo!52.5,13.4',
          'waypoint1': 'geo!52.5,13.45',
          'mode': 'fastest;car;traffic:disabled'}


def request_weather_for_location(location: str):
    params = {**_KEYS,
              'product': 'observation',
              'name': location.capitalize()}

    response = requests.get(url=_URLS.get('WEATHER'), params=params)
    return response.json()
