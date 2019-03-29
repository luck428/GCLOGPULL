#!/usr/bin/env python3

# read cachecodes from gc_cachelist.txt
# export to logdata.csv
# export to cachedata.csv
# Vrs 09
# create a header file with cachenumber/cachename/chachetype
# 

import unittest
import win_unicode_console
import csv
import sys 
# import unicodecsv as csv

from os import path
import os
import json
import datetime
from pycaching.log import Log, Type
from pycaching.errors import ValueError as PycachingValueError
from pycaching.cache import Cache, Type, Size, Waypoint
from pycaching.errors import ValueError as PycachingValueError, LoadError, PMOnlyException
from pycaching.geo import Point
from pycaching.geocaching import Geocaching
from pycaching.log import Log, Type as LogType
from pycaching.util import parse_date

import pycaching
import pycaching.errors


# prepare timestamp for copying output files to backup
timestamp = '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now())
targetlogdata = 'logdata'+timestamp+'.csv'
targetcachedata = 'cachedata'+timestamp+'.csv'

# file name declarations
cachelist_file = "gc_cachelist.txt"
# "logdata.csv"
if path.isfile("logdata.csv"):
  print("logdata.csv exists, creating copy", targetlogdata)
  os.rename('logdata.csv', targetlogdata)
# cachedata.csv
if path.isfile("cachedata.csv"):
  print("cachedata.csv exists, creating copy ", targetcachedata)
  os.rename('cachedata.csv', targetcachedata)

try:
     geocaching = pycaching.login()
except pycaching.errors.LoginFailedException as inst:
     print('Login Failed:',inst)
     sys.exit()     

except Exception as inst:
     print(inst)              # __str__ allows args to be printed directly
     print('exit')
     sys.exit()
except:
     sys.exit()  

# read file with Geocache codes if it exists


if path.isfile(cachelist_file):
  print("Loading Caches from gc_cachelist.txt")
else:
  print("gc_cachelist.txt not found. No Caches to pull the logs.")
  sys.exit()  

# contains only the GC codes as one column

try:
    with open(cachelist_file, newline='') as my_file:
        array = my_file.read().splitlines()
except pycaching.errors.ValueError as inst:
     print(inst)
     sys.exit() 


# check if file names are <> zero. eg empty lines or empty
# CR/LF at the end

cache_list = []

for row in array:
    try:
        cache_list.append(geocaching.get_cache(row))
    except Exception as inst:
         print(inst)
         sys.exit() 

for cache in cache_list:
    try:
        cache.load_quick()   # takes a small while
        print (cache.name, cache.wp)
    except Exception as inst:
         print(inst)
         sys.exit() 
#----------------------------------------------------------
# no unicode is written to CSV, but printed in console

print("writing logs to logdata.csv")

with open("logdata.csv", "w",newline="", encoding="utf-8") as file1:
	writes = csv.writer(file1, delimiter=';', quoting=csv.QUOTE_ALL)
	writes.writerow(['GCCODE', 'LogDate', 'Logtype', 'LogAuthor'])
	for cache in cache_list:
		for log in cache.load_logbook(limit=2000):
			writes.writerow( (cache.wp, log.visited, log.type, log.author) )

# using write with ab causes followong error
# TypeError: 'str' does not support the buffer interface

print("writing cache information to cachedata.csv")
with open("cachedata.csv", "w",newline="", encoding="utf-8") as file1:
	writes = csv.writer(file1, delimiter=';', quoting=csv.QUOTE_ALL)
	writes.writerow(['GCCODE', 'cachetype', 'Cachename', 'Difficulty', 'Terrain' ])
	for cache in cache_list:
		writes.writerow( (cache.wp, cache.type, cache.name, cache.difficulty, cache.terrain ) )

geocaching.logout()
