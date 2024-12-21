from flask import Flask, render_template,request
import requests
import os

app = Flask(__name__)

API_KEY = 'ef9a3d31837bf5a5ea1f5085a43aab92'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        response = requests.get(f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric')
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'City not found!'}

    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


