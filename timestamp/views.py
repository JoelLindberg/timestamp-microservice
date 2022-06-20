from django.http import HttpResponse
from datetime import datetime
import json
import time
import re

# Create your views here.

def current_date(request):
  unix_ms = time.time() * 1000
  utc = datetime.utcnow()
  utc = utc.strftime('%a, %d %b %Y %H:%M:%S GMT')
  d = {
    "unix": int(unix_ms),
    "utc": utc
  }
  
  return HttpResponse(json.dumps(d), 
                      content_type='application/json')


def requested_date(request, unix_time):
  epoch_s = unix_time / 1000
  utc = datetime.fromtimestamp(epoch_s)
  d = {
      "unix": unix_time,
      "utc": utc.strftime("%a, %d %b %Y %H:%M:%S GMT")
  }
  
  return HttpResponse(json.dumps(d), content_type='application/json')


def req_date_js(request, iso_time):
  iso_p = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

  r = re.search(iso_p, iso_time)
  if r != None:
    epoch_ms = time.mktime(time.strptime(iso_time, '%Y-%m-%d')) * 1000
    utc = datetime.fromisoformat(iso_time)
    d = {
      "unix": int(epoch_ms),
      "utc": utc.strftime("%a, %d %b %Y %H:%M:%S GMT")
    }
  else:
    d = { "error": "Invalid Date" }
  
  return HttpResponse(json.dumps(d), 
                      content_type='application/json')


def req_date2_js(request, custom_time):
  utc = datetime.strptime(custom_time, '%d %B %Y, %Z')

  epoch_ms = time.mktime(time.strptime(custom_time, '%d %B %Y, %Z')) * 1000
  
  d = {
    "unix": int(epoch_ms),
    "utc": utc.strftime("%a, %d %b %Y %H:%M:%S GMT")
  }
  
  return HttpResponse(json.dumps(d), 
                      content_type='application/json')