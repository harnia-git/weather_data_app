import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # APIからデータを取得
    #仮で適当な値を変数に代入しています。
    lat = 32.7503
    lon = 129.8779
    date = "2023-06-06T09:00:00+09:00"
    #url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m&timezone=Asia%2FTokyo&past_days=14"
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m,relativehumidity_2m,windspeed_10m&timezone=Asia%2FTokyo&past_days=14"
    response = requests.get(url)
    data = response.json()

    return jsonify(data)  # JSONデータを返す

if __name__ == '__main__':
    app.run()
