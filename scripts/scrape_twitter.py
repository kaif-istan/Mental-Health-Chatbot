import os
import tweepy
import json
from dotenv import load_dotenv

# Load token from .env
load_dotenv()
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

# Initialize client
client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

# Define search query (recent 7 days only)
query = "(depression OR anxiety OR burnout OR FOMO) lang:en -is:retweet"

# Setup pagination: max 100 total tweets
tweets = tweepy.Paginator(
    client.search_recent_tweets,
    query=query,
    tweet_fields=["id", "text", "created_at", "author_id", "lang"],
    max_results=100  # Max per request
).flatten(limit=100)  # Total tweets limit

# Collect tweets
data = []
for tweet in tweets:
    data.append({
        "id": tweet.id,
        "text": tweet.text,
        "created_at": str(tweet.created_at),
        "author_id": tweet.author_id
    })

# Create output directory if needed
os.makedirs("data", exist_ok=True)

# Save to JSON file with timestamped name
output_path = "data/twitter_data_batch1.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Scraped {len(data)} tweets and saved to {output_path}")
