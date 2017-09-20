from django.conf.urls import url
from . import views  # import *

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process/', views.process),
    url(r'^result/', views.result),
]