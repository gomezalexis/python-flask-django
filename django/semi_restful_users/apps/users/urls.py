from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='my_index'),
    url(r'^new/', views.new, name='my_new'),
    url(r'^(?P<id>\d+)/$', views.show, name='my_show'),
    url(r'^(?P<id>\d+)/edit/$', views.edit, name='my_edit'),
    url(r'^create/', views.create),
    url(r'^(?P<id>\d+)/update/$', views.update),
    url(r'^(?P<id>\d+)/delete/$', views.delete),

]