from app.meetupapi.connection import MeetupAPI
from fixtures import MeetupApiFixtures
from vcr_unittest import VCRTestCase


class TestMeetupAPI(VCRTestCase):

    def test_should_get_group_information(self):
        meetup = MeetupAPI()
        received_group = meetup.get_group('GDG-BH')

        fields_received_group = sorted(received_group.keys())
        fields = sorted(MeetupApiFixtures.group_by_urlname().keys())

        for field_fixture, fields_received_group in zip(fields, fields_received_group):
            self.assertEqual(field_fixture, fields_received_group)
