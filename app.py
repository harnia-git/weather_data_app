from flask import Flask, render_template, request
import requests
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def fetch_weather_data(lat, lon, days):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_min,temperature_2m_max&timezone=Asia%2FTokyo&past_days={days}"
    response = requests.get(url)
    return response.json()

def plot_weather_data(data):
    df = pd.DataFrame({
        'date': data['daily']['time'],
        'temp_min': data['daily']['temperature_2m_min'],
        'temp_max': data['daily']['temperature_2m_max']
    })
    plt.figure()
    df.set_index('date')[['temp_min', 'temp_max']].plot()
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url

@app.route('/', methods=['GET', 'POST'])
def index():
    plot_url = None
    if request.method == 'POST':
        lat = request.form.get('latitude', type=float)
        lon = request.form.get('longitude', type=float)
        days = request.form.get('days', type=int)
        data = fetch_weather_data(lat, lon, days)
        plot_url = plot_weather_data(data)
    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
