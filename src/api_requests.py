import requests
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "hourly": "temperature_2m"
}
headers = {"Content-Type": "application/json"}
result = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params=params,
    headers=headers
)
print(result)
json = result.json()
print("JSON response: ", json)
