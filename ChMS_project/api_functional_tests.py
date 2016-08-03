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
        response = requests.get(
            self.api['interests'], auth=('demo', 'demodemo'))
        self.assertTrue(response.status_code, 200)

    def test_update_interest(self):
        response = requests.get(self.api['interests'])
        self.assertTrue(response.status_code, 200)
        interests = response.json()
        for interest in interests:
            current_interest = interest
            pprint.pprint('Updating Interest: ' + interest['name'])
            current_interest['name'] = 'Test Interests' + \
                str(int(interest['id']) + 1)
            put_response = requests.put(
                interest['links']['self'], data=current_interest)
            self.assertTrue(put_response.status_code, 200)
            put_response_json = put_response.json()
            self.assertTrue(put_response_json[
                            'name'], current_interest['name'])
            pprint.pprint('to : ' + put_response_json['name'])

    def test_delete_interest(self):
        response = requests.get(self.api['interests'])
        self.assertTrue(response.status_code, 200)
        interests = response.json()
        for interest in interests:
            pprint.pprint('Deleting Interest: ' + interest['name'])
            del_response = requests.delete(interest['links']['self'])
            self.assertTrue(del_response.status_code, 204)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
