import requests

APP_ID = "a7144d21"
API_KEY = "0c15ecd78c2e406d5685a22dbbaf98c3"

GENDER = "male"
WEIGHT_KG = 74
HEIGHT_CM = 170
AGE = 21

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    'query':exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)