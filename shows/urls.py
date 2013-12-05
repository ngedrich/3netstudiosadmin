from django.conf.urls import patterns, url

from shows import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)