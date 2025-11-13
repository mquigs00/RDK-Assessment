import weather_app
from weather_app import WeatherApp
from Sort import sort, sortAndFindMedian

if __name__ == "__main__":
    weather = weather_app.WeatherApp()
    weather.add_favorite_city("Philadelphia")
    weather.add_favorite_city("Chicago")
    weather.add_favorite_city("New York")
    weather.view_favorite_cities()

    numbers = [1, 5, 2, 5, 7]
    result = sortAndFindMedian(numbers)
    print(result)