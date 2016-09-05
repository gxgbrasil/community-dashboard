from app.meetupapi.connection import MeetUpAPI
import unittest
import vcr
import config


class TestCaseMeetUpAPI(unittest.TestCase):

    my_vcr = vcr.VCR(cassette_library_dir=config.TEST_DIR + '/unit/fixtures/cassettes/',
                     record_mode='once',
                     filter_headers=['authorization'],
                     filter_query_parameters=['key'])

    def setUp(self):
        self.meetup = MeetUpAPI()

    @my_vcr.use_cassette()
    def test_should_get_group_information(self):
        received_group = self.meetup.group('GDG-BH')
        fields_received_group = received_group.keys()
        assert 'name' in fields_received_group
