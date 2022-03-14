import requests
import  datetime as  dt

MY_LAT = 51.107883 #My position
MY_LON = 17.038538

respons = requests.get(url="http://api.open-notify.org/iss-now.json")
respons.raise_for_status()

data = respons.json()
# print(data)

#iss position
longitude = float(data["iss_position"]['longitude'])
latitude = float(data["iss_position"]['latitude'])
# print(longitude)
# print(latitude)

iss_possision = (longitude , latitude)
print(iss_possision)

# +5 and -5 degree of the iss position

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(response)
# print(data)

time_now = dt.datetime.now()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise)
print(sunset)
print(time_now.hour)
