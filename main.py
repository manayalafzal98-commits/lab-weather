import httpx

city = input("Enter a city: ")

# 1. City name -> latitude/longitude
geo = httpx.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name": city, "count": 1},
).json()
place_list = geo.get("results")
if not place_list:
    print(f"Sorry, I couldn't find '{city}'.")
    exit()
place = place_list[0]

# 2. Latitude/longitude -> current weather
weather = httpx.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": place["latitude"],
        "longitude": place["longitude"],
        "current": "temperature_2m,wind_speed_10m",
    },
).json()
current = weather["current"]

print(f"{place['name']}, {place['country']}: "
      f"{current['temperature_2m']}°C, wind {current['wind_speed_10m']} km/h")