from django.contrib.auth.models import User
from django.contrib.gis.db.models.functions import Distance
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from Api.serializers import LocationSerializer
from .models import Location
from django.contrib.gis.geos import Point


class LocationTest(APITestCase):

    def setUp(self):
        user = User.objects.create_user(username='john',
                                        email='jlennon@beatles.com',
                                        password='glass onion')

        self.location_attributes = {
            'user': user,
            'name': 'loc1',
            'elevation': 120.0,
            'localization': Point(15.82031249779768, 7.449624259166628)
        }

        self.location_serializer_data = {
            'name': 'loc2',
            'localization': Point(25.82031249779768, 17.449624259166628),
            'elevation': 950.0,
        }

        self.location_object = Location.objects.create(**self.location_attributes)
        self.serializer = LocationSerializer(instance=self.location_object)

    def test_name_content(self):
        # location = Location.objects.get(id=1)
        expected_object_name = f'{self.location_object.name}'
        self.assertEqual(expected_object_name, 'loc1')

    def test_contains_expected_field_names(self):
        serializer_data = self.serializer.data
        self.assertEqual(set(serializer_data.keys()), set(['name', 'localization', 'elevation']))

    def test_name_field_content(self):
        serializer_data = self.serializer.data
        self.assertEqual(serializer_data['name'], self.location_attributes['name'])

    def test_get_all_locations(self):
        user = User.objects.get(username='john')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get(reverse("Api:location_list"))

        expected = Location.objects.filter(user=user)
        serialized = LocationSerializer(expected, many=True)

        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_fixed_locations(self):
        user = User.objects.get(username='john')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get(reverse("Api:fixed_location_search", kwargs={'lat': 20, 'lon': 10, 'dist': 2000}))

        y = 20.0
        x = 10.0
        d = 2000.0
        user_location = Point(x, y, srid=4326)

        expected = []

        for l in Location.objects.filter(user=user).annotate(distance=Distance('localization', user_location)):
            if l.distance.km <= d:
                expected.append(LocationSerializer(l).data)
                expected[-1]['distance'] = str(l.distance.km) + ' km'


        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
