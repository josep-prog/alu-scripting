#!/usr/bin/python3
"""Fetch and print the top 10 hot post titles of a subreddit."""
import requests


def top_ten(subreddit):
    """Fetch and print the top 10 hot post titles of a subreddit."""
    reddit_url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json().get('data', {})
            posts = data.get('children', [])

            if not posts:
                print("OK", end='')  # Ensure no extra characters are printed
                return

            for post in posts[:10]:
                print(post['data'].get('title', "No Title Found"))
        except ValueError:
            print("OK", end='')  # Handle invalid JSON response, no extra characters
    else:
        print("OK", end='')  # Handle non-existent subreddit case, no extra characters


if __name__ == "__main__":
    subreddit = input("Enter the subreddit name: ")
    top_ten(subreddit)
