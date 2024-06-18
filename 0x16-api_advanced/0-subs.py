#!/usr/bin/python3
"""module to querry a Reddit API."""
from requests import get


def number_of_subscribers(subreddit):
    """queries the Reddit API
    returns the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    results = get(
        url,
        headers=headers,
        allow_redirects=False
    )
    if results.status_code == 200:
        return results.json()['data']['subscribers']
    return 0
