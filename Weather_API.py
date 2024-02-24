#importing the required library.
import requests

#Class and Methods Definition.
class City:

    def __init__(self, name, lat, lon, units="metric"):
        '''
        This method assigns the instance variables and calls the two dependent methods.
        '''
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()
        self.print_data()

    def get_data(self):
        '''
        Helper Function (1):
        This method tries to get the data in a json file format from www.openweathermap.org.
        '''
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid={weather_api_id}")
        except:
            print("Please connect to internet to get the weather data.")

        #read the json file data in a variable.
        response_json = response.json()

        #using the json file, get the data we need for weather report.
        self.today_temp = response_json["main"]["temp"]
        self.today_temp_min = response_json["main"]["temp_min"]
        self.today_temp_max = response_json["main"]["temp_max"]

    def print_data(self):
        '''
        Helper function (2):
        This method prints all the data we seek for a city on today.
        '''
        print(f"In {self.name}, the temperature today is {round(self.today_temp,0)}°C")
        print(f"In {self.name}, today's lowest temperature is {round(self.today_temp_min,0)}°C")
        print(f"In {self.name}, today's highest temperature is {round(self.today_temp_max,0)}°C")

#Instance of the class City.
city_name = input("Please enter the name of the city you want to check the weather for.\n")
city_lat = float(input("Please enter the latitude of the city you want to check the weather for.\n"))
city_lon = float(input("Please enter the longitude of the city you want to check the weather for.\n"))
weather_api_id = input("Please enter your weather API ID.\n")

city = City(city_name, city_lat, city_lon)