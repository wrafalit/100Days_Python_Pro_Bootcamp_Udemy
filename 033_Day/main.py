import requests
import datetime as dt
import  smtplib
import  time

MY_LAT = 51.107883 #My position
MY_LON = 17.038538

# ------------------- Email ----------------------
def send_email():
    my_email = "wraxxxxxxmail.com"
    password = "Pyxxxxx12#"
    to_addres_email = "pyxxxxp.pl"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_addres_email,
            msg="Subject:ISS up to sky\n\n"
                "See up to sky ISS is above you!"
        )

def is_iss_overhead():
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
    print("iss possision",iss_possision)

    # +5 and -5 degree of the iss position
    if (longitude - MY_LON < 5 or longitude- MY_LON < -5) :
        if (latitude - MY_LAT < 5 or latitude- MY_LAT < -5) :
            return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LON,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
        # its dark

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        send_email()



