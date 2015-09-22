__author__ = 'narcis'
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^edit/$',views.edit_profile,name='edit_profile'),
    url(r'^(?P<user_id>\d+)/$',views.profile, name='profile'),

]