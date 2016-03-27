import unittest
from app.meetupapi.connection import MeetupAPI
from syntaxsugar import SyntaxSugar


class TestMeetupAPI(unittest.TestCase):

    def test_get_group_information(self):
        meetup = MeetupAPI()
        group_info = meetup.get_group('GDG-BH')
        self.assertEquals(SyntaxSugar.group_by_urlname().keys(), group_info.keys())
