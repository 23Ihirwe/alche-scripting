#!/usr/bin/python3
"""
Queries the Reddit API and prints titles of the first 10 hot posts.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "alche-scripting/1.0"
    }

    response = requests.get(
        url,
        headers=headers,
        params={"limit": 10},
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json()["data"]["children"]
    except (ValueError, KeyError):
        print(None)
        return

    if not posts:
        print(None)
        return

    for post in posts[:10]:
        print(post["data"]["title"])
