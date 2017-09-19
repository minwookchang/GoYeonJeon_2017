from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^$',views.post_list,name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^score_history/$', views.score_history, name='score_history'),
	url(r'^videos/$', views.videos, name='videos'),
	url(r'^cheeringsongs/$', views.cheeringsongs, name='cheeringsongs'),
]