import requests
import datetime as dt
import os

# I KNOW I SHOULD NOT DO THAT
# os.environ['APP_ID'] = "674b8750"
# os.environ['API_KEY'] = "e3fffb3470508be8a50925c4a4dba0a5"
# os.environ['SHEETY_Authorization'] = "Basic U2FlZWQ6MTIzNDMyNGUz"
# os.environ['EXERCISE_END_POINT'] = "https://trackapi.nutritionix.com/v2/natural/exercise"
# os.environ['SHEET_END_POINT'] = "https://api.sheety.co/dcb9fe8d3777fe4163a80cbba2455531/myWorkouts/workouts"

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_Authorization = os.environ.get("SHEETY_Authorization")
EXERCISE_END_POINT = os.environ.get("EXERCISE_END_POINT")
SHEET_END_POINT = os.environ.get("SHEET_END_POINT")
MY_AGE = 35
MY_GENDER = "male"
MY_WEIGHT_KG = 116
MY_HEIGHT = 178

user_input = input("Tell me which exercises you did:")

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
nutritionix_body = {
    "query": user_input,
    "gender": MY_GENDER,
    "weight_kg": MY_WEIGHT_KG,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE,
}

nutritionix_response = requests.post(url=EXERCISE_END_POINT, headers=nutritionix_headers, json=nutritionix_body)
nutritionix_result = nutritionix_response.json()
now_date = dt.datetime.now().strftime('%d/%m/%Y')
now_time = dt.datetime.now().strftime("%H:%M:%S")

sheety_headers = {
    "Authorization": SHEETY_Authorization
}

for exercise in nutritionix_result['exercises']:
    sheet_body = {
        "workout":
            {
                "date": now_date,
                "time": now_time,
                "exercise": exercise['name'].title(),
                "duration": str(exercise['duration_min']),
                "calories": str(exercise['nf_calories']),
            },
    }
    response = requests.post(url=SHEET_END_POINT, json=sheet_body, headers=sheety_headers)
    print(response.status_code)
