import requests

api_url = 'http://api.openweathermap.org/data/2.5/weather'

city = input('Enter your city: ')

params = {
    'q': city,
    'appid': '73f3f5de8f0e2ef1e53c1407dd55b99a',
    'units': 'metric'
}

res = requests.get(api_url, params=params)

data = res.json()
template = 'Current temperature in {} is {} °C'

city = city[0].upper() + city[1:].lower()
print(template.format(city, data['main']['temp']))