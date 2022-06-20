from django.http import HttpResponse
from datetime import datetime
import json
import time

# Create your views here.

def time_now(request):
  """Return the current time as unix time and utc in the format
  :'Fri, 25 Dec 2015 00:00:00 GMT'."""
  unix_ms = time.time() * 1000
  utc = datetime.utcnow()
  utc = utc.strftime('%a, %d %b %Y %H:%M:%S GMT')
  
  d = {
    "unix": int(unix_ms),
    "utc": utc
  }
  
  return HttpResponse(json.dumps(d), 
                      content_type='application/json')


def unix_time(request, unix_time):
  """Accept a unix (epoch) timestamp in millseconds.
  :Return the same unix timestamp and an utc time in the format 
  :'Fri, 25 Dec 2015 00:00:00 GMT'."""
  unix_time = int(unix_time)
  epoch_s = unix_time / 1000
  utc = datetime.fromtimestamp(epoch_s)
  
  d = {
      "unix": unix_time,
      "utc": utc.strftime("%a, %d %b %Y %H:%M:%S GMT")
  }
  
  return HttpResponse(json.dumps(d), content_type='application/json')


def js_date1(request, iso_time):
  """Accept time in iso format and return unix time and utc time in the format
  :'Fri, 25 Dec 2015 00:00:00 GMT'.
  :The input time is one of many supported variants for Javascript's new Date()."""
  epoch_ms = time.mktime(time.strptime(iso_time, '%Y-%m-%d')) * 1000
  utc = datetime.fromisoformat(iso_time)
  
  d = {
    "unix": int(epoch_ms),
    "utc": utc.strftime("%a, %d %b %Y %H:%M:%S GMT")
  }
  
  return HttpResponse(json.dumps(d), 
                      content_type='application/json')


def js_date2(request, custom_time):
  """Accept time in a Javascript specific time format and return unix time and utc time in the format
  :'Fri, 25 Dec 2015 00:00:00 GMT'.
  :The input time is one of many supported variants for Javascript's new Date()."""
  utc = datetime.strptime(custom_time, '%d %B %Y, %Z')
  epoch_ms = time.mktime(time.strptime(custom_time, '%d %B %Y, %Z')) * 1000
  
  d = {
    "unix": int(epoch_ms),
    "utc": utc.strftime("%a, %d %b %Y %H:%M:%S GMT")
  }
  
  return HttpResponse(json.dumps(d), 
                      content_type='application/json')


def invalid_datetime(request, slug):
  """Invalid inputs handled"""
  d = { "error": "Invalid Date" }
  
  return HttpResponse(json.dumps(d), 
                      content_type='application/json')