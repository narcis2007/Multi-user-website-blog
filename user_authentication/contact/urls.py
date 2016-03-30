__author__ = 'narcis'
from django.conf.urls import include, url
from . import views
urlpatterns=[
    url(r'^$',views.addContactMessage),
    url(r'^messages/$',views.all_contacts),
]