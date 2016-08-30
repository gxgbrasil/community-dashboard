import unittest
from selenium import webdriver


class TestOpenDashboard(unittest.TestCase):
    URL = 'http://localhost:5000/'

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.urlname = 'GDG-BH'

    def tearDown(self):
        self.browser.close()

    def test_should_loads_page(self):
        self.browser.get(self.URL)
        title = self.browser.title
        assert 'Community Dashboard' in title

    def test_should_loads_groupname_as_url_on_dashboard(self):
        self.browser.get(self.URL)
        urlname_field = self.browser.find_element_by_id('urlname')
        urlname_field.send_keys(self.urlname)

        go_button = self.browser.find_element_by_id('go')
        go_button.click()
        assert 'http://localhost:5000/dashboard/?urlname=' + self.urlname in self.browser.current_url

    def test_should_loads_groupname_on_dashboard(self):
        self.browser.get(self.URL)
        urlname_field = self.browser.find_element_by_id('urlname')
        urlname_field.send_keys(self.urlname)

        go_button = self.browser.find_element_by_id('go')
        go_button.click()

        community_name = self.browser.find_element_by_id('community-name')
        assert self.urlname in community_name.text

    def test_should_return_page_not_found_when_try_access_inexistent_page(self):
        self.browser.get(self.URL + 'inexistent')
        page_not_found = self.browser.find_element_by_tag_name('h1')
        assert 'Page Not Found' in page_not_found.text

if __name__ == '__main__':
    unittest.main(verbosity=1)
