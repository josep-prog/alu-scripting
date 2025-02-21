#!/usr/bin/python3
"""
Module: 1-top_ten.py

This module contains a function to fetch and print the titles of the top 10 hot posts 
from a given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Fetch and print the top 10 hot post titles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit to fetch posts from.

    Returns:
        None: Prints the titles of the hot posts or 'None' if an error occurs.
    """
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    HEADERS = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {})

        # Check if 'data' contains 'children' key
        hot_posts = data.get("children", [])
        if not hot_posts:
            print(None)
            return

        # Print post titles
        for post in hot_posts:
            print(post.get("data", {}).get("title", "Unknown Title"))

    except requests.exceptions.RequestException:
        print(None)
