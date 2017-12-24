import pickle, redis

import environment as Environment
import playlist as Playlist
import scrapper as Scrapper
import tweeter as Tweeter


host = Environment.redis_host
r = redis.StrictRedis(host=host, port=6379, db=0)


def main():
    results = Scrapper.getTracks()
    titles = Playlist.clean(results)
    formatted_titles = Playlist.format(titles)

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
        message = "{}\n{}\n{}".format(title["time"],
                                      title["artist_album"],
                                      title["track_title"])
        Tweeter.tweet(message)

    r.ltrim("playlist", 0, 49)


if __name__ == "__main__":
    main()
