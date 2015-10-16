from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

urlpatterns = [
    url(regex = '^admin/', view = include(admin.site.urls)),
    url(r'', include('cornerstone.urls')),
]
