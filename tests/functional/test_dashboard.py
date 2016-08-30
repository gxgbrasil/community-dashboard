import unittest
from selenium import webdriver


class TestOpenDashboard(unittest.TestCase):
    URL = 'http://localhost:5000/'

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()

    def test_should_loads_page(self):
        self.browser.get(self.URL)
        title = self.browser.title
        self.assertIn('Community Dashboard', title)

    def test_should_loads_groupname_as_url_on_dashboard(self):
        self.browser.get(self.URL)
        urlname_field = self.browser.find_element_by_id('urlname')
        urlname_field.send_keys('GDG-BH')

        go_button = self.browser.find_element_by_id('go')
        go_button.click()

        self.assertIn('http://localhost:5000/dashboard/gdg-bh', self.browser.current_url)

    def test_should_loads_groupname_on_dashboard(self):
        self.browser.get(self.URL)
        urlname_field = self.browser.find_element_by_id('urlname')
        urlname_field.send_keys('GDG-BH')

        go_button = self.browser.find_element_by_id('go')
        go_button.click()

        community_name = self.browser.find_element_by_id('community_name')
        self.assertIn('GDG Belo Horizonte', community_name.text)

    def test_should_return_page_not_found_when_try_access_inexistent_page(self):
        self.browser.get(self.URL + 'inexistent')
        page_not_found = self.browser.find_element_by_tag_name('h1')
        self.assertIn('Page Not Found', page_not_found.text)

if __name__ == '__main__':
    unittest.main(verbosity=1)
