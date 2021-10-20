import requests
import os
from dotenv import load_dotenv
from datetime import date

#CREATE USER

load_dotenv('100 days of code//.gitignore')

PIXELA_TOKEN = os.getenv('pixela_token')
USERNAME = "justas"
GRAPH = 'graph1'

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token':PIXELA_TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
response = requests.post(url = pixela_endpoint, json = user_params)

# # CREATE GRAPH DEFINITION

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_params = {
#     'id': 'graph1',
#     'name': 'Cycling graph',
#     'unit': 'Km',
#     'type': 'float',
#     'color': 'shibafu',
# }

# headers = {
#     'X-USER-TOKEN': PIXELA_TOKEN
# }
# response = requests.post(url=graph_endpoint, json = graph_params, headers = headers)



#Pixel in graph


pixel_endpoint = f"{graph_endpoint}/{GRAPH}"
today = str(date.today()).replace("-", "")

pixel_params = {
    'date' : today,
    'quantity' : '20',
}

headers = {
    'X-USER-TOKEN': PIXELA_TOKEN
}

# response = requests.post(url = pixel_endpoint, json = pixel_params, headers = headers)

pixel_update_endpoint = f"{pixel_endpoint}/{today}"

pixel_update_params = {
    'quantity': input("How many kilometers did you bike today?")
}

response = requests.put(url = pixel_update_endpoint, json = pixel_update_params, headers = headers)
print(response)