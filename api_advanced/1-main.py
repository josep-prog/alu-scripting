#!/usr/bin/python3
"""
1-main
"""
import sys

def main():
    """
    Main function to test the top_ten function.
    """
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
        sys.exit(1)  # Exit with a non-zero status to indicate an error

    try:
        top_ten = __import__('1-top_ten').top_ten
        top_ten(sys.argv[1])
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)  # Exit with a non-zero status to indicate an error

if __name__ == '__main__':
    main()
