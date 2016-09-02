import unittest
from app import app
import flask


class TestApplication(unittest.TestCase):

    def setUp(self):
        self.webapp = app.test_client()
        self.home = self.webapp.get('/')
        self.urlname = 'GDG-BH'
        self.dashboard = self.webapp.get('/dashboard/?urlname=' + self.urlname)

    def test_home_successful_access(self):
        assert 200 == self.home.status_code

    def test_home_content_type(self):
        assert 'text/html' in self.home.content_type

    def test_home_content(self):
        page = self.home.data
        assert '<title>Community Dashboard</title>' in page

    def test_dashboard_successful_access(self):
        assert 200 == self.dashboard.status_code

    def test_dashboard_content_type(self):
        assert 'text/html' in self.dashboard.content_type

    def test_dashboard_content(self):
        page = self.dashboard.data
        assert '<h1 id="community-name">' + self.urlname + '</h1>' in page
        assert '<div class="graphic" id="no-show-chart"></div>' in page
        assert '<div class="graphic" id="diversity-chart"></div>' in page
        assert '<div class="graphic" id="newest-older-attendees-chart"></div>' in page
        assert '<div class="graphic" id="topics-chart"></div>' in page

    def test_page_not_found(self):
        page_not_found = self.webapp.get("/test")
        assert 404 == page_not_found.status_code

    def test_should_receive_urlname_from_index_page(self):
        with app.test_request_context('/dashboard/?urlname=' + self.urlname):
            assert flask.request.args['urlname'] == self.urlname
