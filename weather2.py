from pyowm.owm import OWM
from sys import argv
from pyowm.utils import timestamps

city = argv[1]
owm = OWM('6b314425a78fac7f97eb283598883964')

mgr = owm.geocoding_manager()

list_of_locations = mgr.geocode(city)
a_city = list_of_locations[0]  # taking the first city in the list
latitude = a_city.lat
longitude = a_city.lon

mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
weather = observation.weather

print(f"\nShowing data for city: {argv[1]}")
print("Current weather: " + str(weather.detailed_status))

temp_dict_celsius = weather.temperature('celsius')
print(f"Current temp: {temp_dict_celsius['temp']:.1f} °C")
print(f"Todays max temp: {temp_dict_celsius['temp_max']:.1f} °C")
print(f"Todays min temp: {temp_dict_celsius['temp_min']:.1f} °C")
print(f"Feels like: {temp_dict_celsius['feels_like']:.1f} °C")

wind_dict_in_meters_per_sec = observation.weather.wind()
print(f"Current wind: {wind_dict_in_meters_per_sec['speed'] * 10/36:.2f} km/h")

rain_dict = mgr.weather_at_place(city).weather.rain

try:
    print(f"Last hour {rain_dict['1h']:.1f} mm of rain has fallen")
    try:
        print(f"Last 3 hours {rain_dict['3h']:.1f} mm of rain has fallen")
    except KeyError:
        pass
except KeyError:
    print("No rain currently")

pressure_dict = mgr.weather_at_place(city).weather.barometric_pressure()
print("Current pressure: " + str(pressure_dict['press']) + " hPa")








""" 
sunrise_iso = weather.sunrise_time(timeformat='iso')        COS JEST ZLE I POKAZUJE MI WSCHOD O 10 XD
print(sunrise_iso)                                          A ZACHOD O 1 W NOCY XD
sunrise_date = weather.sunrise_time(timeformat='date')
print(sunrise_date)

sunrise_unix = weather.sunrise_time()
print(sunrise_unix)
sunrset_date = weather.sunset_time(timeformat='date')
print(sunrset_date)
"""

#TOMORROW

one_call = mgr.one_call(latitude, longitude)
print(f"\nTomorrows morning it will feel like: {one_call.forecast_daily[0].temperature('celsius').get('feels_like_morn', None):.1f} °C")

three_h_forecaster = mgr.forecast_at_place(city, '3h')  # Forecaster object
tomorrow = timestamps.tomorrow()                   # datetime object for tomorrow
if three_h_forecaster.will_be_rainy_at(tomorrow):
    print("Tomorrow will be rainy")
else:
    print("Tomorrow will not be rainy")



"""
list_of_weathers = three_h_forecaster.when_clear()

status = []
daty = []
for i in range(len(list_of_weathers)):
    status.append(str(list_of_weathers[i]).split(","))
    if i % 3 == 1:
        daty.append(list_of_weathers[i])

print(len(list_of_weathers))
print(len(status))

s = "Name1=Value1;Name2=Value2;Name3=Value3"
print(dict(item.split("=") for item in s.split(";")))

print(dict(item.split(",") for item in str(list_of_weathers).split(",")))





daty = []
status = []
for i in range(len(list_of_weathers)):
    if i % 3 == 1:
        daty.append(list_of_weathers[i])
    elif i % 3 == 0:
        status.append(list_of_weathers[i])

print(daty)
print("\n")
print(status)
"""






