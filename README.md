# Lab Weather 🌤️

A small Python script that shows the **live weather for any city**, using the free [Open-Meteo](https://open-meteo.com/) API (no API key needed).
## How it works
1. Asks you for a city name.
2. Calls the Open-Meteo **Geocoding API** to find the city's latitude and longitude.
3. Calls the Open-Meteo **Forecast API** to get the current temperature and wind speed.
4. Prints a short summary.
