import requests
from datetime import datetime

# nutritionix
APP_ID = ""
API_KEY = ""
exercise_end_url = ""

# sheety
TOKEN = ""
head = {"Authorization" : "Bearer " + TOKEN}
end_url = ""

def post_exercise(active):

    user_param = {
         "query": active,
         "gender":"male",
         "weight_kg":84,
         "height_cm":180,
         "age":35
        }

    headers = {
        "x-app-id" : APP_ID,
        "x-app-key" : API_KEY,
        "Content-Type" : "application/json",
    }

    response = requests.post(url=exercise_end_url, json=user_param, headers=headers)
    exercise = []
    action = response.json()["exercises"][0]['user_input']
    duration = response.json()["exercises"][0]['duration_min']
    calories = response.json()["exercises"][0]['nf_calories']
    print(f"Your action: {action}, duration: {duration} and burn {calories} calories.")
    exercise.append(action)
    exercise.append(duration)
    exercise.append(calories)
    return exercise

def sheety(exercise:list):

    data = {
        "workout" : {
                "date": datetime.now().strftime("%d/%m/%Y"),
                "time": datetime.now().strftime("%H:%M:%S"),
                "exercise": exercise[0],
                "duration": exercise[1],
                "calories": exercise[2]
            }
        }

    sheety_post = requests.post(url=end_url, json=data, headers=head)



# active = input("Tell me which exercise you did? ")
active =  "runing 30 min"
exercise = post_exercise(active)
sheety(exercise)