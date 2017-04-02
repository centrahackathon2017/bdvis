from sodapy import Socrata
from datetime import datetime
import dateutil.parser

DRY_RUN = False

client = Socrata("data.cityofgainesville.org", None)

counter = 0
for i in range(45):
    offset = i * 1000
    data = client.get("8b4k-2i2h", offset=offset, limit=1000)

    for row in data:
        try:
            pin = row["pin"]
            zone = row["zone"]
            if "mp_nzone_1" in row.keys():
                mp_nzone1 = row["mp_nzone_1"]
            else:
                mp_nzone1 = ""
            if "mp_nzone_2" in row.keys():
                mp_nzone2 = row["mp_nzone_2"]
            else:
                mp_nzone2 = ""
            locations = row["the_geom"]["coordinates"][0][0]
            locations = ["[%s,%s]" % (x, y) for x, y in locations]
            locations = "[%s]" % (",".join(locations))

            if not DRY_RUN:
                from core.models import Zone
                Zone(
                    pin=pin,
                    mp_nzone1=mp_nzone1,
                    mp_nzone2=mp_nzone2,
                    zone=zone,
                    locations=locations
                ).save()
                counter += 1

                if counter % 500 == 0:
                    print counter

        except KeyError:
            continue
