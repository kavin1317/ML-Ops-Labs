# test_unittest.py

import unittest
from temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius
)

class TestTemperatureConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0)
        self.assertEqual(fahrenheit_to_celsius(212), 100)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(celsius_to_kelvin(0), 273.15)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0)

if __name__ == "__main__":
    unittest.main()
