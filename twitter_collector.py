"""Twitter collector module."""
import gflags
import twitter

FLAGS = gflags.FLAGS

gflags.DEFINE_string(
    'access_token_key', None,
    'Twitter API Consumer Key.'
)

gflags.DEFINE_string(
    'access_token_secret', None,
    'Twitter API Consumer Key.'
)

gflags.DEFINE_string(
    'consumer_key', None,
    'Twitter API Consumer Key.'
)

gflags.DEFINE_string(
    'consumer_secret', None,
    'Twitter API Consumer Key.'
)

gflags.DEFINE_integer(
    'max_results', 100,
    'Maximum results to return from Twitter. Defaults to 100 (API max).'
)


class TwitterCollector(object):
    """A simple facade around the python-twitter API to collect data."""

    def __init__(self, consumer_key=None, consumer_secret=None,
                 access_token_key=None, access_token_secret=None,
                 max_results=None):
        self._api = twitter.Api(
            consumer_key=consumer_key or FLAGS.consumer_key,
            consumer_secret=consumer_secret or FLAGS.consumer_secret,
            access_token_key=access_token_key or FLAGS.access_token_key,
            access_token_secret=(
                access_token_secret or FLAGS.access_token_secret))
        self._max_results = max_results or FLAGS.max_results

    def find_statuses(self, target):
        """Returns Status model objects for search target."""
        # Many assumptions made here, could be flagged out. Leaving
        # the None kwargs here for convenience and quick tuning/playing.
        return self._api.GetSearch(
            term=target, raw_query=None, geocode=None, since_id=None,
            max_id=None, until=None, since=None, count=self._max_results,
            lang='en', locale=None, result_type='mixed',
            include_entities=None)

