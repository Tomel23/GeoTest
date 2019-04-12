from django.test import TestCase

from Api.serializers import LocationSerializer
from .models import Location
from django.contrib.gis.geos import Point


class LocationTest(TestCase):

    def setUp(self):
        self.location_attributes={
            'name': 'loc1',
            'elevation': 120.0,
            'localization': Point(15.82031249779768, 7.449624259166628)
        }

        self.location_serializer_data = {
            'name': 'loc2',
            'localization': Point(25.82031249779768, 17.449624259166628),
            'elevation': 950.0,
        }

        self.location_object=Location.objects.create(**self.location_attributes)
        self.serializer = LocationSerializer(instance=self.location_object)

    def test_name_content(self):

        #location = Location.objects.get(id=1)
        expected_object_name = f'{self.location_object.name}'
        self.assertEqual(expected_object_name, 'loc1')

    def test_contains_expected_field_names(self):
        serializer_data = self.serializer.data
        self.assertEqual(set(serializer_data.keys()), set(['name', 'localization', 'elevation']))
