from django.conf.urls import patterns, url
from testApp import views

urlpatterns = patterns(
    'testApp.views',
    url(r'^$', views.index, name='index'),
    url(r'^something/$', views.something, name = 'something'),
    url(r'^anything/$', views.anything, name = 'anything'),
    url(r'^identify/$', views.identify_examinee, name = 'identify_examinee'),
    url(r'^test/(?P<online_test_id>[0-9]+)/$', views.load_test, name = 'test'),
)
