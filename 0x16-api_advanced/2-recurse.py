#!/usr/bin/python3
"""
return a list containing all titles of hot articles for a given subreddit
"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    if no results, function returns none
    """
    import requests

    subs = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        params={"count": count, "after": after},
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)

    if subs.status_code >= 400:
        return None

    list = hot_list + [
        child.get("data").get("title")
        for child in subs.json().get("data").get("children")
        ]

    hot = subs.json()
    if not hot.get("data").get("after"):
        return list

    return recurse(
        subreddit, list,
        hot.get("data").get("count"),
        hot.get("data").get("after"))
