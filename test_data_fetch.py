import json
import requests

#仮で適当な値を変数に代入しています。
lat = 34.55
lon = 133.5
date = "2023-02-25T09:00:00+09:00"
#URL
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=weathercode,windspeed_10m,winddirection_10m&timezone=Asia%2FTokyo&datetime={date}"

#リクエスト
response = requests.get(url)

#レスポンス
#data = response.json()
#print(data)

#レスポンス
data = response.json()
print(data)

weather_data = {t: dict(zip(['天気', '風速', '風向'], d)) for t, *d in zip(*data['hourly'].values())}

print(weather_data.get('2023-02-24T20:00', None))

# {'天気': 0, '風速': 6.6, '風向': 9}