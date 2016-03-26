import unittest
from selenium import webdriver


class TestOpenDashboard(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()

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

#TODO test status code when is ok
#TODO test what happen with 404 error
#TODO test what happen with 503 error
#TODO test content type


if __name__ == '__main__':
    unittest.main(verbosity=1)
