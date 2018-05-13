import psycopg2
import numpy as np

# lat = 29.652
# lng = -82.295185

def predict(lat, lng): 
  conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='1234'")

  # get zone
  cur = conn.cursor()
  point = 'POINT(' + str(lng[0]) + ' ' + str(lat[0]) + ')'

  sql = """SELECT ogc_fid
                FROM public.neighborhoods
                WHERE ST_Within(ST_GeomFromText('""" + point + """', 4432), ST_GeomFromWKB(wkb_geometry, 4432));"""

  cur.execute(sql)
  fetch = cur.fetchone()

  zone = 'no_zone'
  if fetch and len(fetch) > 0:
    zone = fetch[0]

  # get zone data from 'zones' table, 
  # check if all data are not zero -> get data
  # if all data are zero -> find another zone ex. 86 or use another business type
  sql = """SELECT *
              FROM public.zones
              WHERE ogc_fid = '""" + str(zone) + """';"""
  cur.execute(sql)
  fetch = cur.fetchone()
  data = None

  if fetch and len(fetch) > 0:
    if all(v == 0 for v in fetch[4:]):
      print('{"result": "fail", "msg": "zero data"}')
      return 'Unknown'      
    else:
      data = fetch[2:]
  else:
      print('{"result": "fail", "msg": "no zone"}')
      return 'Unknown'

  if data:
    ## calculate probability
    import numpy as np
    from sklearn.preprocessing import PolynomialFeatures
    import random
    from sklearn.linear_model import LinearRegression
    from sklearn.pipeline import Pipeline

    X = np.load("C:\\Users\\UC238617\\Desktop\\bdvis\\utils\\X_data3.npy")
    Y = np.load("C:\\Users\\UC238617\\Desktop\\bdvis\\utils\\Y_ratio3.npy")

    X_no_zone = []
    Y_no_zone = []
    zones = []
    for x, y in zip(X, Y):
        if not x[0] in zones:
            X_no_zone.append(x[2:len(x)])
            zones.append(x[0])
            Y_no_zone.append(y)

    clf = Pipeline([('poly', PolynomialFeatures(degree=2)),
                    ('linear', LinearRegression(fit_intercept=False))])

    # fit to an order-3 polynomial data
    model = clf.fit(X_no_zone, Y_no_zone)

   
    threshold = 0.1
    miss_less_than_threshold = 0
    summation = 0

    for i, x in enumerate(X_no_zone):
        # print 'zone:', zones[i]
        pred = model.predict([x])
        summation += pow(Y_no_zone[i] - pred, 2)
        if abs(Y_no_zone[i] - pred) <= threshold:
            miss_less_than_threshold += 1
            print('true:', "{0:.3f}".format(float(Y_no_zone[i])), '\tpredict:', "{0:.3f}".format(float(pred)), '***')
        else:
            print('true:', "{0:.3f}".format(float(Y_no_zone[i])), '\tpredict:',  "{0:.3f}".format(float(pred)))
            pass

    print('Miss less than threshold:', miss_less_than_threshold)
    print('RMSE:', summation/len(Y_no_zone))

    success = model.predict([list(data)])
    if success[0] <= 0:
      success = 0
    else:
      success = int(float(success[0])*100)
    return success

  else:
    return 'Unknown'












# #!C:\Users\UC238617\AppData\Local\Programs\Python\Python36\python
# # -*- coding: utf-8 -*-

# import psycopg2
# import numpy as np

# import cgitb
# cgitb.enable()

# import cgi
# form = cgi.FieldStorage()

# ###variable from front-end###
# # lng = form.getvalue('lat')
# # lat = form.getvalue('lng')
# #############################

# lat = 29.652
# lng = -82.295185

# # print "Content-Type: text/html"     
# # print "Access-Control-Allow-Origin: *"  
# # print

# def get_zone(point):
#     sql = """SELECT ogc_fid
#                 FROM public.neighborhoods
#                 WHERE ST_Within(ST_GeomFromText('""" + point + """', 4432), ST_GeomFromWKB(wkb_geometry, 4432));"""
#     cur.execute(sql)

#     fetch = cur.fetchone()
#     if fetch and len(fetch) > 0:
#         return fetch[0]
#     else:
#          return 'no_zone'

# # Connecting to database
# conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='1234'")

# # get zone
# cur = conn.cursor()
# point = 'POINT(' + str(lng) + ' ' + str(lat) + ')'
# zone = get_zone(point)
# # print 'zone:', zone

# # get zone data from 'zones' table, 
# #   check if all data are not zero -> get data
# #   if all data are zero -> find another zone ex. 86 or use another business type
# sql = """SELECT *
#             FROM public.zones
#             WHERE ogc_fid = '""" + str(zone) + """';"""
# cur.execute(sql)
# fetch = cur.fetchone()
# data = None
# if fetch and len(fetch) > 0:
#     if all(v == 0 for v in fetch[4:]):
#         print('{"result": "fail", "msg": "zero data"}')
#     else:
#         data = fetch[2:]
# else:
#     print('{"result": "fail", "msg": "no zone"}')

# if data:
#     ## calculate probability
#     import numpy as np
#     from sklearn.preprocessing import PolynomialFeatures
#     import random
#     from sklearn.linear_model import LinearRegression
#     from sklearn.pipeline import Pipeline

#     X = np.load('X_data3.npy')
#     Y = np.load('Y_ratio3.npy')

#     # print X.shape, Y.shape

#     X_no_zone = []
#     Y_no_zone = []
#     zones = []
#     for x, y in zip(X, Y):
#         if not x[0] in zones:
#             X_no_zone.append(x[2:len(x)])
#             zones.append(x[0])
#             Y_no_zone.append(y)


#     # print 'X_no_zone:', np.array(X_no_zone).shape
#     # print 'Y_no_zone:', np.array(Y_no_zone).shape


#     clf = Pipeline([('poly', PolynomialFeatures(degree=2)),
#                     ('linear', LinearRegression(fit_intercept=False))])
#     # fit to an order-3 polynomial data
#     model = clf.fit(X_no_zone, Y_no_zone)
#     # print(len(X_no_zone[0]), X_no_zone[0])

    
#     """
#     threshold = 0.1
#     miss_less_than_threshold = 0
#     summation = 0

#     for i, x in enumerate(X_no_zone):
#         # print 'zone:', zones[i]
#         pred = model.predict([x])
#         summation += pow(Y_no_zone[i] - pred, 2)
#         if abs(Y_no_zone[i] - pred) <= threshold:
#             miss_less_than_threshold += 1
#             print 'true:', "{0:.3f}".format(float(Y_no_zone[i])), '\tpredict:', "{0:.3f}".format(float(pred)), '***'
#         else:
#             print 'true:', "{0:.3f}".format(float(Y_no_zone[i])), '\tpredict:',  "{0:.3f}".format(float(pred))
#             pass

#     print 'Miss less than threshold:', miss_less_than_threshold
#     print 'RMSE:', summation/len(Y_no_zone)
#     """

#     # print(len(list(data)), [list(data)])
#     # print('{"result":', model.predict(list(data)), '}')
#     print('{"result":', model.predict([list(data)]), '}')








# #usr/bin/python2.7
# # -*- coding: utf-8 -*-

# import psycopg2
# import numpy as np

# # import cgitb
# # cgitb.enable()

# # import cgi
# # form = cgi.FieldStorage()

# ###variable from front-end###
# # lng = form.getvalue('lat')
# # lat = form.getvalue('lng')
# #############################

# lat = 29.652
# lng = -82.295185

# # print "Content-Type: text/html"     
# # print "Access-Control-Allow-Origin: *"  
# # print


# def get_zone(point):
#     sql = """SELECT ogc_fid
#                 FROM public.neighborhoods
#                 WHERE ST_Within(ST_GeomFromText('""" + point + """', 4432), ST_GeomFromWKB(wkb_geometry, 4432));"""
#     cur.execute(sql)

#     fetch = cur.fetchone()
#     if fetch and len(fetch) > 0:
#         return fetch[0]
#     else:
#          return 'no_zone'

# # Connecting to database
# conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='1234'")

# # get zone
# cur = conn.cursor()
# point = 'POINT(' + str(lng) + ' ' + str(lat) + ')'
# zone = get_zone(point)
# # print 'zone:', zone

# # get zone data from 'zones' table, 
# #   check if all data are not zero -> get data
# #   if all data are zero -> find another zone ex. 86 or use another business type
# sql = """SELECT *
#             FROM public.zones
#             WHERE ogc_fid = '""" + str(zone) + """';"""
# cur.execute(sql)
# fetch = cur.fetchone()
# data = None
# if fetch and len(fetch) > 0:
#     if all(v == 0 for v in fetch[4:]):
#         print('{"result": "fail", "msg": "zero data"}')
#     else:
#         data = fetch[2:]
# else:
#     print('{"result": "fail", "msg": "no zone"}')

# if data:
#     ## calculate probability
#     import numpy as np
#     from sklearn.preprocessing import PolynomialFeatures
#     import random
#     from sklearn.linear_model import LinearRegression
#     from sklearn.pipeline import Pipeline

#     X = np.load('X_data3.npy')
#     Y = np.load('Y_ratio3.npy')

#     # print X.shape, Y.shape

#     X_no_zone = []
#     Y_no_zone = []
#     zones = []
#     for x, y in zip(X, Y):
#         if not x[0] in zones:
#             X_no_zone.append(x[2:len(x)])
#             zones.append(x[0])
#             Y_no_zone.append(y)


#     # print 'X_no_zone:', np.array(X_no_zone).shape
#     # print 'Y_no_zone:', np.array(Y_no_zone).shape


#     clf = Pipeline([('poly', PolynomialFeatures(degree=2)),
#                     ('linear', LinearRegression(fit_intercept=False))])
#     # fit to an order-3 polynomial data
#     model = clf.fit(X_no_zone, Y_no_zone)
#     # print(len(X_no_zone[0]), X_no_zone[0])

    
#     """
#     threshold = 0.1
#     miss_less_than_threshold = 0
#     summation = 0

#     for i, x in enumerate(X_no_zone):
#         # print 'zone:', zones[i]
#         pred = model.predict([x])
#         summation += pow(Y_no_zone[i] - pred, 2)
#         if abs(Y_no_zone[i] - pred) <= threshold:
#             miss_less_than_threshold += 1
#             print 'true:', "{0:.3f}".format(float(Y_no_zone[i])), '\tpredict:', "{0:.3f}".format(float(pred)), '***'
#         else:
#             print 'true:', "{0:.3f}".format(float(Y_no_zone[i])), '\tpredict:',  "{0:.3f}".format(float(pred))
#             pass

#     print 'Miss less than threshold:', miss_less_than_threshold
#     print 'RMSE:', summation/len(Y_no_zone)
#     """

#     # print(len(list(data)), [list(data)])
#     # print('{"result":', model.predict(list(data)), '}')
#     print('{"result":', model.predict([list(data)]), '}')