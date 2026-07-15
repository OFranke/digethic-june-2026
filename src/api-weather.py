import requests

latitude = 52.5244
longitude = 13.4105

location_name = "Berlin"

print(
    "Der Wohnort ist "
    + location_name
    + " mit den Koordinaten: "
    + str(latitude)
    + ", "
    + str(longitude)
)

forecast_params = {
    "latitude": latitude,
    "longitude": longitude,
    "daily": "temperature_2m_max",
}


forecast_url = "https://api.open-meteo.com/v1/forecast"

response = requests.get(forecast_url, params=forecast_params)

data = response.json()
# print(data)

for i in range(len(data["daily"]["time"])):
    print(
        "Um "
        + str(data["daily"]["time"][i])
        + " Uhr "
        + str(data["daily"]["temperature_2m_max"][i])
        + "°C"
    )
