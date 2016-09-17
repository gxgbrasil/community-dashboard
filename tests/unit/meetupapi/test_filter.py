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
        assert group_info['created'] == 1411653886000
        assert len(group_info.keys()) == 3

    @my_vcr.use_cassette()
    def test_should_give_list_of_events(self):
        events_data = self.meetup.events(self.urlname)
        events_info = self.filter.events(events_data)
        first_event = events_info[0]

        assert len(events_info) == 57
        assert first_event['id'] == '218868742'
        assert first_event['audience'] == 10
        assert first_event['created'] == 1416824376000
        assert first_event['utc_offset'] == -7200000
        assert first_event['duration'] == 1417125600000

    @my_vcr.use_cassette()
    def test_should_receive_attendance_status_from_rsvps(self):
        event_id = '218868742'
        rsvps_data = self.meetup.rsvps(self.urlname, event_id)
        rsvps_list = self.filter.rsvps(rsvps_data)

        assert len(rsvps_list) == 8

    @my_vcr.use_cassette()
    def test_should_receive_attendance_status_from_rsvps_without_no_response(self):
        event_id = '221804615'
        rsvps_data = self.meetup.rsvps(self.urlname, event_id)
        rsvps_list = self.filter.rsvps(rsvps_data)

        assert len(rsvps_list) == 23
