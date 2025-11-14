import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if not API_KEY:
        print("API key not found! Please set it in your .env file.")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"\nWeather for {data['name']}, {data['sys']['country']}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Condition: {data['weather'][0]['description'].title()}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        elif response.status_code == 401:
            print("\nInvalid API key. Please check your .env file.")
        elif response.status_code == 404:
            print("\nCity not found. Please check the city name and try again.")
        else:
            print(f"\nError {response.status_code}: {data.get('message', 'Unknown error')}")

    except requests.exceptions.RequestException as e:
        print(f"\nNetwork error: {e}")

def main():
    print("Welcome to Weather Dashboard CLI!")
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye!")
            break
        if not city:
            print("Please enter a valid city name.")
            continue
        get_weather(city)

if __name__ == "__main__":
    main()
