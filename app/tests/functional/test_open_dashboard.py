import unittest
from selenium import webdriver


class TestOpenDashboard(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_if_page_loads(self):
        self.browser.get('http://localhost:5000/')
        title = self.browser.title
        self.assertIn('Community Dashboard', title)

    def test_if_loads_dashboard(self):
        self.browser.get('http://localhost:5000/')
        urlname_field = self.browser.find_element_by_id('urlname')
        urlname_field.send_keys('GDG-BH')

        go_button = self.browser.find_element_by_id('go')
        go_button.click()

        community_name = self.browser.find_element_by_id('community_name')
        self.assertIn('GDG Belo Horizonte', community_name.text)

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main(verbosity=1)
