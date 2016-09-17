import requests
import os


class MeetUpAPI:

    BASE_URL = "https://api.meetup.com/"

    def __init__(self):
        self.key = os.environ['MEETUPAPIKEY']

    def group(self, urlname):
        params = {"page": 500}
        url = self.url_compose(urlname)
        result = self.request(url, params=params)
        return result

    def events(self, urlname):
        params = {"group_urlname": urlname, "page": 500, "status": "past"}
        url = self.url_compose("/2/events/")
        result = self.request(url, params=params)
        return result

    def members(self, urlname):
        params = {"group_urlname": urlname, "page": 500}
        url = self.url_compose("/members/")
        result = self.request(url, params=params)
        return result

    def rsvps(self, urlname, event_id):
        params = {"page": 500}
        url = self.url_compose(urlname + "/events/" + event_id + "/rsvps")
        result = self.request(url, params=params)
        return result

    #TODO implement the pagination
    def request(self, url, params):
        response = requests.get(url, params=params)
        return response.json()

    def url_compose(self, endpoint):
        return self.BASE_URL + endpoint + "?key=" + self.key
