#!/usr/bin/python3
"""
Module: 1-top_ten.py

Fetches and prints the top 10 hot post titles from a given subreddit 
using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Fetch and print the top 10 hot post titles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None: Prints the titles of the posts or 'None' if subreddit is invalid.
    """
    reddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(reddit_url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get("data", {})
            posts = data.get("children", [])

            if posts:
                for post in posts[:10]:
                    print(post.get("data", {}).get("title", "Unknown Title"))
            else:
                print(None)  # Empty subreddit case
        else:
            print(None)  # Subreddit does not exist or restricted

    except requests.exceptions.RequestException:
        print(None)  # Handle request errors
