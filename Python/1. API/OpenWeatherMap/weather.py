import os

import requests

# Function search the City that You enter, and return info from openweather API about current weather
def find_over_city():
    yourCity = input('Pass Your City : ')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=7ea290f5bb54f4d7562ae933a868a038'.format(yourCity)
    res = requests.get(url)
    data = res.json()
    show_info(data)

# Function search over ZIP code & country code
#def findOverZipAndCountryCode():
#    countryCode = input('Type Your country code here: ')
#    countryZipCode = input('Enter Your country ZIP code: ')
# --------------------- > to be continued < ---------------------

# Function uses 'ipinfo' webpage to check the geolocation, and return info from openweather API about current weather
def find_over_current_location():
    url_location = ('https://ipinfo.io/')
    res = requests.get(url_location)
    data = res.json()
    place = data['loc'].split(',')
    latitude = place[0]
    longitude = place[1]

    url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=7ea290f5bb54f4d7562ae933a868a038&units=metric'.format(latitude, longitude)
    res = requests.get(url)
    data = res.json()
    show_info(data)

# This is summary function, which is concludes all information downloaded from openweather API
def show_info(data):
    currentTemperature = data['main']['temp']
    windSpeed = data['wind']['speed']
    currentPressure = data['main']['pressure']

    print('Current temperature : ', currentTemperature)
    print('Wind speed: ', windSpeed, 'm/s')
    print('Current pressure: ', currentPressure)

    print(weather_file(data))

# Function saving the result of the weather in mentioned file.
def weather_file(data):
    weatherLog = os.getcwd()

    try:
        f = open('weatherLog.txt','w')
        try:
            f.write(str(data))
        finally:
            f.close()
    except IOError:
        print('oops')
# ----------------> Change - cut necessary data and paste into mentioned file. <------------------

def main():
    print('1. Get data by city')
    print('2. Get data by location')

    choice = input('Type Your choice : ')

    if choice == '1':
        find_over_city()
    elif choice == '2':
        find_over_current_location()
    else:
        print('Invalid...')

if __name__ == '__main__':
    main()

