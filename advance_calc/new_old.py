import datetime as dt
import requests
BASE_URl = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api','r').read()
city = "udaipur"
url = BASE_URl+"appid="+API_KEY+"&q="+city
response = requests.get(url).json()
print(response)