import requests
import json


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat" : 51.107883,
    "lon" : 17.038538,
    "appid" : "4eaf4346eb269bfee1ee3f1c726cac57",
    "exclude" : "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
print(response)

data_weather = response.json()
print(data_weather['hourly'][0]["weather"][0])

for i in range(0,12):
    for weather in data_weather['hourly'][i]["weather"]:
        if weather["id"] < 700:
            print("Bring an Umbrella")
            break

