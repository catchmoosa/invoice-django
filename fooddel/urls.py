from django.urls import path, re_path
from . import views



urlpatterns = [
    re_path('^$', views.index, name = 'fooddel.index'),
    path('result/', views.result, name = 'fooddel.result')
]