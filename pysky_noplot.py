#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib
from os import environ
from sys import exit, argv


# If desired, enter lat & long as arguments
try:
  lat = argv[1]
  lon = argv[2]
except IndexError:
  lat = 39.200932
  lon = -84.376009

# Get my API key and construct the URL
try:
  with open(environ['HOME'] + '/.darksky') as rcfile:
    for line in rcfile:
      k, v = line.split(':')
      if k.strip() == 'APIkey':
        APIkey = v.strip()
    dsURL = 'https://api.darkskyapp.com/v1/forecast/%s/%s,%s' \
    	    % (APIkey, lat, lon)
except (IOError, NameError):
  print "Failed to get API key"
  exit()

# Get the data from Dark Sky.
try:
  jsonString = urllib.urlopen(dsURL).read()
  weather = json.loads(jsonString)
except (IOError, ValueError):
  print "Connection failure to %s" % dsURL
  exit()

print 'NOW\n' +  str(weather['currentSummary']).capitalize() + ', '\
	  + str(weather['currentTemp']) + u'° F'.encode('utf8') + '\n'
print 'NEXT HOUR \n' + weather['hourSummary'].capitalize() + '\n'

# Highest intensity in the next 3 hours.
hrsType = [ i['type'] for i in weather['dayPrecipitation'][1:4] ]
hrsProb = [ i['probability'] for i in weather['dayPrecipitation'][1:4] ]

chance = max(hrsProb)
probIndex = hrsProb.index(chance)

if chance > 0.8:
  nextThreeHrs = '%s' % (str(hrsType[probIndex])).capitalize()
elif chance > 0.5:
  nextThreeHrs = '%s likely' % (str(hrsType[probIndex])).capitalize()
elif chance > 0.2:
  nextThreeHrs = 'Possible %s' % str(hrsType[probIndex])
else:
  nextThreeHrs = 'No rain'

print  'FOLLOWING 3 HRS\n' + nextThreeHrs.capitalize() + '\n'
print 'NEXT 24 HRS \n' + weather['daySummary'].capitalize() + '\n'


 