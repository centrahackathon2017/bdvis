from bs4 import BeautifulSoup
import requests
import locale
import json
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

DRY_RUN = False

zipcodes = [32601, 32603, 32605, 32606, 32607, 32608, 32809, 32641, 32653]

for zipcode in zipcodes:
    url = "http://boundaries.io/geographies/postal-codes?search=%d" % (zipcode)
    result = requests.get(url, headers={"Accept": "application/json"})
    result = json.loads(result.content)

    shapes = [_[0] for _ in result[0]["geometry"]["coordinates"]]

    if zipcode in [32605, 32606, 32608, 32809, 32641]:
        shapes = result[0]["geometry"]["coordinates"]
    else:
        shapes = [_[0] for _ in result[0]["geometry"]["coordinates"]]
    shapes = json.dumps(shapes, separators=(',', ':'))

    url = "http://zipatlas.com/us/fl/gainesville/zip-%d.htm" % (zipcode)

    result = requests.get(url)
    soup = BeautifulSoup(result.content, "html.parser")

    values = {
        "Total Population": None,
        "Households": None,
        # "Male": None,
        # "Female": None,
        "Under 5 years": None,
        "5 to 9 years": None,
        "10 to 14 years": None,
        "15 to 19 years": None,
        "20 to 24 years": None,
        "25 to 34 years": None,
        "35 to 44 years": None,
        "45 to 54 years": None,
        "55 to 59 years": None,
        "60 to 64 years": None,
        "65 to 74 years": None,
        "75 to 84 years": None,
        "85 years and over": None,
        # "25 years and over": None,
        "Less than 9th grade": None,
        "9th to 12th grade, no diploma": None,
        "High school graduate (includes equivalency)": None,
        "Some college, no degree": None,
        "Associate degree": None,
        "Bachelor's degree": None,
        "Graduate or professional degree": None,
    }

    tds = soup.findAll("td")
    for tag in tds:
        for key in values.keys():
            if tag.text == key:
                tag = tag.next_sibling
                values[key] = locale.atoi(tag.text)
                break

    values["25 years and over"] = sum([
        values["25 to 34 years"],
        values["35 to 44 years"],
        values["45 to 54 years"],
        values["55 to 59 years"],
        values["60 to 64 years"],
        values["65 to 74 years"],
        values["75 to 84 years"],
        values["85 years and over"]
    ])

    keys = [
        "Less than 9th grade",
        "9th to 12th grade, no diploma",
        "High school graduate (includes equivalency)",
        "Some college, no degree",
        "Associate degree",
        "Bachelor's degree",
        "Graduate or professional degree",
    ]

    tds = soup.findAll("td")
    for tag in tds:
        for key in keys:
            if tag.text == key:
                tag = tag.next_sibling.next_sibling.text[:-1].strip()
                values[key] = int(round(locale.atof(tag) * values["25 years and over"] * 0.01))
                break

    tds = soup.findAll("td")
    for tag in tds:
        if tag.text == "Gender":
            male = tag.parent.next_sibling.contents[1]
            values["Male"] = locale.atoi(male.text)
            female = tag.parent.next_sibling.next_sibling.contents[1]
            values["Female"] = locale.atoi(female.text)
        elif tag.text == "Employed":
            tag = tag.next_sibling.next_sibling.text[:-1].strip()
            values["Employed"] = int(round(locale.atof(tag) * values["Total Population"] * 0.01))

    keys = [
        "Agriculture, forestry, fishing and hunting, and mining",
        "Construction",
        "Manufacturing",
        "Wholesale trade",
        "Retail trade",
        "Transportation and warehousing, and utilities",
        "Information",
        "Finance, insurance, real estate, and rental and leasing",
        "Professional, scientific, management, administrative, and waste management services",
        "Educational, health and social services",
        "Arts, entertainment, recreation, accommodation and food services",
        "Other services (except public administration)",
        "Public administration",
    ]

    tds = soup.findAll("td")
    for tag in tds:
        for key in keys:
            if tag.text == key:
                tag = tag.next_sibling.next_sibling.text[:-1].strip()
                values[key] = int(round(locale.atof(tag) * values["Employed"] * 0.01))
                break

    keys = [
        "Less than $10,000",
        "$10,000 to $14,999",
        "$15,000 to $24,999",
        "$25,000 to $34,999",
        "$35,000 to $49,999",
        "$50,000 to $74,999",
        "$75,000 to $99,999",
        "$100,000 to $149,999",
        "$150,000 to $199,999",
        "$200,000 or more",
    ]

    tds = soup.findAll("td")
    for tag in tds:
        for key in keys:
            if tag.text == key:
                tag = tag.next_sibling.next_sibling.text[:-1].strip()
                values[key] = int(round(locale.atof(tag) * values["Households"] * 0.01))
                break

    print zipcode
    print shapes
    print values

    if not DRY_RUN:
        from core.models import Population
        Population(
            zipcode=zipcode,
            locations=shapes,
            total_people=values["Total Population"],
            total_households=values["Households"],
            males=values["Male"],
            females=values["Female"],
            age_under_5=values["Under 5 years"],
            age_5_9=values["5 to 9 years"],
            age_10_14=values["10 to 14 years"],
            age_15_19=values["15 to 19 years"],
            age_20_24=values["20 to 24 years"],
            age_25_34=values["25 to 34 years"],
            age_35_44=values["35 to 44 years"],
            age_45_54=values["45 to 54 years"],
            age_55_59=values["55 to 59 years"],
            age_60_64=values["60 to 64 years"],
            age_65_74=values["65 to 74 years"],
            age_75_84=values["75 to 84 years"],
            age_over_85=values["85 years and over"],
            edu_9th_grade=values["Less than 9th grade"],
            edu_12th_grade=values["9th to 12th grade, no diploma"],
            edu_high_school=values["High school graduate (includes equivalency)"],
            edu_college=values["Some college, no degree"],
            edu_associate=values["Associate degree"],
            edu_bachelors=values["Bachelor's degree"],
            edu_graduate=values["Graduate or professional degree"],
            incomes_below_10000=values["Less than $10,000"],
            incomes_10000_14999=values["$10,000 to $14,999"],
            incomes_15000_24999=values["$15,000 to $24,999"],
            incomes_25000_34999=values["$25,000 to $34,999"],
            incomes_35000_49999=values["$35,000 to $49,999"],
            incomes_50000_74999=values["$50,000 to $74,999"],
            incomes_75000_99999=values["$75,000 to $99,999"],
            incomes_100000_149999=values["$100,000 to $149,999"],
            incomes_150000_199999=values["$150,000 to $199,999"],
            incomes_over_200000=values["$200,000 or more"],
            industry_agriculture=values["Agriculture, forestry, fishing and hunting, and mining"],
            industry_construction=values["Construction"],
            industry_manufacturing=values["Manufacturing"],
            industry_wholesale=values["Wholesale trade"],
            industry_retail=values["Retail trade"],
            industry_transportion=values["Transportation and warehousing, and utilities"],
            industry_information=values["Information"],
            industry_financial=values["Finance, insurance, real estate, and rental and leasing"],
            industry_professional=values["Professional, scientific, management, administrative, and waste management services"],
            industry_social=values["Educational, health and social services"],
            industry_arts=values["Arts, entertainment, recreation, accommodation and food services"],
            industry_other=values["Other services (except public administration)"],
            industry_public=values["Public administration"]
        ).save()
