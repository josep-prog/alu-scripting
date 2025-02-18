#!/usr/bin/python3
"""Module to fetch and print the top ten hot posts from a subreddit."""
import requests

def top_ten(subreddit):
    """Fetch and print the titles of the top 10 hot posts in a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts[:10]:
            print(post['data']['title'])
    else:
        print(None)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
