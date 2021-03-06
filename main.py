import datetime
import pickle
import redis

import environment as Env
import playlist as Playlist
import scrapper as Scrapper
import tooter as Tooter


url = Env.redis_url
r = redis.from_url(url=url, db=0)


def main():
    today = datetime.date.today()

    results = Scrapper.getTracks()
    titles = Playlist.clean(results)
    formatted_titles = Playlist.format(titles)

    known_titles = []
    if r.exists("playlist"):
        known_titles = list(map(
            pickle.loads,
            r.lrange("playlist", 0, -1),
        ))

    unknown_titles = list(filter(
        lambda title: title not in known_titles,
        formatted_titles
    ))

    for title in unknown_titles:
        r.lpush("playlist", pickle.dumps(title))

        message = "{} ({}/{})\n{}\n{}".format(
            title["time"],
            today.day,
            today.month,
            title["artist_album"],
            title["track_title"]
        )
        Tooter.toot(message)

    r.ltrim("playlist", 0, 49)


if __name__ == "__main__":
    main()
