import os
import json
import re
import pandas as pd

RAW_PATHS = {
    "twitter": "D:/Projects/mental_health_dataset/raw_data/twitter/twitter_data_batch1.json",
    "reddit": "D:/Projects/mental_health_dataset/raw_data/reddit/reddit_posts.json",
    "forums": "D:/Projects/mental_health_dataset/raw_data/forums/psychforums.json",
    "kaggle": "D:/Projects/mental_health_dataset/raw_data/kaggle/intents.json",
    "youtube": "D:/Projects/mental_health_dataset/raw_data/youtube/youtube_comments.json"
}

def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)  # remove links
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    text = re.sub(r"\s+", " ", text).strip()  # remove extra whitespace
    return text

def process_and_combine(raw_paths):
    all_data = []

    for source, path in raw_paths.items():
        if not os.path.exists(path):
            print(f"Skipping {source}: file not found.")
            continue

        print(f"Loading from: {source}")
        entries = load_data(path)

        if source == "kaggle":
            intents = entries.get("intents", [])
            for intent in intents:
                for pattern in intent.get("patterns", []):
                    text = clean_text(pattern)
                    if len(text.split()) >= 3:
                        all_data.append({
                            "text": text,
                            "source": source,
                            "label": intent.get("tag", "Unknown"),
                            "severity_index": 0,
                            "timestamp": "",
                            "language": "en",
                            "user_id": ""
                        })

        elif source == "forums":
            for entry in entries:
                posts = entry.get("posts", [])
                for post in posts:
                    text = clean_text(post)
                    if len(text.split()) >= 10:
                        all_data.append({
                            "text": text,
                            "source": source,
                            "label": entry.get("category", "Unknown"),
                            "severity_index": 0,
                            "timestamp": "",
                            "language": "en",
                            "user_id": ""
                        })

        else:
            for entry in entries:
                text = clean_text(entry.get("text", ""))
                if len(text.split()) >= 10:
                    all_data.append({
                        "text": text,
                        "source": source,
                        "label": "Unlabeled",
                        "severity_index": 0,
                        "timestamp": entry.get("created_at", entry.get("timestamp", entry.get("published_at", ""))),
                        "language": entry.get("lang", "en"),
                        "user_id": str(entry.get("author_id", entry.get("user_id", entry.get("author", ""))))
                    })

    return pd.DataFrame(all_data)

if __name__ == "__main__":
    df = process_and_combine(RAW_PATHS)
    df.drop_duplicates(subset=["text"], inplace=True)

    os.makedirs("../processed_data", exist_ok=True)
    df.to_csv("../processed_data/cleaned_data.csv", index=False)

    print(f"Cleaned and saved {len(df)} entries.")
