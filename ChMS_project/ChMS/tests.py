from django.core.urlresolvers import resolve
from django.test import TestCase
from django.test import Client


class AdminPageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        webclient = Client()
        response = webclient.get('/')
        self.assertIn(b'<title>Church Management System</title>',
                      response.content)
