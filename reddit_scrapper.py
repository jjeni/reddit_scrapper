import requests
import base64
import os
from dotenv import load_dotenv


def authenticate_reddit():

    #Authenticate with Reddit API using client credentials from .env file.
    load_dotenv()
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT", "SimpleRedditScript")

    # Encode client credentials in Base64
    auth = f"{client_id}:{client_secret}"
    auth_encoded = base64.b64encode(auth.encode()).decode()
    headers = {
        "User-Agent": user_agent,
        "Authorization": f"Basic {auth_encoded}"
    }
    data = {
        "grant_type": "client_credentials"
    }

    # Send request to get access token
    response = requests.post("https://www.reddit.com/api/v1/access_token", headers=headers, data=data)

    if response.status_code == 200:
        token = response.json()["access_token"]
        print("✅ Successfully authenticated")
        return token
    else:
        print(f"❌ Authentication failed: {response.text}")
        return None


def fetch_latest_posts(subreddit_name, token, limit=5):

    #Fetch the latest posts from a given subreddit.
    headers = {
        "User-Agent": "SimpleRedditScript",
        "Authorization": f"bearer {token}"
    }

    # Construct URL for fetching posts
    url = f"https://oauth.reddit.com/r/{subreddit_name}/new?limit={limit}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        posts = response.json()["data"]["children"]
        print(f"\nFetching the latest {limit} posts from r/{subreddit_name}...\n")
        for post in posts:
            data = post["data"]
            print(f"Title: {data['title']}")
            print(f"Author: {data['author']}")
            print(f"Upvotes: {data['score']}\n")
    else:
        print(f"❌ Error fetching posts: {response.text}")


if __name__ == "__main__":
    token = authenticate_reddit()

    if token:
        # Prompt user for subreddit name and fetch posts
        subreddit_name = input("Enter the subreddit name: ")
        fetch_latest_posts(subreddit_name, token)
