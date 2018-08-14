import os


access_token = os.environ.get("ACCESS_TOKEN")
python_env = os.environ.get("PYTHON_ENV") or "development"
redis_url = os.environ.get("REDIS_URL") or "redis://@meuh-redis:6379"


if (access_token == None):
    message = \
"""Do not forget to set the following environment variables:
  * `ACCESS_TOKEN`
"""
    raise EnvironmentError(message)
