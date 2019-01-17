Iimport requests
from pprint import pprint

city = input('Enter your City : ')

# Here You have to type suitable api key, that cen be generated on apiweather web page
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=<ENTER_OWN_API_KEY>'.format(city)

res = requests.get(url)
data = res.json()

currentTemp = data['main']['temp']
windSpeed = data['wind']['speed']

latitude = data['coord']['lat']
longitude = data['coord']['lon']

print('Temperature : {} degree celcius'.format(currentTemp))
print('Wind speed : {} m/s'.format(windSpeed))
print('Latitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))
