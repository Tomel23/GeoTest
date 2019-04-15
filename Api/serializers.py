from rest_framework import serializers

from Api.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'localization', 'elevation']

