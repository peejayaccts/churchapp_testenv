from selenium import webdriver
import unittest
import requests
import pprint
import random
import string
import json


def randomword(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


class InterestAPITest(unittest.TestCase):

    added_test_data = []

    def setUp(self):
        response = requests.get('http://127.0.0.1:8000/api/')
        self.assertTrue(response.status_code, 200)
        self.api = response.json()
        # pprint.pprint(self.api)

    def tearDown(self):
        while self.added_test_data:
            response = requests.get(
                self.api['interests'] + str(self.added_test_data.pop()))
            self.assertTrue(response.status_code == 200)
            interest = response.json()
            # pprint.pprint('Deleting Interest: ' + interest['name'])
            del_response = requests.delete(interest['links']['self'])
            self.assertTrue(del_response.status_code == 204)

    def test_interest_resource_found(self):
        self.assertTrue('interests' in self.api)

    def test_add_interest(self, interest=randomword(200)):
        # pprint.pprint('Adding interest: ' + interest)
        response = requests.post(
            self.api['interests'], data={'name': interest})
        self.assertTrue(response.status_code == 201)
        response_json = response.json()
        # pprint.pprint(response_json)
        self.added_test_data.append(response_json['id'])

    def test_add_duplicate(self):
        same_name = randomword(200)
        self.test_add_interest(same_name)
        # pprint.pprint('Duplicate interest: ' + same_name)
        response = requests.post(self.api['interests'],
                                 data={'name': same_name})
        # self.assertFalse(response.status_code, 201)
        self.assertTrue(response.status_code == 400)

    def test_add_256char(self):
        str256 = randomword(256)
        response = requests.post(self.api['interests'], data={'name': str256})
        # self.assertFalse(response.status_code, 201)
        self.assertTrue(response.status_code == 400)

    def test_get_all_interest(self):
        response = requests.get(self.api['interests'])
        self.assertTrue(response.status_code == 200)
        # pprint.pprint('Interest List: ')
        # pprint.pprint(response.json())

    def test_search_interest(self):
        new_interest = randomword(20)
        self.test_add_interest(new_interest)
        response = requests.get(
            self.api['interests'] + '?search=' + new_interest)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(response.json()) == 1)

    def test_sort_asc_name(self):
        new_interest = 'A' * 10
        self.test_add_interest(new_interest)
        another_interest = 'Z' * 10
        self.test_add_interest(another_interest)
        response = requests.get(self.api['interests'] + '?ordering=name')
        interests = response.json()
        latest_interest = ''
        for interest in interests:
            if interest['name'] == new_interest or interest['name'] == another_interest:
                latest_interest = interest['name']
        self.assertTrue(latest_interest == another_interest,
                        "Ascending order not ok")

    def test_sort_desc_name(self):
        new_interest = 'A' * 10
        self.test_add_interest(new_interest)
        another_interest = 'Z' * 10
        self.test_add_interest(another_interest)
        response = requests.get(self.api['interests'] + '?ordering=-name')
        interests = response.json()
        latest_interest = ''
        for interest in interests:
            if interest['name'] == new_interest or interest['name'] == another_interest:
                latest_interest = interest['name']
        self.assertTrue(latest_interest == new_interest,
                        "Descending order not working")

    def test_update_interest(self):
        new_interest = randomword(200)
        self.test_add_interest(new_interest)
        response = requests.get(self.api['interests'])
        self.assertTrue(response.status_code == 200)
        interests = response.json()
        for interest in interests:
            if interest['name'] == new_interest:
                # pprint.pprint('Updating Interest: ' + interest['name'])
                interest['name'] = 'Test: Updated Interest'
                put_response = requests.put(interest['links']['self'],
                                            data=interest)
                self.assertTrue(put_response.status_code == 200)
                put_response_json = put_response.json()
                self.assertTrue(put_response_json['name'] == interest['name'])
                # pprint.pprint('to : ' + put_response_json['name'])

    def test_delete_interest(self):
        self.test_add_interest()
        current_id = self.added_test_data[-1]
        response = requests.get(self.api['interests'] + str(current_id))
        self.assertTrue(response.status_code == 200)
        interest = response.json()
        # pprint.pprint('Deleting Interest: ' + interest['name'])
        del_response = requests.delete(interest['links']['self'])
        self.assertTrue(del_response.status_code == 204)
        self.added_test_data.pop()


class SkillsAndProfessionsAPITest(unittest.TestCase):

    added_test_data = []

    def setUp(self):
        response = requests.get('http://127.0.0.1:8000/api/')
        self.assertTrue(response.status_code, 200)
        self.api = response.json()
        # pprint.pprint(self.api)

    def tearDown(self):
        while self.added_test_data:
            response = requests.get(
                self.api['skills_and_professions'] + str(self.added_test_data.pop()))
            self.assertTrue(response.status_code == 200)
            skill = response.json()
            # pprint.pprint('Deleting Skill: ' + skill['name'])
            del_response = requests.delete(skill['links']['self'])
            self.assertTrue(del_response.status_code == 204)

    def test_skills_resource_found(self):
        self.assertTrue('skills_and_professions' in self.api)

    def test_add_skills(self, skill=randomword(200)):
        # pprint.pprint('Adding skill: ' + skill)
        response = requests.post(
            self.api['skills_and_professions'], data={'name': skill})
        self.assertTrue(response.status_code == 201)
        response_json = response.json()
        # pprint.pprint(response_json)
        self.added_test_data.append(response_json['id'])

    def test_add_duplicate(self):
        same_name = randomword(200)
        self.test_add_skills(same_name)
        # pprint.pprint('Duplicate skill: ' + same_name)
        response = requests.post(self.api['skills_and_professions'],
                                 data={'name': same_name})
        # self.assertFalse(response.status_code, 201)
        self.assertTrue(response.status_code == 400)

    def test_add_256char(self):
        str256 = randomword(256)
        response = requests.post(
            self.api['skills_and_professions'], data={'name': str256})
        # self.assertFalse(response.status_code, 201)
        self.assertTrue(response.status_code == 400)

    def test_get_all_skills(self):
        response = requests.get(self.api['skills_and_professions'])
        self.assertTrue(response.status_code == 200)
        # pprint.pprint('Skill List: ')
        # pprint.pprint(response.json())

    def test_search_skills(self):
        new_skills = randomword(20)
        self.test_add_skills(new_skills)
        response = requests.get(
            self.api['skills_and_professions'] + '?search=' + new_skills)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(response.json()) == 1)

    def test_sort_asc_name(self):
        new_skills = 'A' * 10
        self.test_add_skills(new_skills)
        another_skills = 'Z' * 10
        self.test_add_skills(another_skills)
        response = requests.get(
            self.api['skills_and_professions'] + '?ordering=name')
        skills = response.json()
        latest_skills = ''
        for skill in skills:
            if skill['name'] == new_skills or skill['name'] == another_skills:
                latest_skills = skill['name']
        self.assertTrue(latest_skills == another_skills,
                        "Ascending order not ok")

    def test_sort_desc_name(self):
        new_skills = 'A' * 10
        self.test_add_skills(new_skills)
        another_skills = 'Z' * 10
        self.test_add_skills(another_skills)
        response = requests.get(
            self.api['skills_and_professions'] + '?ordering=-name')
        skills = response.json()
        latest_skills = ''
        for skill in skills:
            if skill['name'] == new_skills or skill['name'] == another_skills:
                latest_skills = skill['name']
        self.assertTrue(latest_skills == new_skills,
                        "Descending order not working")

    def test_update_skills(self):
        new_skills = randomword(200)
        self.test_add_skills(new_skills)
        response = requests.get(self.api['skills_and_professions'])
        self.assertTrue(response.status_code == 200)
        skills = response.json()
        for skill in skills:
            if skill['name'] == new_skills:
                # pprint.pprint('Updating Skill: ' + skill['name'])
                skill['name'] = 'Test: Updated Skill'
                put_response = requests.put(skill['links']['self'],
                                            data=skill)
                self.assertTrue(put_response.status_code == 200)
                put_response_json = put_response.json()
                self.assertTrue(put_response_json['name'] == skill['name'])
                # pprint.pprint('to : ' + put_response_json['name'])

    def test_delete_skills(self):
        self.test_add_skills()
        current_id = self.added_test_data[-1]
        response = requests.get(
            self.api['skills_and_professions'] + str(current_id))
        self.assertTrue(response.status_code == 200)
        skill = response.json()
        # pprint.pprint('Deleting Skill: ' + skill['name'])
        del_response = requests.delete(skill['links']['self'])
        self.assertTrue(del_response.status_code == 204)
        self.added_test_data.pop()


class SpiritualMilestonesAPITest(unittest.TestCase):

    added_test_data = []

    def setUp(self):
        response = requests.get('http://127.0.0.1:8000/api/')
        self.assertTrue(response.status_code, 200)
        self.api = response.json()

    def tearDown(self):
        while self.added_test_data:
            response = requests.get(
                self.api['spiritual_milestones'] + str(self.added_test_data.pop()))
            self.assertTrue(response.status_code == 200)
            spiritual_milestone = response.json()
            del_response = requests.delete(
                spiritual_milestone['links']['self'])
            self.assertTrue(del_response.status_code == 204)

    def test_spiritual_milestone_resource_found(self):
        self.assertTrue('spiritual_milestones' in self.api)

    def test_add_spiritual_milestone(self, spiritual_milestone=randomword(200)):
        response = requests.post(
            self.api['spiritual_milestones'], data={'name': spiritual_milestone})
        self.assertTrue(response.status_code == 201)
        response_json = response.json()
        self.added_test_data.append(response_json['id'])

    def test_add_duplicate(self):
        same_name = randomword(200)
        self.test_add_spiritual_milestone(same_name)
        response = requests.post(self.api['spiritual_milestones'],
                                 data={'name': same_name})
        self.assertTrue(response.status_code == 400)

    def test_add_256char(self):
        str256 = randomword(256)
        response = requests.post(
            self.api['spiritual_milestones'], data={'name': str256})
        self.assertTrue(response.status_code == 400)

    def test_get_all_spiritual_milestone(self):
        response = requests.get(self.api['spiritual_milestones'])
        self.assertTrue(response.status_code == 200)

    def test_search_spiritual_milestone(self):
        new_spiritual_milestone = randomword(20)
        self.test_add_spiritual_milestone(new_spiritual_milestone)
        response = requests.get(
            self.api['spiritual_milestones'] + '?search=' + new_spiritual_milestone)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(response.json()) == 1)

    def test_sort_asc_name(self):
        new_spiritual_milestone = 'A' * 10
        self.test_add_spiritual_milestone(new_spiritual_milestone)
        another_spiritual_milestone = 'Z' * 10
        self.test_add_spiritual_milestone(another_spiritual_milestone)
        response = requests.get(
            self.api['spiritual_milestones'] + '?ordering=name')
        spiritual_milestones = response.json()
        latest_spiritual_milestone = ''
        for spiritual_milestone in spiritual_milestones:
            if spiritual_milestone['name'] == new_spiritual_milestone or \
               spiritual_milestone['name'] == another_spiritual_milestone:
                latest_spiritual_milestone = spiritual_milestone['name']
        self.assertTrue(latest_spiritual_milestone == another_spiritual_milestone,
                        "Ascending order not ok")

    def test_sort_desc_name(self):
        new_spiritual_milestone = 'A' * 10
        self.test_add_spiritual_milestone(new_spiritual_milestone)
        another_spiritual_milestone = 'Z' * 10
        self.test_add_spiritual_milestone(another_spiritual_milestone)
        response = requests.get(
            self.api['spiritual_milestones'] + '?ordering=-name')
        spiritual_milestones = response.json()
        latest_spiritual_milestone = ''
        for spiritual_milestone in spiritual_milestones:
            if spiritual_milestone['name'] == new_spiritual_milestone or \
               spiritual_milestone['name'] == another_spiritual_milestone:
                latest_spiritual_milestone = spiritual_milestone['name']
        self.assertTrue(latest_spiritual_milestone == new_spiritual_milestone,
                        "Descending order not working")

    def test_update_spiritual_milestone(self):
        new_spiritual_milestone = randomword(200)
        self.test_add_spiritual_milestone(new_spiritual_milestone)
        response = requests.get(self.api['spiritual_milestones'])
        self.assertTrue(response.status_code == 200)
        spiritual_milestones = response.json()
        for spiritual_milestone in spiritual_milestones:
            if spiritual_milestone['name'] == new_spiritual_milestone:
                spiritual_milestone[
                    'name'] = 'Test: Updated Spiritual_Milestone'
                put_response = requests.put(spiritual_milestone['links']['self'],
                                            data=spiritual_milestone)
                self.assertTrue(put_response.status_code == 200)
                put_response_json = put_response.json()
                self.assertTrue(put_response_json[
                                'name'] == spiritual_milestone['name'])

    def test_delete_spiritual_milestone(self):
        self.test_add_spiritual_milestone()
        current_id = self.added_test_data[-1]
        response = requests.get(
            self.api['spiritual_milestones'] + str(current_id))
        self.assertTrue(response.status_code == 200)
        spiritual_milestone = response.json()
        del_response = requests.delete(spiritual_milestone['links']['self'])
        self.assertTrue(del_response.status_code == 204)
        self.added_test_data.pop()


class MinistriesAPITest(unittest.TestCase):

    added_test_data = []

    def setUp(self):
        response = requests.get('http://127.0.0.1:8000/api/')
        self.assertTrue(response.status_code, 200)
        self.api = response.json()

    def tearDown(self):
        while self.added_test_data:
            response = requests.get(
                self.api['ministries'] + str(self.added_test_data.pop()))
            self.assertTrue(response.status_code == 200)
            ministry = response.json()
            del_response = requests.delete(
                ministry['links']['self'])
            self.assertTrue(del_response.status_code == 204)

    def test_ministry_resource_found(self):
        self.assertTrue('ministries' in self.api)

    def test_add_ministry(self, ministry=randomword(200)):
        response = requests.post(
            self.api['ministries'], data={'name': ministry})
        self.assertTrue(response.status_code == 201)
        response_json = response.json()
        self.added_test_data.append(response_json['id'])

    def test_add_duplicate(self):
        same_name = randomword(200)
        self.test_add_ministry(same_name)
        response = requests.post(self.api['ministries'],
                                 data={'name': same_name})
        self.assertTrue(response.status_code == 400)

    def test_add_256char(self):
        str256 = randomword(256)
        response = requests.post(
            self.api['ministries'], data={'name': str256})
        self.assertTrue(response.status_code == 400)

    def test_get_all_ministry(self):
        response = requests.get(self.api['ministries'])
        self.assertTrue(response.status_code == 200)

    def test_search_ministry(self):
        new_ministry = randomword(20)
        self.test_add_ministry(new_ministry)
        response = requests.get(
            self.api['ministries'] + '?search=' + new_ministry)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(response.json()) == 1)

    def test_sort_asc_name(self):
        new_ministry = 'A' * 10
        self.test_add_ministry(new_ministry)
        another_ministry = 'Z' * 10
        self.test_add_ministry(another_ministry)
        response = requests.get(
            self.api['ministries'] + '?ordering=name')
        ministries = response.json()
        latest_ministry = ''
        for ministry in ministries:
            if ministry['name'] == new_ministry or \
               ministry['name'] == another_ministry:
                latest_ministry = ministry['name']
        self.assertTrue(latest_ministry == another_ministry,
                        "Ascending order not ok")

    def test_sort_desc_name(self):
        new_ministry = 'A' * 10
        self.test_add_ministry(new_ministry)
        another_ministry = 'Z' * 10
        self.test_add_ministry(another_ministry)
        response = requests.get(
            self.api['ministries'] + '?ordering=-name')
        ministries = response.json()
        latest_ministry = ''
        for ministry in ministries:
            if ministry['name'] == new_ministry or \
               ministry['name'] == another_ministry:
                latest_ministry = ministry['name']
        self.assertTrue(latest_ministry == new_ministry,
                        "Descending order not working")

    def test_update_ministry(self):
        new_ministry = randomword(200)
        self.test_add_ministry(new_ministry)
        response = requests.get(self.api['ministries'])
        self.assertTrue(response.status_code == 200)
        ministries = response.json()
        for ministry in ministries:
            if ministry['name'] == new_ministry:
                ministry[
                    'name'] = 'Test: Updated Ministry'
                put_response = requests.put(ministry['links']['self'],
                                            data=ministry)
                self.assertTrue(put_response.status_code == 200)
                put_response_json = put_response.json()
                self.assertTrue(put_response_json[
                                'name'] == ministry['name'])

    def test_delete_ministry(self):
        self.test_add_ministry()
        current_id = self.added_test_data[-1]
        response = requests.get(
            self.api['ministries'] + str(current_id))
        self.assertTrue(response.status_code == 200)
        ministry = response.json()
        del_response = requests.delete(ministry['links']['self'])
        self.assertTrue(del_response.status_code == 204)
        self.added_test_data.pop()


class MemberStatusesAPITest(unittest.TestCase):

    added_test_data = []

    def setUp(self):
        response = requests.get('http://127.0.0.1:8000/api/')
        self.assertTrue(response.status_code, 200)
        self.api = response.json()

    def tearDown(self):
        while self.added_test_data:
            response = requests.get(
                self.api['member_statuses'] + str(self.added_test_data.pop()))
            self.assertTrue(response.status_code == 200)
            member_status = response.json()
            del_response = requests.delete(
                member_status['links']['self'])
            self.assertTrue(del_response.status_code == 204)

    def test_member_status_resource_found(self):
        self.assertTrue('member_statuses' in self.api)

    def test_add_member_status(self, member_status=randomword(200)):
        response = requests.post(
            self.api['member_statuses'], data={'name': member_status})
        self.assertTrue(response.status_code == 201)
        response_json = response.json()
        self.added_test_data.append(response_json['id'])

    def test_add_duplicate(self):
        same_name = randomword(200)
        self.test_add_member_status(same_name)
        response = requests.post(self.api['member_statuses'],
                                 data={'name': same_name})
        self.assertTrue(response.status_code == 400)

    def test_add_256char(self):
        str256 = randomword(256)
        response = requests.post(
            self.api['member_statuses'], data={'name': str256})
        self.assertTrue(response.status_code == 400)

    def test_get_all_member_status(self):
        response = requests.get(self.api['member_statuses'])
        self.assertTrue(response.status_code == 200)

    def test_search_member_status(self):
        new_member_status = randomword(20)
        self.test_add_member_status(new_member_status)
        response = requests.get(
            self.api['member_statuses'] + '?search=' + new_member_status)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(response.json()) == 1)

    def test_sort_asc_name(self):
        new_member_status = 'A' * 10
        self.test_add_member_status(new_member_status)
        another_member_status = 'Z' * 10
        self.test_add_member_status(another_member_status)
        response = requests.get(
            self.api['member_statuses'] + '?ordering=name')
        member_statuses = response.json()
        latest_member_status = ''
        for member_status in member_statuses:
            if member_status['name'] == new_member_status or \
               member_status['name'] == another_member_status:
                latest_member_status = member_status['name']
        self.assertTrue(latest_member_status == another_member_status,
                        "Ascending order not ok")

    def test_sort_desc_name(self):
        new_member_status = 'A' * 10
        self.test_add_member_status(new_member_status)
        another_member_status = 'Z' * 10
        self.test_add_member_status(another_member_status)
        response = requests.get(
            self.api['member_statuses'] + '?ordering=-name')
        member_statuses = response.json()
        latest_member_status = ''
        for member_status in member_statuses:
            if member_status['name'] == new_member_status or \
               member_status['name'] == another_member_status:
                latest_member_status = member_status['name']
        self.assertTrue(latest_member_status == new_member_status,
                        "Descending order not working")

    def test_update_member_status(self):
        new_member_status = randomword(200)
        self.test_add_member_status(new_member_status)
        response = requests.get(self.api['member_statuses'])
        self.assertTrue(response.status_code == 200)
        member_statuses = response.json()
        for member_status in member_statuses:
            if member_status['name'] == new_member_status:
                member_status[
                    'name'] = 'Test: Updated Member_Status'
                put_response = requests.put(member_status['links']['self'],
                                            data=member_status)
                self.assertTrue(put_response.status_code == 200)
                put_response_json = put_response.json()
                self.assertTrue(put_response_json[
                                'name'] == member_status['name'])

    def test_delete_member_status(self):
        self.test_add_member_status()
        current_id = self.added_test_data[-1]
        response = requests.get(
            self.api['member_statuses'] + str(current_id))
        self.assertTrue(response.status_code == 200)
        member_status = response.json()
        del_response = requests.delete(member_status['links']['self'])
        self.assertTrue(del_response.status_code == 204)
        self.added_test_data.pop()


class ChurchAPITest(unittest.TestCase):

    added_test_data = []

    def setUp(self):
        response = requests.get('http://127.0.0.1:8000/api/')
        self.assertTrue(response.status_code, 200)
        self.api = response.json()
        # pprint.pprint(self.api)

    def tearDown(self):
        while self.added_test_data:
            response = requests.get(
                self.api['churches'] + str(self.added_test_data.pop()))
            self.assertTrue(response.status_code == 200)
            interest = response.json()
            # pprint.pprint('Deleting Interest: ' + interest['name'])
            del_response = requests.delete(interest['links']['self'])
            self.assertTrue(del_response.status_code == 204)

    def test_church_resource_found(self):
        self.assertTrue('churches' in self.api)

    def test_add_church(self, church=randomword(200)):
        input_data = {
            'name': church,
            'vision': randomword(200),
            'logo': randomword(200),
            'banner': randomword(200),
            'regional_info': None
        }
        headers = {'X-Requested-With': 'Python requests',
                   'Content-type': 'application/json'}
        response = requests.post(
            self.api['churches'], data=json.dumps(input_data), headers=headers)
        response_json = response.json()
        # pprint.pprint(response_json)
        self.assertTrue(response.status_code == 201)
        self.added_test_data.append(response_json['id'])

    def test_add_duplicate(self):
        same_name = randomword(200)
        self.test_add_church(same_name)
        input_data = {
            'name': same_name,
            'vision': randomword(200),
            'logo': randomword(200),
            'banner': randomword(200),
            'regional_info': None,
        }
        headers = {'X-Requested-With': 'Python requests',
                   'Content-type': 'application/json'}
        response = requests.post(
            self.api['churches'], data=json.dumps(input_data), headers=headers)
        if(response.status_code != 400):
            response_json = response.json()
            self.added_test_data.append(response_json['id'])
        self.assertTrue(response.status_code == 400,
                        'Must not allow duplicate church names')

    def test_add_main_church(self):
        input_data = {
            'name': randomword(200),
            'church_type': 'M',
            'vision': randomword(200),
            'logo': randomword(200),
            'banner': randomword(200),
            'regional_info': None,
        }
        headers = {'X-Requested-With': 'Python requests',
                   'Content-type': 'application/json'}
        response = requests.post(
            self.api['churches'], data=json.dumps(input_data), headers=headers)
        if(response.status_code != 400):
            response_json = response.json()
            self.added_test_data.append(response_json['id'])
        self.assertTrue(response.status_code == 400,
                        'Must not allow adding main churches')

    def test_add_256char(self):
        str256 = randomword(256)
        input_data = {
            'name': str256,
            'vision': randomword(200),
            'logo': randomword(200),
            'banner': randomword(200),
            'regional_info': None,
        }
        headers = {'X-Requested-With': 'Python requests',
                   'Content-type': 'application/json'}
        response = requests.post(
            self.api['churches'], data=json.dumps(input_data), headers=headers)
        if(response.status_code != 400):
            response_json = response.json()
            self.added_test_data.append(response_json['id'])
        self.assertTrue(response.status_code == 400,
                        'Must not allow church name exceeding 255.')

    def test_get_all_church(self):
        response = requests.get(self.api['churches'])
        self.assertTrue(response.status_code == 200)

    def test_search_church(self):
        new_church = randomword(20)
        self.test_add_church(new_church)
        response = requests.get(
            self.api['churches'] + '?search=' + new_church)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(response.json()) == 1)

    def test_update_basic_info_church(self):
        new_church = randomword(200)
        self.test_add_church(new_church)
        response = requests.get(self.api['churches'])
        self.assertTrue(response.status_code == 200)
        churches = response.json()
        for church in churches:
            if church['name'] == new_church:
                church['name'] = 'Test: Updated Church Name'
                church['vision'] = 'Test: Updated Vision'
                church['logo'] = 'Test: Logo'
                church['banner'] = 'Test: Banner'
                headers = {'X-Requested-With': 'Python requests',
                           'Content-type': 'application/json'}
                put_response = requests.put(church['links']['self'],
                                            data=json.dumps(church),
                                            headers=headers)
                put_response_json = put_response.json()
                self.assertTrue(put_response.status_code == 200)
                self.assertTrue(put_response_json['name'] == church['name'])
                self.assertTrue(put_response_json[
                                'vision'] == church['vision'])
                self.assertTrue(put_response_json['logo'] == church['logo'])
                self.assertTrue(put_response_json[
                                'banner'] == church['banner'])

    def test_delete_church(self):
        self.test_add_church()
        current_id = self.added_test_data[-1]
        response = requests.get(
            self.api['churches'] + str(current_id))
        self.assertTrue(response.status_code == 200)
        church = response.json()
        del_response = requests.delete(church['links']['self'])
        self.assertTrue(del_response.status_code == 204)
        self.added_test_data.pop()

    def test_sort_asc_name(self):
        new_church = 'A' * 10
        self.test_add_church(new_church)
        another_church = 'Z' * 10
        self.test_add_church(another_church)
        response = requests.get(
            self.api['churches'] + '?ordering=name')
        churches = response.json()
        latest_church = ''
        for church in churches:
            if church['name'] == new_church or \
               church['name'] == another_church:
                latest_church = church['name']
        self.assertTrue(latest_church == another_church,
                        "Ascending order not ok")

    def test_sort_desc_name(self):
        new_church = 'A' * 10
        self.test_add_church(new_church)
        another_church = 'Z' * 10
        self.test_add_church(another_church)
        response = requests.get(
            self.api['churches'] + '?ordering=-name')
        churches = response.json()
        latest_church = ''
        for church in churches:
            if church['name'] == new_church or \
               church['name'] == another_church:
                latest_church = church['name']
        self.assertTrue(latest_church == new_church,
                        "Descending order not working")

    def test_link_regional_info_link(self):
        new_church = randomword(20)
        self.test_add_church(new_church)
        response = requests.get(self.api['churches'] + '?search=' + new_church)
        self.assertTrue(response.status_code == 200)
        churches = response.json()
        for church in churches:
            self.assertTrue('regional_info' in church)

    def test_add_update_region_info_church(self):
        new_church = randomword(200)
        self.test_add_church(new_church)
        response = requests.get(self.api['churches'])
        self.assertTrue(response.status_code == 200)
        churches = response.json()
        for church in churches:
            if church['name'] == new_church:
                # ADD : With null regional info
                regional_info = {
                    'date_format': 'date_format',
                    'timezone': 'timezone',
                    'language': 'language',
                    'kanguage': 'language',
                    'country': 'country',
                    'state_province': 'province_info',
                    'city': 'city',
                    'zip_post_code': 999
                }
                church['regional_info'] = regional_info
                headers = {'X-Requested-With': 'Python requests',
                           'Content-type': 'application/json'}
                put_response = requests.put(church['links']['self'],
                                            data=json.dumps(church),
                                            headers=headers)
                put_response_json = put_response.json()
                self.assertTrue(put_response.status_code ==
                                200, put_response.status_code)
                self.assertTrue(put_response_json['regional_info'][
                                'date_format'] == 'date_format')

                # UPDATE : With existing regional info
                regional_info['date_format'] = 'date_format_updated'
                church['regional_info'] = regional_info
                headers = {'X-Requested-With': 'Python requests',
                           'Content-type': 'application/json'}
                put_response = requests.put(church['links']['self'],
                                            data=json.dumps(church),
                                            headers=headers)
                put_response_json = put_response.json()
                self.assertTrue(put_response.status_code ==
                                200, put_response.status_code)
                self.assertTrue(put_response_json['regional_info'][
                                'date_format'] == 'date_format_updated')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
