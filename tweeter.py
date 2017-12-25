import tweepy

import environment as Env


def tweet(message):
    if Env.python_env != "production":
        print("Tweet sent: \n" + message)
    else:
        auth = tweepy.OAuthHandler(Env.consumer_key, Env.consumer_secret)
        auth.set_access_token(Env.access_token, Env.access_token_secret)

        api = tweepy.API(auth)
        api.update_status(message)
