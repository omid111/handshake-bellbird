from django.conf.urls import url

from alarms import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^alarm/$', views.AlarmView.as_view(), name='alarm'),
    url(r'^list/$', views.AlarmsListView.as_view(), name='alarms_list'),
    url(r'^alarm/(?P<pk>[0-9]+)/upvote/$', views.UpvoteAlarmView.as_view(), name='alarm_upvote'),
    url(r'^api/recent/$', views.RecentAlarmsView.as_view(), name='recent_alarms'),
]
