from app.meetupapi.data_retrieve import MeetUpAPI
from app.meetupapi.filter import Filter
import unittest
import vcr
import config


class TestFilter(unittest.TestCase):

    my_vcr = vcr.VCR(cassette_library_dir=config.TEST_DIR + '/unit/fixtures/cassettes/',
                     record_mode='once',
                     filter_headers=['authorization'],
                     filter_query_parameters=['key'])

    def setUp(self):
        self.urlname = 'GDG-BH'
        self.meetup = MeetUpAPI()
        self.filter = Filter()

    @my_vcr.use_cassette()
    def test_should_give_id_name_number_of_members(self):
        group_data = self.meetup.group(self.urlname)
        group_info = self.filter.group_basic_info(group_data)
        assert group_info['id'] == 17205732
        assert group_info['name'] == 'Google Developers Group - Belo Horizonte'
        assert group_info['members'] == 1556
        assert len(group_info.keys()) == 3

    @my_vcr.use_cassette()
    def test_should_give_list_of_events(self):
        events_data = self.meetup.events(self.urlname)
        events_info = self.filter.events(events_data)
        assert len(events_info) == 57
