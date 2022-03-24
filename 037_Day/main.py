import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "wrafalit"
TOKEN = "sdfw42wrtjfsndiufy34rhewfu34"

GRAPHID = "graph1"

user_params = {
    "token" : TOKEN,
    "username" :USERNAME ,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# respons = requests.post(url=pixela_endpoint, json=user_params)
# print(respons.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPHID,
    "name" : "Coding graph",
    "unit" : " hours",
    "type": "float",
    "color" : "kuro"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime(year=2022, month=3, day=20)
date = today.strftime("%Y%m%d")
print(date)
pixel_config = {
    "date" : date,
    "quantity" : "6.0",
}

# respons = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(respons.text)

#update
update_graph = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date}"

update_config = {
    "quantity" : "0.4"
}

respons = requests.delete(url=update_graph, json=update_config, headers=headers)
print(respons.text)