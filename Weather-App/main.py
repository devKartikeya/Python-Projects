import requests

apiUrl = "8901d86538774341ae0163103260906"

print("Welcome to the Weather App built on Python!")

location = input("Enter your location: ")

# Fetch weather data
response = requests.get(
    f"https://api.weatherapi.com/v1/current.json?key={apiUrl}&q={location.strip()}&aqi=no"
)

if response.ok:
    data = response.json()
    loc = data["location"]
    weather = data["current"]

    # Location info
    print("\n📍 Location:")
    print(f"City: {loc['name']}")
    print(f"Region: {loc['region']}")
    print(f"Country: {loc['country']}\n")

    # Weather info
    print("🌤️  Current Weather:")
    print(f"Temperature: {weather['temp_c']}°C / {weather['temp_f']}°F")
    print(f"Condition: {weather['condition']['text']}")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind: {weather['wind_kph']} km/h {weather['wind_dir']}")
    print(f"Feels Like: {weather['feelslike_c']}°C")
    print(f"Cloud Cover: {weather['cloud']}%")
    print(f"Pressure: {weather['pressure_mb']} mb")
    print(f"Visibility: {weather['vis_km']} km")
else:
    print("❌ Error fetching weather data. Please check your API key or location.")