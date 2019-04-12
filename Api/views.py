from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from Api.models import Location
from Api.serializers import LocationSerializer


class LocalizationListView(generics.ListAPIView):
    serializer_class=LocationSerializer

    def get_queryset(self):
        user=self.request.user
        return Location.objects.filter(user=user)



