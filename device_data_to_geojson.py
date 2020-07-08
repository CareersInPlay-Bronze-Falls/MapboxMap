import csv
import sys
import json
from collections import defaultdict

IN_FILENAME = sys.argv[1]


in_csv_file = csv.DictReader(open(IN_FILENAME, 'r'))
featuresByGroup = defaultdict(list)

geojson = {
    "type": "FeatureCollection",
    "features": []
}


for row in in_csv_file:
    geojson['features'].append(
        {
            "type": "Feature",
            "properties": {
                "name": row['name'],
                "deviceId": row['deviceId'],
                "group": row['group']
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    float(row["longitude"]),
                    float(row["latitude"])
                ]
            }
        }
    )

with open("devices.json", 'w') as f:
    f.write(json.dumps(geojson))
