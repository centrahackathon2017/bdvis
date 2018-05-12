#usr/bin/python2.7
# -*- coding: utf-8 -*-

import psycopg2
import numpy as np

import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

###variable from front-end###
# lng = form.getvalue('lat')
# lat = form.getvalue('lng')
#############################

lat = 29.652
lng = -82.295185

print "Content-Type: text/html"     
print "Access-Control-Allow-Origin: *"  
print


def get_zone(point):
    sql = """SELECT ogc_fid
                FROM public.neighborhoods
                WHERE ST_Within(ST_GeomFromText('""" + point + """', 4432), ST_GeomFromWKB(wkb_geometry, 4432));"""
    cur.execute(sql)

    fetch = cur.fetchone()
    if fetch and len(fetch) > 0:
        return fetch[0]
    else:
         return 'no_zone'

# Connecting to database
conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='1234'")

# get zone
cur = conn.cursor()
point = 'POINT(' + str(lng) + ' ' + str(lat) + ')'
zone = get_zone(point)
print 'zone:', zone

# get zone data from 'zones' table, 
#   check if all data are not zero -> get data
#   if all data are zero -> find another zone ex. 86 or use another business type
sql = """SELECT *
            FROM public.zones
            WHERE ogc_fid = '""" + str(zone) + """';"""
cur.execute(sql)
data = cur.fetchone()
if data and len(data) > 0:
    if all(v == 0 for v in data[4:]):
        print 'Fail: zero data'
    else:
        data = data[4:]
else:
    print 'Fail: No zone'

# get coef from regression model
data = np.array(data)


# calculate probability