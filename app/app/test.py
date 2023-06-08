"""
Sampel tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):

    # prefix test_ is required for test methods
    def test_add_numbers(self):
        """
        Test that two numbers are added together
        docker-compose run --rm app sh -c "python manage.py test"
        """
        res = calc.add(3,8)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """
        Test that values are subtracted
        """
        res = calc.subtract(5,11)
        self.assertEqual(res, -6)