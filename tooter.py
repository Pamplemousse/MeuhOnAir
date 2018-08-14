from mastodon import Mastodon

import environment as Env


def toot(message):
    if Env.python_env != "production":
        print("Toot sent: \n" + message)
    else:
        Mastodon(
            access_token=Env.access_token,
            api_base_url='https://mamot.fr'
        ).toot(message)
