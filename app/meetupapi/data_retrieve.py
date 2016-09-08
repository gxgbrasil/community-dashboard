import requests
import os


class MeetUpAPI:

    BASE_URL = "https://api.meetup.com/"

    def __init__(self):
        self.key = os.environ['MEETUPAPIKEY']

    def group(self, urlname):
        params = {"page": 500}
        url = self.url_compose(urlname)
        return self.request(url, params=params)

    def events(self, urlname):
        params = {"group_urlname": urlname, "page": 500, "status": "past"}
        url = self.url_compose("/2/events/")
        return self.request(url, params=params)

    def members(self, urlname):
        params = {"group_urlname": urlname, "page": 500}
        url = self.url_compose("/members/")
        return self.request(url, params=params)

    def rsvps(self, urlname, event_id):
        params = {"group_urlname": urlname, "page": 500}
        url = self.url_compose("/2/events/" + event_id + "/rsvps")
        return self.request(url, params=params)

    #TODO implement the pagination
    def request(self, url, params):
        response = requests.get(url, params=params)
        return response.json()

    def url_compose(self, endpoint):
        return self.BASE_URL + endpoint + "?key=" + self.key
