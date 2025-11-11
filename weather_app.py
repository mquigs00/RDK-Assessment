import requests
import os
from dotenv import load_dotenv
load_dotenv()

class WeatherApp:
    def __init__(self):
        self.favorite_cities = []

    def add_favorite_city(self, city):
        '''
        Allows the user to keep up to three favorite cities
        :param city:
        :return:
        '''
        if len(self.favorite_cities) < 3:
            self.favorite_cities.append(city)
        else:
            print("Sorry, you can only have up to 3 favorite cities!")

    def view_favorite_cities(self,):
        print("Favorite cities:")
        for city in self.favorite_cities:
            print(city)

    def get_city_coordinates(self, city_name):
        '''
        Gets the latitiude and longitude of a city
        :param city_name:
        :return: lat, long
        '''
        res = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&&appid={os.getenv("API_KEY")}')
        lat = res.json()[0]["lat"]
        long = res.json()[0]["lon"]
        return lat, long

    def get_city_data(self, city_name):
        '''
        Gets the total weather data for a city across many dates
        :param city_name:
        :return: json of weather data
        '''
        city_id = self.get_city_id(city_name)
        res = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?id={city_id}&units=imperial&appid={os.getenv("API_KEY")}")
        return res.json()

    def get_city_id(self, city_name):
        '''
        Gets the OpenWeatherMap id of a city
        :param city_name:
        :return: id
        '''
        res = requests.get(f"http://api.openweathermap.org/data/2.5/find?q={city_name}&appid={os.getenv("API_KEY")}")
        id = res.json()["list"][0]["id"]
        return id

    def get_temperature(self, city_name):
        '''
        Gets the temperature of a city in Fahrenheit
        :param city_name:
        :return: temp
        '''
        data = self.get_city_data(city_name)
        temp = data["list"][1]["main"]["temp"]
        print(f"It is {temp} degrees Fahrenheit in {city_name}")
        return temp

    def get_weather_description(self, city_name):
        '''
        Gets the weather description of a city
        :param city_name:
        :return: description
        '''
        data = self.get_city_data(city_name)
        description = data["list"][1]["weather"][0]["description"]
        print(f"Weather in {city_name}: {description}")
        return description

    def get_wind_speed(self, city_name):
        '''
        Gets the wind speed in a city
        :param city_name:
        :return: wind_speed
        '''
        data = self.get_city_data(city_name)
        wind_speed = data["list"][1]["wind"]["speed"]
        print(f"Wind speed in {city_name}: {wind_speed} mph")
        return wind_speed