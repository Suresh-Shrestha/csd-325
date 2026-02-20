


import unittest
from city_functions import format_city_country


class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Test that city and country are formatted correctly."""
        result = format_city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()

