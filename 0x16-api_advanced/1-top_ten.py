#!/usr/bin/python3
"""
reddit api that prints the title of the first 10 hot posts listed for a given subreddit
"""


def top_ten(subreddit):
    """
    return top ten hosts
    """
    import requests
    subs = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format
        (subreddit),
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)
    if subs.status_code >=300:
        print("None")
    else:
        [print(d.get("data").get("title"))
        for d in subs.json().get("data").get("children")]
