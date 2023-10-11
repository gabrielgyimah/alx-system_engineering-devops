#!/usr/bin/python3
"""Recursive Reddit API Hot Artciles Module"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit
    If no results are found for the given subreddit,
    the function should return None.
    """

    limit = 100
    url = f"https://www.reddit.com/r/{subreddit}/top.json?limit={limit}"

    if after:
        url += f"&after={after}"

    response = requests.get(
        url,
        headers={'User-Agent': 'Mozilla/5.0'},
        allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        after = data["data"]["after"]

        for post in posts:
            hot_list.append(post['data']['title'])

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
