from django.urls import path

from Api import views

app_name='Api'
urlpatterns=[
    path('locations/',views.LocalizationListView.as_view(),name='location_list')
]