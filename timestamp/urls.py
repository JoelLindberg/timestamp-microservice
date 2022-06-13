from django.urls import path

from . import views

urlpatterns = [
  path('', views.current_date, name='current_date'),
  path('/', views.current_date, name='current_date'),
  path('/<int:unix_time>', views.requested_date, name='requested_date'),
  path('/<slug:iso_time>', views.req_date_js, name='req_date_js'),
]