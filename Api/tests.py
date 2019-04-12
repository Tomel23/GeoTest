from django.test import TestCase
from .models import Location
from django.contrib.gis.geos import Point

class LocationTest(TestCase):

    def setUp(self):
        Location.objects.create(name='loc1',elevation=120.0,localization=Point(15.82031249779768,7.449624259166628))

    def test_name_content(self):
        location=Location.objects.get(id=1)
        expected_object_name=f'{location.name}'
        self.assertEqual(expected_object_name,'loc1')