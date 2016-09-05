import os
import redis


class Storage:

    def __init__(self):
        self.redis = redis.from_url(os.environ.get("REDIS_URL"))
