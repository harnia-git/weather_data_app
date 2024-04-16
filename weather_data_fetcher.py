# /**
#    * https://open-meteo.com/en/docs
#    * 
#    * - Location : Tokyo … Latitude : 35.6785 ・ Longitude : 139.6823
#    * - Hourly Weather Variables : Temperature (2 m) ・ Weathercode
#    * - Current Weather With Temperature, Windspeed And Weather Code
#    * - Temperature Unit : Celsius °C
#    * - Timeformat : ISO 8601 (ex. YYYY-MM-DDTHH:mm)
#    * - Timezone : Azia/Tokyo
#    * - Past Days : 2
#    */
import requests
import math
import json

# nagasakiの
#url = 'https://api.open-meteo.com/v1/forecast?latitude=32.7503&longitude=129.8779&hourly=temperature_2m,weathercode&current_weather=true&timezone=Asia%2FTokyo&past_days=6'
#response = requests.get(url).json()
#response = requests.get(url)
#data = json.loads(response.text)
#print(data)
url = f'https://api.open-meteo.com/v1/forecast?latitude=32.7503&longitude=129.8779&hourly=temperature_2m,weathercode&current_weather=true&timezone=Asia%2FTokyo&past_days=6'
response = requests.get(url)
data = json.loads(response.text)
#print(data)
for d in data['hourly']:
     #if 0 in d['weathercode']:
        #print('hare', d['time'])
    print(d)
current_weather = data['current_weather']
print(current_weather)  
#forecast = data[""]["forecastday"][0]["hour"]
 #forecast = data["forecast"]["forecastday"][0]["hour"]

# for hour in forecast:
#     time = hour["time"]
#     temperature = hour["temperature"]
#     condition = hour["condition"]["text"]
#     print(f"Time: {time}, Temperature: {temperature}°C, Condition: {condition}")
       



# ラベルを表示
labels = data.keys()
for label in labels:
    print(label)
#レスポンス
#data = response
#weather_data = {t: dict(zip(['天気', '風速', '風向'], d)) for t, *d in zip(*data['hourly'].values())}
print('-------')
weather_data = {}
hourly_values = data['hourly'].values()

for t, *d in zip(*hourly_values):
    print(d)
   # weather_info = {}
   # weather_info['天気'] = d[0] if len(d) > 0 else None
   # weather_info['風速'] = d[1] if len(d) > 1 else None
   # weather_info['風向'] = d[2] if len(d) > 2 else None
   # weather_data[t] = weather_info

print(weather_data.get('2023-06-10T20:00', None))

# {'天気': 0, '風速': 6.6, '風向': 9}


def slice_arrays(array, number):
    sliced_arrays = []
    array_length = len(array)
    num_slices = math.ceil(array_length / number)

    for index in range(num_slices):
        start = index * number
        end = (index + 1) * number
        sliced_array = array[start:end]
        sliced_arrays.append(sliced_array)

    return sliced_arrays