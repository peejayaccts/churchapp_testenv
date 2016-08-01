from selenium import webdriver
import unittest


class AdminTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_RootPageIsFound(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Church Management System', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
