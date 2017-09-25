from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='my_index'),
    url(r'^add_course/', views.add_course),
    url(r'^(?P<id>\d+)/description/$', views.show_desc), 
    url(r'^destroy/(?P<id>\d+)/$', views.destroy),
    url(r'^(?P<id>\d+)/delete/$', views.delete),
]