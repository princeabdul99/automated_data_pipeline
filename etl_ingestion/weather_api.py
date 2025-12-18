import requests


api_url = ''

def fetch_data():
    response = requests.get(api_url)
    print(response)