import json

import requests
from django.contrib.auth import logout
from django.contrib.gis.geos import Point
from django.db import transaction
from django.shortcuts import render
from rest_framework import generics, authentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.gis.db.models.functions import Distance

from Api.models import Location
from Api.serializers import LocationSerializer


class AllLocalizationListView(APIView):
    # serializer_class=LocationSerializer
    @authentication_classes(BasicAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, format=None):
        locations = [LocationSerializer(location).data for location in Location.objects.all() if
                     location.user.username == request.user.username]


        return Response((locations))

    # def get_queryset(self):
    # user=self.request.user
    #  return Location.objects.filter(user=user)



class ClosestLocationsView(APIView):

    @authentication_classes(BasicAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, lat, lon):
        user = self.request.user
        y = float(lat)
        x = float(lon)
        user_location= Point(x,y,srid=4326)
        location=Location.objects.filter(user=user).annotate(distance=Distance('localization',user_location)).order_by('distance')[0]
        response =LocationSerializer(location).data
        response['distance']=str(location.distance.km)+' km'
        return Response(response)

class FixedDistanceLocationsView(APIView):

    @authentication_classes(BasicAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, lat, lon,dist):
        user = self.request.user
        y = float(lat)
        x = float(lon)
        d=float(dist)
        user_location= Point(x,y,srid=4326)
        location = []
        for l in Location.objects.filter(user=user).annotate(distance=Distance('localization',user_location)):
            if l.distance.km <= d:
                location.append(LocationSerializer(l).data)
                location[-1]['distance']=str(l.distance.km)+' km'

        return Response(location)
class LocationCreateView(APIView):

    @transaction.atomic
    @authentication_classes(BasicAuthentication)
    @permission_classes((IsAuthenticated,))
    def post(self, request, name, lat, lon):

        result = requests.get(
            f'https://elevation-api.io/api/elevation?points=({lat},{lon})')
        if result.status_code == requests.codes.ok:
            elevation = (result.json()['elevations'][0]['elevation'])
        else:
            elevation = 0.0

        y = float(lat)
        x = float(lon)

        Location.objects.create(user=request.user, name=name, elevation=elevation, localization=Point(x, y,srid=4326))

        return Response({'Location created': True})
