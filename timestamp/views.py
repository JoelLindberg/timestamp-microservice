from django.http import HttpResponse
from datetime import datetime
import json
import time

# Create your views here.

def index(request):
  return HttpResponse('Hello!')

def date(request, unix_time):
    epoch_s = unix_time / 1000
    #epoch_ms = time.time() * 1000
    #int(epoch_ms)
    #a = datetime.utcnow()
    #a.strftime("%a, %d %b %Y %H:%M:%S %z")
    b = datetime.fromtimestamp(epoch_s)
    d = {
        "unix": unix_time,
        "utc": b.strftime("%a, %d %b %Y %H:%M:%S GMT")
    }
    return HttpResponse(json.dumps(d), content_type='application/json')