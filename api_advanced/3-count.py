#!/usr/bin/python3
"""
module for the Reddit API
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively count keywords in titles of hot Reddit posts."""

    if counts is None:
        counts = {}

        for word in word_list:
            word = word.lower()
            counts[word] = counts.get(word, 0) + 1

        word_list = [word.lower() for word in word_list]

    headers = {'User-agent': 'test'}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    params = {
        'limit': 100
    }

    if after:
        params['after'] = after

    res = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if res.status_code != 200:
        return

    try:
        data = res.json()['data']
    except Exception:
        return

    posts = data['children']

    for post in posts:
        title = post['data']['title'].lower().split()

        for word in counts:
            matches = title.count(word)

            if matches:
                duplicate_count = word_list.count(word)
                counts[word] += matches * duplicate_count

    after = data['after']

    if after:
        return count_words(
            subreddit,
            word_list,
            after,
            counts
        )

    result = []

    for word in counts:
        duplicate_count = word_list.count(word)

        original_value = duplicate_count

        actual_count = counts[word] - original_value

        if actual_count > 0:
            result.append((word, actual_count))

    result.sort(key=lambda item: (-item[1], item[0]))

    for word, count in result:
        print("{}: {}".format(word, count))
