import requests

API_URL ='https://restcountries.com/v3.1/all'

HEADERS = {
    'Content-Type': 'application/json'
}

PARAMS = {
    "fields": "name,region",
    "param 2": "value2"
}

def get_data():

    try:
        response = requests.get(API_URL, headers=HEADERS, params=PARAMS)

        if response.status_code == 200:
            print(f"Fout bij ophalen van data: {response.status_code}")




