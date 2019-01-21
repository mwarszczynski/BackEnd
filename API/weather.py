import requests
from pprint import pprint

city = input('Enter your City : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=7ea290f5bb54f4d7562ae933a868a038'.format(city)

res = requests.get(url)
data = res.json()

currentTemp = data['main']['temp']
pressure = data['main']['pressure']
windSpeed = data['wind']['speed']

latitude = data['coord']['lat']
longitude = data['coord']['lon']

print('Temperature :', currentTemp)
print('Wind speed : {} m/s'.format(windSpeed))
print('Pressure : {} hPa'.format(pressure))
print('Latitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))
