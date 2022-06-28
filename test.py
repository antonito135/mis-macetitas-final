import requests

response = requests.get('https://swapi.dev/api/people/').json()

print(response)