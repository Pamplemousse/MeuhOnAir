import tweepy
import os
import sys

class Tweeter():
    def __init__(self):
        self._access_token        = os.environ.get("ACCESS_TOKEN")
        self._access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
        self._consumer_key        = os.environ.get("CONSUMER_KEY")
        self._consumer_secret     = os.environ.get("CONSUMER_SECRET")

        # TODO: maybe it's better to raise an exception
        if not self._consumer_key or not self._consumer_secret or \
           not self._access_token or not self._access_token_secret:
            message = \
"""Do not forget to set the following environment variables:
  * `ACCESS_TOKEN`
  * `ACCESS_TOKEN_SECRET`
  * `CONSUMER_KEY`
  * `CONSUMER_SECRET`
"""
            print(message, file=sys.stderr)
            exit()

    def tweet(self, message):
        auth = tweepy.OAuthHandler(self._consumer_key, self._consumer_secret)
        auth.set_access_token(self._access_token, self._access_token_secret)

        api = tweepy.API(auth)
        api.update_status(message)
