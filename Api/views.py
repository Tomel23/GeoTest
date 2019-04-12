from django.shortcuts import render
from rest_framework import generics

from Api.models import Location
from Api.serializers import LocationSerializer


class LocalizationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class=LocationSerializer

