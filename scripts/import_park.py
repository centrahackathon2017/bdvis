from sodapy import Socrata
from datetime import datetime

DRY_RUN = False

client = Socrata("data.cityofgainesville.org", None)

counter = 0
for i in range(1):
    offset = i * 1000
    data = client.get("fyxq-xtpn", offset=offset, limit=1000)

    for row in data:
        try:
            park = row["park"]
            location = "[%s,%s]" % (row["the_geom"]["coordinates"][0], row["the_geom"]["coordinates"][1])

            print park
            print location

            if not DRY_RUN:
                from core.models import Poi
                Poi(
                    category="PARK",
                    name=park,
                    location=location
                ).save()
                counter += 1

                if counter % 100 == 0:
                    print counter

        except KeyError:
            continue
