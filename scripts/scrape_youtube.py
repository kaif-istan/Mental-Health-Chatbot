import os
import json
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

# Base URLs
SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
COMMENT_URL = "https://www.googleapis.com/youtube/v3/commentThreads"

# Step 1: Search for video IDs related to mental health topics
def search_videos(query, max_results=5):
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": API_KEY
    }
    response = requests.get(SEARCH_URL, params=params)
    items = response.json().get("items", [])
    return [item["id"]["videoId"] for item in items]

# Step 2: Fetch comments for each video ID
def get_comments(video_id, max_results=100):
    comments = []
    params = {
        "part": "snippet",
        "videoId": video_id,
        "maxResults": 100,
        "textFormat": "plainText",
        "key": API_KEY
    }

    while True:
        response = requests.get(COMMENT_URL, params=params)
        data = response.json()

        for item in data.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "video_id": video_id,
                "author": comment.get("authorDisplayName"),
                "text": comment.get("textDisplay"),
                "published_at": comment.get("publishedAt"),
                "like_count": comment.get("likeCount")
            })

        # Check for next page
        if "nextPageToken" in data and len(comments) < max_results:
            params["pageToken"] = data["nextPageToken"]
        else:
            break

    return comments

# Step 3: Run for keywords
keywords = [
    "TED talk burnout",
    "depression personal story",
    "social comparison mental health",
    "anxiety motivation",
    "stress management talk"
]

all_comments = []
for keyword in keywords:
    print(f"🔍 Searching videos for: {keyword}")
    video_ids = search_videos(keyword, max_results=3)
    for vid in video_ids:
        print(f"📹 Fetching comments for video: {vid}")
        comments = get_comments(vid, max_results=100)
        all_comments.extend(comments)

# Step 4: Save to JSON
output_dir = "/raw_data/youtube"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "youtube_comments.json")

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_comments, f, indent=2, ensure_ascii=False)

print(f"✅ Collected {len(all_comments)} comments. Saved to {output_file}")
