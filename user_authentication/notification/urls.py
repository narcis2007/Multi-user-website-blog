__author__ = 'narcis'
from django.conf.urls import include, url
from . import views
urlpatterns=[
    url(r'^show_all_unviewed/$',views.show_unviewed_notifications),
    url(r'^view/(?P<notification_id>\d+)/$',views.view_notification),

]