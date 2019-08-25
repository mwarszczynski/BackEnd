import json


class CarDB:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)

    def get_data(self, model):
        for car in self.__data['cars']:
            if car['model'] == model:
                return car

    def close(self):
        print('Connection to database end properly')

