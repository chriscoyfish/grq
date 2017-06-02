# GRQ: Gutsy Retweet Querier

Author:
- Chris Coykendall (chriscoyfish@gmail.com)

## Overview

This is a basic tool to analyze user sentiment/popularity for a given topic from
Twitter and score the topic popularity using a crude, simple counter method in
straightforward Python. The higher the score, the better.

## Considerations

Given a particular symbol, determine overall sentiment/popularity score based
upon the following features:

* The # of tweets on Twitter mentioning target
* For every tweet mentioning target, calculate score using...
    - Number of followers
    - Number of retweets
    - Length of tweet
    - Count of positive sentiment words
    - Count of negative sentiment words
    - Etc...

This is by no means a perfect algorithm for scoring social media posts, but is
meant to be a playful exercise in data mining.

Unit tests to follow...

## Installation

1. Download the necessary files

```python

git clone http://<here>
cd grq
pip install -r requirements.txt

```

2. Modify *config.cfg* with the API keys/credential flags associated with your 
Twitter API project. See https://apps.twitter.com/ for more details.

3. Run the tool

```python

python main.py <keyword>

```

