import csv
import json
from collections import defaultdict

shapes = defaultdict(list)

with open("data/shapes.txt") as f:
    reader = csv.DictReader(f)
    for row in reader:
        shape_id = row["shape_id"]
        lat = float(row["shape_pt_lat"])
        lon = float(row["shape_pt_lon"])
        seq = int(row["shape_pt_sequence"])

        shapes[shape_id].append((seq, lat, lon))

# sort points by sequence
output = {}

for shape_id, points in shapes.items():
    points.sort()
    output[shape_id] = [(lat, lon) for _, lat, lon in points]

with open("data/shapes.json", "w") as f:
    json.dump(output, f)