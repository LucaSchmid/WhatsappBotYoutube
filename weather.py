import requests

myKey = process.env.API_KEY
url = 'http://api.openweathermap.org/data/2.5/weather?q=Ulm&appid='+myKey

json_data = requests.get(url).json()
print(url)