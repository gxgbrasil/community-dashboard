import unittest
import mock
from app import app


class TestApplication(unittest.TestCase):

    def setUp(self):
        self.webapp = app.test_client()
        self.home = self.webapp.get('/')
        self.dashboard = self.webapp.get('/dashboard')

    def test_home_successful_access(self):
        self.assertEqual(200, self.home.status_code)

    def test_home_content_type(self):
        self.assertIn('text/html', self.home.content_type)

    def test_home_content(self):
        page = self.home.data
        self.assertIn('<title>Community Dashboard</title>', page)
        self.assertIn('<input type="text" id="urlname" placeholder="urlname">', page)
        self.assertIn('<a class="ui huge button" href="dashboard">', page)

    def test_dashboard_successful_access(self):
        self.assertEqual(200, self.dashboard.status_code)

    def test_dashboard_content_type(self):
        self.assertIn('text/html', self.dashboard.content_type)

    def test_dashboard_content(self):
        page = self.dashboard.data
        self.assertIn('<h1 id="community-name">GDG Belo Horizonte</h1>', page)
        self.assertIn('<div class="graphic" id="no-show-chart"></div>', page)
        self.assertIn('<div class="graphic" id="diversity-chart"></div>', page)
        self.assertIn('<div class="graphic" id="newest-older-attendees-chart"></div>', page)
        self.assertIn('<div class="graphic" id="topics-chart"></div>', page)

    def test_page_not_found(self):
        page_not_found = self.webapp.get("/test")
        self.assertEqual(404, page_not_found.status_code)

    @mock.patch("app.app.test_client")
    def test_error_on_application(self, mock_app):
        mock_app.get("/test").status_code.return_value = 503
        mock_app.assert_called_with()

    def test_should_return_page_with_group_info(self):
        group_info_page = self.webapp.get('/group')
        page = group_info_page.data
        self.assertEqual(200, group_info_page.status_code)
        self.assertIn('{\n  "name": "Google Developer Group - Belo Horizonte"\n}', page)
