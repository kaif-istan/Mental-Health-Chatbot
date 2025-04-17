import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from config.env_loader import load_env
import praw
import json
from datetime import datetime


# Load environment variables
env = load_env()

# Setup Reddit API client
reddit = praw.Reddit(
    client_id=env["REDDIT_CLIENT_ID"],
    client_secret=env["REDDIT_CLIENT_SECRET"],
    user_agent=env["REDDIT_USER_AGENT"]
)

# Subreddits to scrape
subreddits = ["depression", "Anxiety", "FOMO", "mentalhealth"]
limit_per_sub = 100
data = []

# Create output path if it doesn't exist
output_dir = os.path.join(os.path.dirname(__file__), "..", "raw_data", "reddit")
output_dir = os.path.abspath(output_dir)
os.makedirs(output_dir, exist_ok=True)


# Scrape top posts
for sub in subreddits:
    for post in reddit.subreddit(sub).top(limit=limit_per_sub):
        entry = {
            "text": post.title + " " + post.selftext,
            "source": "Reddit",
            "timestamp": datetime.utcfromtimestamp(post.created_utc).isoformat(),
            "user_id": hash(post.author.name) if post.author else "anonymous",
            "subreddit": sub
        }
        data.append(entry)

# Save to JSON file
output_dir = os.path.join("..", "raw_data", "youtube")  # safer, cross-platform
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, "youtube_comments.json")

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_comments, f, indent=2, ensure_ascii=False)

print(f"✅ Collected {len(all_comments)} comments. Saved to {output_file}")

