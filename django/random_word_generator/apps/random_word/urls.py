from django.conf.urls import url
from . import views  # import *

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reset/', views.reset)
]