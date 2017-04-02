from sodapy import Socrata
from datetime import datetime
import dateutil.parser

DRY_RUN = False

client = Socrata("data.cityofgainesville.org", None)

counter = 0
for i in range(7):
    offset = i * 1000
    data = client.get("hk2b-em59", offset=offset, limit=1000)

    for row in data:
        try:
            business_type = row["business_type"]
            name = row["name"]
            start_date = dateutil.parser.parse(row["start_date"]).date()
            location_address = row["location_address"]
            mailing_address = row["mailing_address"]
            business_phone = row["business_phone"]
            email = row["email"]
            location = "[%s,%s]" % (row["location"]["latitude"], row["location"]["longitude"])

            if not DRY_RUN:
                from core.models import Business
                Business(
                    category=business_type,
                    name=name,
                    start_date=start_date,
                    physical_address=location_address,
                    mailing_address=mailing_address,
                    business_phone=business_phone,
                    email=email,
                    location=location
                ).save()
                counter += 1

                if counter % 100 == 0:
                    print counter

        except KeyError:
            continue
