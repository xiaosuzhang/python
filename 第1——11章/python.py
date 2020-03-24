# coding=utf-8

from city_funcction import city_country
import unittest

class CityTestCase(unittest.TestCase):
    
    def test_city_country(self):
        beijng_china = city_country("Beijing","China")
        self.assertEqual(beijng_china,"Beijing,China")
    
    
    def test_city_country_population(self):
        beijng_china = city_country("Beijing","China",population=50000000)
        self.assertEqual(beijng_china,"Beijing,China - population 50000000")
        

unittest.main()