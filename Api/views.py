from django.contrib.auth import logout
from django.shortcuts import render
from rest_framework import generics, authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Api.models import Location
from Api.serializers import LocationSerializer


class LocalizationListView(APIView):

    #serializer_class=LocationSerializer
    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (IsAuthenticated,)


    def get(self, request, format=None):
        locations=[LocationSerializer(location).data for location in Location.objects.all() if location.user.username==request.user.username]
        return Response((locations))

    #def get_queryset(self):
       # user=self.request.user
      #  return Location.objects.filter(user=user)



