# test unittest

import unittest
from city_functions import get_city_country


class TESTCITYCOUNTRY(unittest.TestCase):
    def test_city_country(self):
        result = get_city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')

    def test_city_country_population(self):
        result = get_city_country('santiago', 'chile', 'population=5000000')
        self.assertEqual(result, 'Santiago, Chile - population 5000000')
