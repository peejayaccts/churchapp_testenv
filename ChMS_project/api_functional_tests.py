from selenium import webdriver
import unittest
import requests
import pprint

added_test_data = []


class InterestAPITest(unittest.TestCase):

    def setUp(self):
        response = requests.get('http://127.0.0.1:8000/api/')
        self.assertTrue(response.status_code, 200)
        self.api = response.json()
        # pprint.pprint(self.api)

    def tearDown(self):
        while added_test_data:
            response = requests.get(
                self.api['interests'] + str(added_test_data.pop()))
            self.assertTrue(response.status_code, 200)
            interest = response.json()
            #pprint.pprint('Deleting Interest: ' + interest['name'])
            del_response = requests.delete(interest['links']['self'])
            self.assertTrue(del_response.status_code, 204)

    def test_interest_resource_found(self):
        self.assertTrue('interests' in self.api)

    def test_add_interest(self, interest='Test: Interest 1'):
        pprint.pprint('Adding interest: ' + interest)
        response = requests.post(
            self.api['interests'], data={'name': interest})
        self.assertTrue(response.status_code, 201)
        response_json = response.json()
        # pprint.pprint(response_json)
        added_test_data.append(response_json['id'])

    def test_add_duplicate(self):
        response = requests.post(self.api['interests'],
                                 data={'name': 'X'})
        self.assertTrue(response.status_code, 201)
        response_json = response.json()
        added_test_data.append(response_json['id'])

        response = requests.post(self.api['interests'],
                                 data={'name': 'X'})
        self.assertFalse(response.status_code, 201)
        self.assertTrue(response.status_code, 400)

    def test_get_interest(self):
        response = requests.get(
            self.api['interests'], auth=('demo', 'demodemo'))
        self.assertTrue(response.status_code, 200)
        pprint.pprint('Interest List: ')
        pprint.pprint(response.json())

    def test_update_interest(self):
        self.test_add_interest('Test: Update Interest')
        response = requests.get(self.api['interests'])
        self.assertTrue(response.status_code, 200)
        interests = response.json()
        for interest in interests:
            if interest['name'] == 'Test: Update Interest':
                pprint.pprint('Updating Interest: ' + interest['name'])
                interest['name'] = 'Test: Updated Interest'
                put_response = requests.put(interest['links']['self'],
                                            data=interest)
                self.assertTrue(put_response.status_code, 200)
                put_response_json = put_response.json()
                self.assertTrue(put_response_json['name'],
                                interest['name'])
                pprint.pprint('to : ' + put_response_json['name'])

    def test_delete_interest(self):
        self.test_add_interest('Test1')
        current_id = added_test_data[-1]
        response = requests.get(self.api['interests'] + str(current_id))
        self.assertTrue(response.status_code, 200)
        interest = response.json()
        pprint.pprint('Deleting Interest: ' + interest['name'])
        del_response = requests.delete(interest['links']['self'])
        self.assertTrue(del_response.status_code, 204)
        added_test_data.pop()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
