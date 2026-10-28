import requests

# We need coordinates to get weatherdata
latitude =48.85
longitude=2.35

# Build the API URLnwith our parameters
def get_weather(latitude,longitude):
    response= requests.get(url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
    data = response.json()
    return data['current']['temperature_2m']
# Make the request
haarlem_temp=get_weather(52.37,4.66)
maastricht_temp=get_weather(50.85,5.6955)
paris_temp = get_weather(48.85, 2.35)
barcelona_temp = get_weather(48.85, 2.35)
fuerteventura_temp = get_weather(28.43,-14.01)

print(f"Haarlem: {haarlem_temp} °C")
print(f"Maastricht: {maastricht_temp} °C")
print(f"Paris: {paris_temp} °C")
print(f"Barcelona: {barcelona_temp} °C")
print(f"Fuerteventura: {fuerteventura_temp} °C")

