import requests
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("WEATHERSTACK_API_KEY")
api_url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query=Cebu City"

def fetch_data():
    print("Fetching weather data from weatherstack API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        
        data = response.json()
        # Weatherstack-specific validation
        if "error" in data:
            raise ValueError(f"Weather API error: {data['error']}")

        if "current" not in data or "location" not in data:
            raise KeyError(f"Unexpected API response structure: {data}")

        print("API response received successfully!")
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        raise    

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 
'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-12-18 08:00', 'localtime_epoch': 1766044800, 'utc_offset': '-5.0'}, 'current': {'observation_time': '01:00 PM', 'temperature': 0, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear '], 'astro': {'sunrise': '07:15 AM', 'sunset': '04:30 PM', 'moonrise': '06:17 AM', 'moonset': '03:05 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': 4}, 'air_quality': {'co': '792.85', 'no2': '53.25', 'o3': '26', 'so2': '14.45', 'pm2_5': '30.75', 'pm10': '32.15', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 4, 'wind_degree': 39, 'wind_dir': 'NE', 'pressure': 1026, 'precip': 0, 'humidity': 75, 
'cloudcover': 25, 'feelslike': -1, 'uv_index': 0, 'visibility': 16, 'is_day': 'yes'}}