import tweepy

import environment as Environment


def tweet(message):
    if Environment.python_env != "production":
        print("Tweet sent: \n" + message)
    else:
        auth = tweepy.OAuthHandler(self._consumer_key, self._consumer_secret)
        auth.set_access_token(self._access_token, self._access_token_secret)

        api = tweepy.API(auth)
        api.update_status(message)
