#!/usr/bin/python3
"""
Return the number of subscribers from any subreddit given.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Myapi-app/0.1'}  # Custom User-Agent to avoid Too Many Requests error
    
    try:
        # Make the request, disable redirects to prevent following search results page
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the response code is 200, extract the subscriber count
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # If the subreddit is invalid, return 0
            return 0
    
    except requests.exceptions.RequestException as e:
        # Handle any network-related errors
        print(f"An error occurred: {e}")
        return 0

# Example usage
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
