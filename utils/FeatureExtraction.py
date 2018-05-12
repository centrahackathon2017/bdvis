#usr/bin/python2.7
# -*- coding: utf-8 -*-

import psycopg2
import pandas as pd
import urllib2
import json
import numpy as np

API_KEY = 'AIzaSyAAnIM7PVY2KQnE5WPmnHOcsuqNwSJqeHY'

def get_lat_long(address):
    address_replace = address.replace(' ', '%20')
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + \
            address_replace + '&key=' + API_KEY
    print url
    contents = urllib2.urlopen(url)
    obj = json.load(contents)
    if obj['status'] == 'OK':
        loc = obj['results'][0]['geometry']['location']
        lat = loc['lat']
        lng = loc['lng']
        return 'POINT(' + str(lng) + ' ' + str(lat) + ')'
    else :
        print 'ERROR: Cannot get point from ', address
        return None

def get_zone(point):
    sql = """SELECT ogc_fid
                FROM public.neighborhoods
                WHERE ST_Within(ST_GeomFromText('""" + point + """', 4432), ST_GeomFromWKB(wkb_geometry, 4432));"""
    cur.execute(sql)

    fetch = cur.fetchone()
    if fetch and len(fetch) > 0:
        return fetch[0]
    else:
         return None

# Connecting to database
conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='1234'")

# get all active businesses in specified type
cur = conn.cursor()
cur.execute("""SELECT type, id, name, start_date, physical_addr, mailing_addr, mailing_city, phone, email, contact, location
                    FROM public.active_businesses
                    WHERE type = 'RESTAURANT';""")
restaurants = cur.fetchall()

# convert to dataframe
restaurants_df = pd.DataFrame(restaurants, index=range(0,len(restaurants)),
                    columns=['type', 'id', 'name', 'start_date', 'physical_addr', 'mailing_addr', 'mailing_city', 'phone', 'email', 'contact', 'location'],
                    dtype=None, copy=False)

# get lat long of each restaurant (or any type)
dataset_df = restaurants_df[['id', 'name', 'start_date', 'physical_addr', 'location']]
points = []
for index, row in dataset_df.iterrows():
    spl = row['location'].split('(')
    if spl and len(spl) > 1:
        location = spl[1]
        spl2 = location.split(',')
        if spl2 and len(spl2) > 1:
            lat = spl2[0]
            lng = spl2[1][1:-1]
            point = 'POINT(' + lng + ' ' + lat + ')'
            points.append(point)
            continue
    
    #if lat long are not provided
    points.append('None')

# add lat long to dataframe
dataset_df['point'] = points

# filter out row which doesn't have lat long data
dataset_df = dataset_df[dataset_df.point != 'None']

# get neighbourhood zone id
neighbourhood_id = []
i = 0
for index, row in dataset_df.iterrows():
    point = row['point']
    zone = get_zone(point)

    if zone:
        neighbourhood_id.append(zone)
    else:
        neighbourhood_id.append(-1)

    i += 1

# add neighbourhood id to df
dataset_df['zone_id'] = neighbourhood_id
# print dataset_df

############ Extract zone data ############
### get list of zones id
sql = """SELECT ogc_fid
            FROM public.neighborhoods"""
cur.execute(sql)

list_of_zones = [x[0] for x in cur.fetchall()] #note that zone ids are always sorted
max_zone_id = np.max(np.array(list_of_zones))
print 'list_of_zones', list_of_zones
print 'max_zone_id', max_zone_id

### get total number of businesses in this business_type in each zone
zone_total_bussinesses = np.zeros(shape = (max_zone_id))
for zone in list_of_zones:
    zone_total_bussinesses[zone-1] = len(dataset_df[dataset_df.zone_id == zone])

print 'zone_total_bussinesses', len(zone_total_bussinesses), zone_total_bussinesses

### get total number of apartments in each zone
'''
# ** for first time only we need to get point from address
sql = """SELECT type, id, name, address, city, location
	        FROM public.apartment;"""
cur.execute(sql)
apartments = cur.fetchall()

sql = """ALTER TABLE public.apartment
            ADD COLUMN point geometry,
            ADD COLUMN zone integer;"""
cur.execute(sql)
conn.commit()

for apartment in apartments:
    index = apartment[1]
    address = apartment[3] + ' ' + apartment[4]

    # get point from address
    point = get_lat_long(address)

    # check what zone it is
    if point:
        zone = get_zone(point)
        # update zone data to table
        sql = """UPDATE public.apartment
                    SET point = ST_GeomFromText('""" + point +  """')
                    WHERE id = '""" + str(index) + """';"""
        print sql
        cur.execute(sql)

        if zone:
            sql = """UPDATE public.apartment
                        SET zone = """ + str(zone) +  """
                        WHERE id = '""" + str(index) + """';"""
            print sql
            cur.execute(sql)

            print index, address, point, zone
    
    conn.commit()
    print
    print
'''

sql = """SELECT zone
	        FROM public.apartment;"""
cur.execute(sql)
apartments = cur.fetchall()
zone_number_of_apartments = np.zeros( shape = (max_zone_id) )

for apartment in apartments:
    a = apartment[0]
    if a and a != -1:
        zone_number_of_apartments[a-1] += 1
print 'zone_number_of_apartments', len(zone_number_of_apartments), zone_number_of_apartments

'''
### get total number of crimes in each zone
# ** for first time only we need to get point from address
sql = """SELECT type, id, report_date, offense_date, city, state, location
	        FROM public.crimes;"""
cur.execute(sql)
crimes = cur.fetchall()

sql = """ALTER TABLE public.crimes
            ADD COLUMN point geometry,
            ADD COLUMN zone integer;"""
cur.execute(sql)
conn.commit()

for crime in crimes:
    index = crime[1]
    spl = crime[6].split('(')
    if spl and len(spl) > 1:
        location = spl[1]
        spl2 = location.split(',')
        if spl2 and len(spl2) > 1:
            lat = spl2[0]
            lng = spl2[1][1:-1]
            point = 'POINT(' + lng + ' ' + lat + ')'
            print point

    # check what zone it is
    if point:
        try:
            zone = get_zone(point)
            # update zone data to table
            sql = """UPDATE public.crimes
                        SET point = ST_GeomFromText('""" + point +  """')
                        WHERE id = '""" + str(index) + """';"""
            print sql
            cur.execute(sql)

            if zone:
                sql = """UPDATE public.crimes
                            SET zone = """ + str(zone) +  """
                            WHERE id = '""" + str(index) + """';"""
                print sql
                cur.execute(sql)

                print index, point, zone
        except Exception as e:
            print e
    
    conn.commit()
    print
    print
'''
sql = """SELECT zone
	        FROM public.crimes;"""
cur.execute(sql)
crimes = cur.fetchall()
zone_number_of_crimes = np.zeros( shape = (max_zone_id) )

for crime in crimes:
    a = crime[0]
    if a and a != -1:
        zone_number_of_crimes[a-1] += 1

print 'zone_number_of_crimes', len(zone_number_of_crimes), zone_number_of_crimes


### get many features from Restaurant.csv (on github)
sql = """SELECT name, id, address, zipcode, latitude, longitude, total_pop, households, male, female, white, black, ameri_es, asian, hawn_pi, other, multi_race, hispanic, age_below_18, age_18_40, age_40_65, age_65, age_median, tran_total, tran_car, tran_moto, tran_bike, tran_pub, tran_walk, tran_other, tran_home, student, less_10k, "10k_14k", "15k_19k", "20k_24k", "25k_29k", "30k_34k", "35k_39k", "40k_44k", "45k_49k", "50k_59k", "60k_74k", "75k_99k", "100k_124k", "125k_149k", "150k_199k", "120k_more"
	        FROM public.restaurants;"""
cur.execute(sql)
businesses = cur.fetchall()
zone_other_features = np.zeros( shape = (max_zone_id, 42) )
exist = []
for business in businesses:
    # what zone is it in
    point = 'POINT(' + str(business[5]) + ' ' + str(business[4]) + ')'
    zone = get_zone(point)

    if zone:
        if np.sum(zone_other_features[zone-1]) > .0:
            # if already keep this zone data in the list, don't care
            continue
        else:
            # else keep all columns to be features of this zone
            print 'zone', zone
            zone_other_features[zone-1] = business[6:]
            exist.append(zone)

print 'zone_other_features', len(zone_other_features), zone_other_features
print 'zone exists:', exist


# save zone info to database (all variable starts with 'zone_')
# ** for first time only since we already save all features to 'zones' table
for i, zone in enumerate(list_of_zones):
    values = str(zone) + ', ' + str(zone_total_bussinesses[i]) + ', ' + \
                str(zone_number_of_apartments[i]) + ', ' + str(zone_number_of_crimes[i]) + ', '
    
    if not all(v == 0 for v in zone_other_features[zone-1]):
        zone_features = [str(z) for z in zone_other_features[zone-1]]
        for z in zone_other_features[zone-1]:
            values += str(z) + ', '
        values = values[:-2]
    else:
        for jj in range(0, 42):
            values += '0, '
        values = values[:-2]

    sql = """INSERT INTO public.zones(
	ogc_fid, total_businesses, total_apartments, number_of_crimes, total_pop, households, male, female, white, black, ameri_es, asian, hawn_pi, other, multi_race, hispanic, age_below_18, age_18_40, age_40_65, age_65, age_median, tran_total, tran_car, tran_moto, tran_bike, tran_pub, tran_walk, tran_other, tran_home, student, less_10k, "10k_14k", "15k_19k", "20k_24k", "25k_29k", "30k_34k", "35k_39k", "40k_44k", "45k_49k", "50k_59k", "60k_74k", "75k_99k", "100k_124k", "125k_149k", "150k_199k", "120k_more")
	VALUES (""" + values + """);"""
    print sql
    print
    cur.execute(sql)
    conn.commit()


############ Extract more features from each business point ############
### Is it in enterprise zone
is_in_enterprise = []
for index, row in dataset_df.iterrows():
    point = row['point']
    sql = """SELECT ogc_fid
            FROM public.enterprise_zone
            WHERE ST_Within(ST_GeomFromText('""" + point + """', 4432), ST_GeomFromWKB(wkb_geometry, 4432));"""
    cur.execute(sql)

    fetch = cur.fetchone()
    if fetch and len(fetch) > 0:
        # in enterprise zone
        is_in_enterprise.append(1)
    else:
        is_in_enterprise.append(0)

# add is-in-enterprise-zone to df
dataset_df['is_in_enterprise'] = is_in_enterprise

### number of nearby same type business
distance = 300 # (within 300 m.)
number_of_nearby_business = []
for index, row in dataset_df.iterrows():
    point = row['point']
    sql = """
        SELECT count(name)
        FROM public.restaurants
        WHERE ST_DWithin (
            ST_SetSRID(ST_MakePoint(longitude, latitude), 4326),
            ST_GeomFromText('""" + point +  """', 4326), """ + str(distance) + """, true
        );
    """
    cur.execute(sql)

    fetch = cur.fetchone()
    if fetch and len(fetch) > 0:
        number_of_nearby_business.append(fetch[0])
    else:
        number_of_nearby_business.append(0)

# add number_of_nearby_business to df
dataset_df['nearby_business'] = number_of_nearby_business


### number of nearby apartment (within 300 m.)
distance = 500 # (within 300 m.)
number_of_nearby_apartment = []
for index, row in dataset_df.iterrows():
    point = row['point']
    sql = """
        SELECT count(name)
        FROM public.apartment
        WHERE ST_DWithin (
            ST_SetSRID(point, 4326),
            ST_GeomFromText('""" + point +  """', 4326), """ + str(distance) + """, true
        );
    """
    cur.execute(sql)

    fetch = cur.fetchone()
    if fetch and len(fetch) > 0:
        number_of_nearby_apartment.append(fetch[0])
    else:
        number_of_nearby_apartment.append(0)

# add number_of_nearby_apartment to df
dataset_df['nearby_apartment'] = number_of_nearby_apartment


### open business years
from datetime import date, datetime
now = datetime.now().date()
years = []

for index, row in dataset_df.iterrows():
    start_date = row['start_date']
    diff = (now - start_date)
    years.append(diff.days / 365)

# add opening years to df
dataset_df['years'] = years

"""
print
print 'Grouping..'
print 'years < 5:', len(dataset_df[dataset_df.years < 5])
print 'years >= 5 and < 15:', len(dataset_df[(dataset_df.years >= 5) & (dataset_df.years <15)])
print 'years >= 15 and < 25:', len(dataset_df[(dataset_df.years >= 5) & (dataset_df.years <15)])
print 'years >= 25 and < 35:', len(dataset_df[(dataset_df.years >= 25) & (dataset_df.years <35)])
print 'years >= 35 :', len(dataset_df[dataset_df.years >= 35])
print
"""

print
print 'Grouping..'
print 'years <= 5:', len(dataset_df[dataset_df.years <= 5])
print 'years > 5 :', len(dataset_df[dataset_df.years > 5])
print

### how far from the nearest car park --> the restaurants may provide their own parking (not public)

### Is there any bus pass this way or nearby



### combine zone data with active businesses list (dataset_df with zone table)
# filter all point in zone which are not in exist
print 'before', dataset_df.shape
dataset_df = dataset_df[dataset_df.zone_id.isin(exist)]
print 'after', dataset_df.shape

# combine
dataset_arr = []
years_arr = []
fail_index = []
for i in range(0, len(dataset_df)):
    dataset_arr.append([])

index = 0
for iii, row in dataset_df.iterrows():
    # dataset_arr[index] = [row['id']]
    # dataset_arr[index].append(row['name'])
    # dataset_arr[index].append(row['start_date'])
    # dataset_arr[index].append(row['physical_addr'])
    # dataset_arr[index].append(row['location'])
    # dataset_arr[index].append(row['point'])
    dataset_arr[index].append(row['zone_id'])
    # dataset_arr[index].append(row['is_in_enterprise'])
    # dataset_arr[index].append(row['nearby_business'])
    # dataset_arr[index].append(row['nearby_apartment'])
    
    sql = """
        SELECT total_businesses, total_apartments, number_of_crimes, total_pop, households, male, female, white, black, ameri_es, asian, hawn_pi, other, multi_race, hispanic, age_below_18, age_18_40, age_40_65, age_65, age_median, tran_total, tran_car, tran_moto, tran_bike, tran_pub, tran_walk, tran_other, tran_home, student, less_10k, "10k_14k", "15k_19k", "20k_24k", "25k_29k", "30k_34k", "35k_39k", "40k_44k", "45k_49k", "50k_59k", "60k_74k", "75k_99k", "100k_124k", "125k_149k", "150k_199k", "120k_more"
	    FROM public.zones
        WHERE ogc_fid = '""" + str(row['zone_id']) + """';
    """
    cur.execute(sql)

    fetch = cur.fetchone()

    if fetch and len(fetch) > 0:
        years_arr.append(row['years'])
        for f in fetch:
            dataset_arr[index].append(f)
        index += 1


print 'dataset_arr', len(dataset_arr)
print 'years_arr', len(years_arr)
print


## calculate number of open business in last 3 years in each zone
last_3_years = dict()
for iii, row in dataset_df.iterrows():
    z = row['zone_id']
    if not z in last_3_years:
        num = len([r['zone_id'] for i, r in dataset_df.iterrows() if r['years'] <= 4 and r['zone_id'] == z])
        last_3_years[z] = num
print 'last_3_years,', last_3_years

## calculate ratio of number of open business in last 3 years to total numbers of business in each zone
ratio = dict()
for iii, row in dataset_df.iterrows():
    z = row['zone_id']
    if not z in ratio:
        num = len([r['zone_id'] for i, r in dataset_df.iterrows() if r['zone_id'] == z])
        ratio[z] = last_3_years[z]*1.0 / num
print 'ratio,', ratio

## use ratio to be y
Y_ratio = []
for iii, row in dataset_df.iterrows():
    Y_ratio.append(ratio[row['zone_id']])

print dataset_arr

np.save('X_data3', dataset_arr)
np.save('Year_data3', years_arr)
np.save('Y_ratio3', Y_ratio)


### perform a machine learning model
# 1) SVM with Y = 0 if years <= 5, 1 if years > 5
# 2) K-Means and compare with Years grouping