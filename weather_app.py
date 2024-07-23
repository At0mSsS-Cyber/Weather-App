import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_weather(city_name):
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")  # Get the API key from environment variables
    if not api_key:
        raise ValueError("API key not found. Please set the OPENWEATHERMAP_API_KEY environment variable.")
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        
        if data['cod'] != 200:
            print(f"Error: {data['message']}")
            return
        
        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        weather_description = weather['description']
        
        print(f"Temperature: {temperature}°C")
        print(f"Atmospheric pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {weather_description.capitalize()}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
