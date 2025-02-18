#!/usr/bin/python3
"""
Return the number of subscribers
from any subreddit given
"""
import requests

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Myapi-app'}
    
    try:
        # Make the request, disable redirects to prevent following search results page
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the response code is 200, extract the subscriber count
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        
    except requests.exceptions.RequestException:
        # Handle any network-related errors
        pass

    # If the subreddit is invalid or there is any error, return 0
    return 0
