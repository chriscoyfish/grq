#!/usr/bin/python
"""Main module for GRQ (Gutsy Retweet Querier)."""
import sys
from google.apputils import app
import scorer
import twitter_collector


USAGE_MESSAGE = """
%s target1 target2 ...
(See --helpfull for more information)
""" % __file__


class GrqCli(object):
    """CLI executor class for GRQ."""

    def __init__(self, targets):
        self._targets = targets
        self._collector = twitter_collector.TwitterCollector()

    def run(self):
        """Runs the CLI."""
        for target in self._targets:
            sentiment_score = 0.0
            for status in self._collector.find_statuses(target):
                score = scorer.StatusScorer().score(status)
                if abs(score) > 0.0:
                    print '-' * 80
                    print 'Text:\t', status.text
                    print 'RTs:\t', status.retweet_count
                    print 'Faves:\t', status.favorite_count
                    print 'Score:\t', score
                    sentiment_score += score
            print '-' * 80
            print 'Overall:\t', sentiment_score
            print '*' * 80

def main(argv):
    """CLI for GRQ."""
    if len(argv) < 2:
        raise app.UsageError(USAGE_MESSAGE)
    GrqCli(argv[1:]).run()


if __name__ == '__main__':
    if '--flagfile' not in str(sys.argv):
        sys.argv.insert(1, '--flagfile=config.cfg')
    app.run()
