#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests
import sys

def number_of_subscribers(subreddit):
    """ Queries to Reddit API """

    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    header = {'User-Agent': 'CustomClient/1.0'}
    req = requests.get(url, headers=header, allow_redirects=False)
    if req.status-code != 200:
        return (0)
    req = req.json()
    if "data" in req:
        return (req.get("data").get("subscribers"))
    else:
        return (0)
