from sodapy import Socrata
from datetime import datetime

DRY_RUN = False

client = Socrata("data.cityofgainesville.org", None)

counter = 0
for i in range(1):
    offset = i * 1000
    data = client.get("iye5-bzxs", offset=offset, limit=10)

    for row in data:
        try:
            locations = row["the_geom"]["coordinates"][0]
            locations = ["[%s,%s]" % (x, y) for x, y in locations]
            locations = "[%s]" % (",".join(locations))

            print locations

            if not DRY_RUN:
                from core.models import Parking
                Parking(
                    category="STREET",
                    locations=locations
                ).save()
                counter += 1

                if counter % 100 == 0:
                    print counter

        except KeyError:
            continue
