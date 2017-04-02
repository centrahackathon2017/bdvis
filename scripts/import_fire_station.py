from sodapy import Socrata
from datetime import datetime

DRY_RUN = True

client = Socrata("data.cityofgainesville.org", None)

counter = 0
for i in range(1):
    offset = i * 1000
    data = client.get("nfs9-huac", offset=offset, limit=1000)

    for row in data:
        try:
            name = row["station"]
            location = "{%s,%s}" % (row["the_geom"]["coordinates"][0], row["the_geom"]["coordinates"][1])

            print name
            print location

            if not DRY_RUN:
                from core.models import Poi
                Poi(
                    category="FIRE STATION",
                    name=station,
                    location=the_geom
                ).save()
                counter += 1

                if counter % 100 == 0:
                    print counter

        except KeyError:
            continue
