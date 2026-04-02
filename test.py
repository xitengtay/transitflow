import requests
import folium
from google.transit import gtfs_realtime_pb2
import time

URL = "https://www3.septa.org/gtfsrt/septarail-pa-us/Vehicle/rtVehiclePosition.pb"

def get_vehicle_positions():
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get(URL)
    feed.ParseFromString(response.content)
    return feed.entity

def create_map(entities):
    # Center map around Philadelphia
    m = folium.Map(location=[39.9526, -75.1652], zoom_start=11)

    for entity in entities:
        if entity.HasField("vehicle"):
            v = entity.vehicle

            lat = v.position.latitude
            lon = v.position.longitude

            label = f"""
                    Vehicle: {v.vehicle.id} \n
                    Trip: {v.trip.trip_id}
                    """

            folium.Marker(
                location=[lat, lon],
                popup=label,
                icon=folium.Icon(color="blue", icon="train", prefix="fa")
            ).add_to(m)

    return m

def main():
    while True:
        entities = get_vehicle_positions()
        m = create_map(entities)
        m.save("map.html")
        with open("map.html", "r+") as f:
            content = f.read()
            f.seek(0, 0)
            f.write('<meta http-equiv="refresh" content="15">\n' + content)
        print("Map saved to map.html")
        time.sleep(15)

if __name__ == "__main__":
    main()