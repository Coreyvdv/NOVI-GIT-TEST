import requests

URL ='<URI>'

def get_countries():

    try:
        response = requests.get(URL, params=params)

        if response.status_code != 200:
            print(f"FOUT, statuscode van data: {response.status_code}")

        countries = response.json()




