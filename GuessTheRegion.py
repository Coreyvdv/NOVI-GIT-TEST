import requests

URL = 'https://restcountries.com/v3.1/name/'

PARAMS = {
    "param 1": "value1",
    "param 2": "value2"
}

response = requests.get(URL)

pictures = response.json()

print(pictures[0])

# ***********************************************

URL = 'https://blablabla.com/pictures'
DATA = {'title': 'Een nieuwe foto', 'body': 'dit is de nieuwe foto'}
HEADERS = {'Content-Type': 'application/json'}
PARAMS = {'key': 'value'}

response = requests.post(URL, json=DATA, headers=HEADERS, params=PARAMS)

# *************************************************
def main():
    print("start application")


if __name__ == "__main__":
    main()



