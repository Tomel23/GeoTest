from django.conf.urls import url
from django.urls import path

from Api import views

app_name = 'Api'
urlpatterns = [
    path('', views.AllLocalizationListView.as_view(), name='location_list'),
    url(r'^add/(?P<name>[^/]+)/(?P<lon>-?\d*(.\d+))/(?P<lat>-?\d*(.\d+))/$', views.LocationCreateView.as_view(),
        name='location_create'),
    url(r'^closest_location/(?P<lon>-?\d*(.\d+))/(?P<lat>-?\d*(.\d+))/$', views.ClosestLocationsView.as_view(),
        name='closest_location_search'),
    url(r'^fixed_location/(?P<lon>-?\d*(.\d+))/(?P<lat>-?\d*(.\d+))/(?P<dist>-?\d*(.\d+))/$', views.FixedDistanceLocationsView.as_view(),
        name='fixed_location_search'),

]
