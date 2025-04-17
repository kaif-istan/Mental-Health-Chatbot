# 🧠 Mental Health Dataset Collection & Curation

This repository focuses on collecting, curating, and preprocessing diverse mental health-related data from multiple sources (Twitter, forums, Kaggle datasets, etc.) to support research on mental health and phenomena like FOMO, anxiety, depression, and burnout.

---

## 📁 Repository Structure

MENTAL_HEALTH_DATASET/
│
├── config/
├── metadata/
├── processed_data/
│   ├── cleaned_data.csv
│   └── severity_index_data.json
│
├── raw_data/
│   ├── forums/
│   ├── kaggle/
│   ├── reddit/
│   ├── surveys/
│   ├── twitter/
│   └── youtube/
│
├── scripts/
│   ├── fetch_forums.py
│   ├── kaggle_downloader.py
│   ├── preprocess.py
│   ├── scrape_reddit.py
│   ├── scrape_twitter.py
│   └── scrape_youtube.py
│
├── .env
├── .gitignore
├── environment.yml
└── requirements.txt


---

## 📌 Project Goals

- 🗃 **Collect and unify mental health data** from:
  - Twitter (using Twitter API v2)
  - Mental health forums (e.g., PsychForums)
  - Public Kaggle datasets
  - Youtube comments
  - Reddit
  - etc.

- 🧹 **Preprocess and organize** the collected data for downstream NLP applications, including:
  - Chatbot fine-tuning for support conversations
  - Emotion and topic classification
  - FOMO and social media usage analysis

- 🔍 **Enable LLMs** and ML models to better understand mental health-related language and sentiment.

---

## 🔧 Tech Stack

- `Python 3.10+`
- `Tweepy` for Twitter scraping
- `BeautifulSoup` and `Requests` for forum scraping
- `Kaggle API` for downloading datasets
- `Pandas`, `JSON`, and `CSV` for data handling

---

## 📌 Status

- ✅ All website scraping implemented
- 🚧 Data preprocessing in progress

---

## 📬 Contact

Questions or contributions? Feel free to open an issue or PR or just send a mail to kaif85077@gmail.com!

---
