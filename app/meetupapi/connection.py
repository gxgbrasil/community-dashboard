import requests
import os


class MeetupAPI:

    def __init__(self):
        self.key = os.environ['MEETUPAPIKEY']

    def get_group(self, urlname):
        url = "https://api.meetup.com/" + urlname + "?key=" + self.key
        response = requests.get(url)
        return response.json()
