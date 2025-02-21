#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests

def top_ten(subreddit):
    """Main function"""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)

        # Check if request was successful
        if RESPONSE.status_code != 200:
            print(None)
            return

        DATA = RESPONSE.json().get("data")
        if not DATA:
            print(None)
            return

        HOT_POSTS = DATA.get("children", [])

        if not HOT_POSTS:
            print(None)
            return

        for post in HOT_POSTS:
            print(post.get("data", {}).get("title", ""))
    except requests.RequestException:
        print(None)
