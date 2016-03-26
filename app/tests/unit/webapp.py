import unittest
from app import app


class TestHome(unittest.TestCase):

    def setUp(self):
        webapp = app.test_client()
        self.response = webapp.get('/')

    def test_successful_access(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    def test_content(self):
        page = self.response.data
        self.assertIn('<title>Community Dashboard</title>', page)
        self.assertIn('<input type="text" id="urlname" placeholder="urlname">', page)
        self.assertIn('<a class="ui huge button" href="dashboard">', page)


class TestDashboard(unittest.TestCase):

    def setUp(self):
        webapp = app.test_client()
        self.response = webapp.get('/dashboard')

    def test_successful_access(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    def test_content(self):
        page = self.response.data
        self.assertIn('<h1 id="community_name">GDG Belo Horizonte</h1>', page)
        self.assertIn('<div class="graphic" id="no-show-chart"></div>', page)
        self.assertIn('<div class="graphic" id="diversity-chart"></div>', page)
        self.assertIn('<div class="graphic" id="newest-older-attendees-chart"></div>', page)
        self.assertIn('<div class="graphic" id="topics-chart"></div>', page)
