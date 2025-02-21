#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests

def top_ten(subreddit):
    """Main function"""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    HEADERS = {"User-Agent": "Mozilla/5.0"}  # Updated user-agent

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        
        # Check if subreddit is valid
        if RESPONSE.status_code != 200:
            print(None)
            return

        DATA = RESPONSE.json().get("data", {}).get("children", [])
        if not DATA:
            print(None)
            return

        for post in DATA:
            print(post.get("data", {}).get("title"))

    except requests.exceptions.RequestException:
        print(None)
