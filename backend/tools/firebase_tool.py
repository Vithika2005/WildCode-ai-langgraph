import requests
from config import FIREBASE_URL, SENSOR_PATH

def get_sensor_data():
    url = f"{FIREBASE_URL}{SENSOR_PATH}"
    
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if not isinstance(data, dict):
            return {}

        return data

    except Exception as e:
        print("Firebase ERROR:", e)
        return {}
