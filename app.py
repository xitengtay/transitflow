import requests
from flask import Flask, jsonify
from google.transit import gtfs_realtime_pb2

app = Flask(__name__)

URL = "https://www3.septa.org/gtfsrt/septarail-pa-us/Vehicle/rtVehiclePosition.pb"

def get_vehicle_data():
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get(URL)
    feed.ParseFromString(response.content)

    vehicles = []

    for entity in feed.entity:
        if entity.HasField("vehicle"):
            v = entity.vehicle
            vehicles.append({
                "id": v.vehicle.id,
                "lat": v.position.latitude,
                "lon": v.position.longitude
            })

    return vehicles

@app.route("/api/vehicles")
def vehicles():
    return jsonify(get_vehicle_data())

@app.route("/")
def index():
    return open("index.html").read()

if __name__ == "__main__":
    app.run(debug=True)