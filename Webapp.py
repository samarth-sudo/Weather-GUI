from flask import Flask, render_template, jsonify
import requests
from datetime import datetime

app = Flask(__name__)
start="2021-08-02 "
end = "2021-09-06"
API_KEY = " XQ9G79JHN6FJCCE9"
# ThingSpeak API endpoint and channel ID
API_ENDPOINT =url = f"https://thingspeak.com/channels/2051273/feeds.json?api_key={API_KEY}&start={start}&end={end}"

# ThingSpeak API read key


@app.route('/')
def index():
    # Fetch the latest data from ThingSpeak
    response = requests.get(API_ENDPOINT, params={"api_key": API_KEY, "results": 1})
    data = response.json()["feeds"][0]

    # Extract the sensor readings from the response
    temperature = data["field1"]
    humidity = data["field2"]
    pressure = data["field2"]

    # Render the sensor readings on the web app
    return render_template('index.html', temperature=temperature, humidity=humidity, pressure=pressure)

if __name__ == '__main__':
    app.run(debug=False)
