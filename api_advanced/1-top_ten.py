#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Fetch and print the top 10 hot post titles from a subreddit."""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    HEADERS = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)

        # Check if the request was successful
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data")
        
        # Check if data is None
        if not data or "children" not in data:
            print(None)
            return

        hot_posts = data.get("children", [])

        # Print titles if available
        for post in hot_posts:
            print(post.get("data", {}).get("title", "Unknown Title"))

    except requests.exceptions.RequestException:
        print(None)
