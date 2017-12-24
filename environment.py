import os


python_env          = os.environ.get("PYTHON_ENV") or "development"

access_token        = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
consumer_key        = os.environ.get("CONSUMER_KEY")
consumer_secret     = os.environ.get("CONSUMER_SECRET")


if (access_token == None
      or access_token_secret == None
      or consumer_key == None
      or consumer_secret == None):
    message = \
"""Do not forget to set the following environment variables:
  * `ACCESS_TOKEN`
  * `ACCESS_TOKEN_SECRET`
  * `CONSUMER_KEY`
  * `CONSUMER_SECRET`
"""
    raise EnvironmentError(message)
