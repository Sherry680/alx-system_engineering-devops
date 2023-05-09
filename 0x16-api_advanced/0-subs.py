#!/usr/bin/python3
"""
Reddit api that returns number of subscribers
"""


def number_of_subscribers(subreddit):
    '''
    return number of subscribers
    '''
    import requests
    subs = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False
        )
    if subs.status_code >= 300:
        return 0
    return subs.json().get("data").get("subscribers")
