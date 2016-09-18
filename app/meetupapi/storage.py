import os
import redis


class Storage:

    def __init__(self, test_mode=False):
        self.redis = redis.from_url(os.environ.get("REDIS_URL"))

        #TODO create a configuration file to test environment
        if test_mode:
            self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)

    def group(self, group_information):
        result = self.redis.set("meetup:GROUP:{0}".format(group_information['urlname']), group_information)
        return result

    def retrieve_group(self, urlname):
        result = self.redis.get("meetup:GROUP:{0}".format(urlname))
        return result

    def events(self, urlname, events_list):
        pipeline = self.redis.pipeline()

        for event in events_list:
            pipeline.hset("meetup:EVENTS:{0}:{1}".format(urlname, event['id']), "id", event)
        result = pipeline.execute()

        return result

    def retrieve_events(self, urlname):
        result = []
        for event in self.redis.scan_iter("meetup:EVENTS:{0}:*".format(urlname)):
            event_details = self.redis.hgetall(event)
            result.append(event_details)

        return result

    def flush(self):
        return self.redis.flushall()
