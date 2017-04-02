from sodapy import Socrata
from datetime import datetime

DRY_RUN = False

client = Socrata("data.cityofgainesville.org", None)

counter = 0
for i in range(2):
    offset = i * 1000
    data = client.get("w6tc-fr7z", offset=offset, limit=1000)

    for row in data:
        try:
            name = row["stop_name"]
            location = "[%s,%s]" % (row["the_geom"]["coordinates"][0], row["the_geom"]["coordinates"][1])

            # print name
            # print location

            if not DRY_RUN:
                from core.models import Poi
                Poi(
                    category="BUS STOP",
                    name=name,
                    location=location
                ).save()
                counter += 1

                if counter % 100 == 0:
                    print counter

        except KeyError:
            continue
