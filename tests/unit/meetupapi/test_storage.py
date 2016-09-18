import unittest
from app.meetupapi.storage import Storage


class TestStorage(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.store = Storage(test_mode=True)
        self.urlname = "GDG-BH-TESTE"

    @classmethod
    def tearDownClass(self):
        self.store.flush()

    def test_should_store_group_information(self):
        group = self.__group_information()
        result = self.store.group(group)
        assert result is True

    def test_should_retrieve_group_information(self):
        group = self.__group_information()
        self.store.group(group)

        group = self.store.retrieve_group(self.urlname)
        assert group == str(self.__group_information())

    def test_should_store_events(self):
        events = self.__events_list()
        result = self.store.events(self.urlname, events)
        assert len(result) is 3

    def test_should_retrieve_events_list(self):
        events = self.__events_list()
        self.store.events(self.urlname, events)

        events = self.store.retrieve_events(self.urlname)
        assert type([]) == type(events)
        assert len(events) == len(self.__events_list())

    def __group_information(self):
        filtered_group_information = {"id": 17205732,
                                      "name": "Google Developers Group - Belo Horizonte",
                                      "urlname": self.urlname,
                                      "created": 1411653886000}
        return filtered_group_information

    def __events_list(self):
        event_details = [{"id": "1886874200",
                         "audience": 10,
                         "created": 1416824376000,
                         "utc_offset": -7200000,
                         "duration": 1417125600000},
                         {"id": "1886874211",
                         "audience": 10,
                         "created": 1416824376000,
                         "utc_offset": -7200000,
                         "duration": 1417125600000},
                         {"id": "1886874222",
                         "audience": 10,
                         "created": 1416824376000,
                         "utc_offset": -7200000,
                         "duration": 1417125600000}]
        return [event_details[0], event_details[1], event_details[2]]
