import praw
import json
from datetime import datetime
import os
from config.env_loader import load_env

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
output_dir = "mental_health_dataset/raw_data/reddit"
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
with open(os.path.join(output_dir, "reddit_posts.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f"[✓] Scraped {len(data)} posts. Saved to {output_dir}/reddit_posts.json")
