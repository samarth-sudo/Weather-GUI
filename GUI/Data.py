import requests
CHANNEL_ID = '2051273'
API_KEY = 'XQ9G79JHN6FJCCE9'
start_date="2021-08-02"
end_date = "2021-09-06"
# Replace YOUR_CHANNEL_ID with your actual ThingSpeak Channel ID
# Replace YOUR_READ_API_KEY with your actual ThingSpeak Read API Key
url = f"https://thingspeak.com/channels/2051273/feeds.json?api_key={API_KEY}&start={start_date}&end={end_date}"

response = requests.get(url)
data = response.json()

# Extract the latest entry from the feed
latest_entry = data["feeds"][0]
print(data)
# Print the field values of the latest entry
print("Temperature: ", latest_entry["field1"])
print("Humidity: ", latest_entry["field2"])
print("Pressure:", latest_entry["field3"])

