from django.urls import path, re_path

from . import views

re_unix_time = '^/(?P<unix_time>[0-9]{13}$)' # 1451001600000
re_js_date1 = '^/(?P<iso_time>[0-9]{4}-[0-9]{2}-[0-9]{2}$)' # 2016-12-25
re_js_date2 = '^/(?P<custom_time>[0-9]{2} [\w]+ [0-9]{4}, GMT$)' # "05 October 2011, GMT"

urlpatterns = [
  re_path('^/$|^$', views.time_now, name='time_now'),
  re_path(re_unix_time, views.unix_time, name='unix_time'),
  re_path(re_js_date1, views.js_date1, name='js_date1'),
  re_path(re_js_date2, views.js_date2, name='js_date2'),
  path('/<slug:slug>', views.invalid_datetime, name='invalid_datetime'),
]