from app.meetupapi.connection import MeetUpAPI
from app.meetupapi.storage import Storage
import unittest
import vcr
import config


class TestCaseMeetUpAPI(unittest.TestCase):

    my_vcr = vcr.VCR(cassette_library_dir=config.TEST_DIR + '/unit/fixtures/cassettes/',
                     record_mode='once',
                     filter_headers=['authorization'],
                     filter_query_parameters=['key'])

    def setUp(self):
        self.urlname = 'GDG-BH'
        self.meetup = MeetUpAPI()
        self.storage = Storage()

    @my_vcr.use_cassette()
    def test_should_store_group_information(self):
        group_information = self.meetup.group(self.urlname)
        response = self.storage.group(group_information)
