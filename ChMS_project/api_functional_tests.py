from selenium import webdriver
import unittest
import requests
import pprint


class InterestAPITest(unittest.TestCase):

    def setUp(self):
        response = requests.get('http://127.0.0.1:8000/api/')
        self.assertTrue(response.status_code, 200)
        self.api = response.json()
        pprint.pprint(self.api)

    def test_interest_resource_found(self):
        self.assertTrue('interests' in self.api)

    def test_add_interest(self, interest='Interest 1'):
        response = requests.post(
            self.api['interests'],
            data={'name': interest},
            auth=('demo', 'demodemo'))
        self.assertTrue(response.status_code, 201)

    def test_get_interest(self):
        response = requests.get(self.api['interests'])
        self.assertTrue(response.status_code, 200)
        interests = response.json()
        pprint.pprint(interests)

    def test_delete_interest(self):
        response = requests.get(self.api['interests'])
        self.assertTrue(response.status_code, 200)
        interests = response.json()
        # do delete here


if __name__ == '__main__':
    unittest.main(warnings='ignore')
