import pyowm

owm = pyowm.OWM('1060b54135410b3cf1bd80a73b8ac92a')  # You MUST provide a valid API key


# Will it be sunny tomorrow at this time in Utrecht ?
forecast = owm.daily_forecast("Utrecht,NL")
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)
x = forecast.will_be_sunny_at(tomorrow)

# Search for current weather in Utrecht

observation = owm.weather_at_place('Utrecht,NL')
w = observation.get_weather()
print("Utrecht\n", w)                      # <Weather - reference time=2013-12-18 09:20,
print(x)                                   # status=Clouds>

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print("weather Details")
print("The wind speed", w.get_wind(),'\n',
      "De hudige vochtigheid is:", w.get_humidity(), "\n"
      "De temperature  is:", w.temp)
