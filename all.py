import requests, json

url = 'http://pokeapi.co/api/v2/pokemon/'

response = requests.get(url)

if response.status_code==200:
    data =  json.loads(response.text)
    print(data)
else:
    print('error')

