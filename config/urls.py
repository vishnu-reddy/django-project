from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(regex='^admin/', view=include(admin.site.urls)),
    url(r'', include('cornerstone.urls'))
]
