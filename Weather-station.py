import pyowm

owm = pyowm.OWM('1060b54135410b3cf1bd80a73b8ac92a')  # You MUST provide a valid API key
owm_nl = pyowm.OWM(language='nl') # Nederlandse taal


# def weather(Utrecht):
#     observation = owm.weather_at_place('Utrecht',owm_nl)
#     today = observation.get_weather

#Forcast will it rrain in Utrecht Tomorrow
forecast = owm.daily_forecast('Utrecht,nl',limit=5)
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_rainy_at(tomorrow)
x = forecast.will_be_rainy_at(tomorrow)
# print ('will it rain?:', x)

# search Current weather
observation = owm.weather_at_place('Utrecht,NL')
w = observation.get_weather()

# Weather details
w.get_wind()                                        # {'speed': 4.6, 'deg': 330}
w.get_humidity()                                    # 87 (vochtigheid)
w.get_rain()                                        # volume regen
w.get_temperature(unit='celsius')                   # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.get_clouds()                                      # Cloud Coverage
w.get_detailed_status()                             # Get detailed weather status


# print ('Vandaag is het weer:','\n',
#        'Status:', w.get_detailed_status() )

fc =owm.three_hours_forecast('Utrecht,nl')
f = fc.get_forecast()
f.get_reception_time('iso')
fc.when_ends()
lst = f.get_weathers()
for weather in lst:
    print (weather.get_reference_time('iso'),weather.get_detailed_status())


# Will it be sunny tomorrow at this time in Utrecht ?
# forecast = owm.daily_forecast("Utrecht,NL")
# tomorrow = pyowm.timeutils.tomorrow()
# forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)
# x = forecast.will_be_sunny_at(tomorrow)

# Search for current weather in Utrecht
#
# observation = owm.weather_at_place('Utrecht,NL')
# w = observation.get_weather()
# print("Utrecht\n", w)                      # <Weather - reference time=2013-12-18 09:20,
# print(x)                                   #status cloudy
#
# # Weather details
# w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# w.get_temperature(unit='celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# print("weather Details")
# print("The wind speed", w.get_wind(),'\n',
#       "De hudige vochtigheid is:", w.get_humidity(), "\n"
#       "De temperature  is:", w.get_temperature('celsius'))