from django.test import TestCase
from .models import Country, City, Place


class TestCountry(TestCase):

    def setUp(self):
        self.country = Country.objects.create(name='France')

    def tearDown(self):
        self.country.delete()

    def test_create(self):
        self.assertEqual(self.country.name, 'France')

    def test_str(self):
        self.assertEqual(str(self.country), 'France')


class TestCity(TestCase):

    def setUp(self):
        self.country = Country.objects.create(name='France')
        self.city = City(name='Paris', country=self.country)

    def tearDown(self):
        self.country.delete()

    def test_name(self):
        self.assertEqual(self.city.name, 'Paris')

    def test_description(self):
        self.assertEqual(self.city.description, '')


class TestPlace(TestCase):

    def setUp(self):
        country = Country.objects.create(name='France')
        self.city = City.objects.create(name='Paris', country=country)
        self.place = Place.objects.create(name='main_area')
        self.place.cities.add(self.city)

    def tearDown(self):
        self.place.delete()
        self.city.delete()

    def test_cities_count(self):
        self.assertEqual(self.place.cities_count(), 1)

    def test_name(self):
        self.assertEqual(self.place.name, 'main_area')

    def test_description(self):
        self.assertEqual(self.place.description, '')

    def test_rate(self):
        self.assertEqual(self.place.rate, 0.0)

    def test_image(self):
        self.assertEqual(self.place.img, None)

