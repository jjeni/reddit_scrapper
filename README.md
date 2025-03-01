Reddit API Fetch Script

📌 Overview

This script interacts with the Reddit API to fetch the latest posts from a given subreddit. It demonstrates API authentication, data fetching, and error handling.

🚀 Features

Authenticates with the Reddit API using OAuth2.

Fetches the 5 latest posts from a user-specified subreddit.

Displays the post title, author, and upvote count.

Implements proper error handling for API failures.

🔧 Requirements

Python 3+

requests

python-dotenv

📂 Setup

Clone this repository or copy the script file.

Install dependencies using:

pip install requests python-dotenv

Create a .env file in the same directory and add your Reddit API credentials:

REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret

🏃‍♂️ Running the Script

Open a terminal and navigate to the script folder.

Run the script:

python reddit_fetch.py

Enter the subreddit name when prompted.

The script will display the latest 5 posts.

⚠️ Notes

Ensure your Reddit API credentials are correct.

Reddit may enforce rate limits; handle repeated requests accordingly.

📜 License

This project is for personal use and learning purposes.

👩‍💻 About Me

Name: Jeni J
LinkedIn: https://www.linkedin.com/in/jeni-j/

Feel free to reach out if you have any questions or suggestions! 🚀

