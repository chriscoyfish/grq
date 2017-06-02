"""Scorer module for GRQ."""
import gflags

FLAGS = gflags.FLAGS

gflags.DEFINE_integer(
    'min_tweet_length', 10,
    'Minimum number of characters to consider useful for scoring. Default 10.'
)

gflags.DEFINE_string(
    'neg_file', 'data/negatives.txt',
    'File containing corpus of positive sentiment words.'
)

gflags.DEFINE_string(
    'pos_file', 'data/positives.txt',
    'File containing corpus of positive sentiment words.'
)


class StatusScorer(object):
    """A simple scoring class to "score" a tweet's sentiment."""

    def __init__(self, pos_corpus=None, neg_corpus=None, min_tweet_length=None):
        self._pos = pos_corpus or self._load_corpus_from_file(
            pos_corpus or FLAGS.pos_file)
        self._neg = pos_corpus or self._load_corpus_from_file(
            neg_corpus or FLAGS.neg_file)
        self._min_tweet_length = min_tweet_length or FLAGS.min_tweet_length

    def _load_corpus_from_file(self, filepath):
        with open(filepath) as f:
            words = set([line.strip() for line in f.readlines() if line])
        return words

    def score(self, status):
        """Scores Status based on positive/negative sentiment."""
        if len(status.text) < self._min_tweet_length:
            return 0.0
        pos = 0.0
        neg = 0.0
        status_text = status.text.split()
        for word in status_text:
            # Score based on content. To consider partials, iterate through
            # the set.
            if any(w in word.lower() for w in self._pos):
                pos += 1.0
            if any(w in word.lower() for w in self._neg):
                neg += 1.0
        sentiment = (pos - neg) / len(status_text)

        # Here we are using retweets and favorite counts, but there are a number
        # of more features which could be incorporated here. See the docs at:
        # https://python-twitter.readthedocs.io/en/latest/_modules/twitter/models.html#Status

        # Weight based on retweets (1 per)
        sentiment *= 1 + status.retweet_count
        # Weight based on favorite count (1 per)
        sentiment *= 1 + status.favorite_count
        return sentiment
