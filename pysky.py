#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib
from os import environ
from sys import exit, argv
import matplotlib.pyplot as plt


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

# Hourly intensity information for plot.
intensity = [x['intensity'] for x in weather['hourPrecipitation']]
time = [(x['time'] - weather['hourPrecipitation'][0]['time'])/60 \
	   for x in weather['hourPrecipitation']]

# Plot dashed lines at intensity ranges.
plt.hlines(15, 0, 59, colors='black', linestyles='dashed')
plt.hlines(30, 0, 59, colors='black', linestyles='dashed')
plt.hlines(45, 0, 59, colors='black', linestyles='dashed')


# Plot the values.
plt.fill_between(time, intensity, color='#ffff00', alpha = .8, linewidth=2)
plt.axis([0, 59, 0, 60], frameon = True)
plt.xticks([10, 20, 30, 40, 50])
plt.yticks([7.5, 22.5, 37.5, 52.5], ['sporadic', 'light', 'moderate', 'heavy'],\
	rotation=90)
plt.tick_params('y', length=0)
plt.xlabel('Minutes from now')

# Save out to a png image.
plt.savefig('/Volumes/MacHD/Projects/darksky-scripts/ds-rain-1.png', dpi=220, \
	transparent=True, bbox_inches='tight')

 