from django.test import TestCase


class ApiTest(TestCase):

    def test_bad_subtract(self):
        self.assertEqual(1 - 1, 10)
