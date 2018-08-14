# MeuhOnAir: from RadioMeuh to Twitter

Make a [Mastodon](https://mastodon.social/about) stream from RadioMeuh's playlist.


## Dev Setup

#### Using Docker

```bash
# build the docker image
docker build -t radiomeuh .

# start a redis database
docker run --name meuh-redis -p 6380:6380 -d redis:alpine

# run the script
docker run --rm -it \
  --name meuh-script \
  --link meuh-redis:redis \
  -v $(pwd):/app \
  -w /app \
  -e ACCESS_TOKEN=<MASTODON ACCESS TOKEN> \
  -e REDIS_URL=meuh-redis \
  -u $(id -u):$(id -g) \
  radiomeuh \
  python main.py

# run the tests
docker run --rm -it \
  -v $(pwd):/app \
  -w /app \
  -u $(id -u):$(id -g) \
  radiomeuh \
  python -m unittest tests/test_*.py
```

#### TODO

  * Correct the `scripts/` module imports. It is currently **BROKEN**.
