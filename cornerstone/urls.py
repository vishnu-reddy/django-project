from django.conf.urls import include, url,patterns
import views

urlpatterns=[
    url(r'^$', views.cornerstone_profiles_list, name = 'cornerstone_profiles_list')
]