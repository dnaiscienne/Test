from django.conf.urls import patterns, url
from testApp import views

urlpatterns = patterns(
    'testApp.views',
    url(r'^$', views.index, name='index'),
    url(r'^something/$', views.something, name = 'something'),
    url(r'^anything/$', views.anything, name = 'anything'),
)
