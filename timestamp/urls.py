from django.urls import path

from . import views

urlpatterns = [
  #path('', views.index, name='index'),
  path('<int:unix_time>', views.date, name='date'),
]