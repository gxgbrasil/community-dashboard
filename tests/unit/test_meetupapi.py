from app.meetupapi.connection import MeetupAPI
from vcr_unittest import VCRTestCase


class TestMeetupAPI(VCRTestCase):

    #TODO we should not test the api
    def test_should_get_group_information(self):
        meetup = MeetupAPI()
        received_group = meetup.get_group('GDG-BH')

        fields_received_group = received_group.keys()

        assert 'name' in fields_received_group
