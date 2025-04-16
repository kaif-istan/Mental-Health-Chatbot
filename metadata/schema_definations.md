# 📄 Mental Health Dataset Schema Definition

**File:** `/mental_health_dataset/metadata/schema_definition.md`  
**Purpose:** This document defines the schema for structured data collected during the mental health and social media project.

---

## 🧩 Field Definitions

| Field Name        | Data Type     | Description                                                                 |
|-------------------|---------------|-----------------------------------------------------------------------------|
| `text`            | string        | Original post/message from social media or user input                       |
| `source`          | string        | Platform from which data was collected (e.g., Reddit, Twitter, Instagram)  |
| `label`           | string        | Categorized mental health issue (e.g., "Anxiety", "FOMO")                  |
| `severity_index`  | integer (0–5) | Subjective rating of severity (0 = low, 5 = very severe)                   |
| `timestamp`       | datetime      | Date and time of data collection or post publication                        |
| `language`        | string (ISO)  | Language code (e.g., `en` for English, `es` for Spanish)                    |
| `user_id`         | string        | Anonymized or hashed identifier for user (used for tracking longitudinal data) |

---

## 🧪 Example Records

### ✅ Example 1 — CSV format

```csv
text,source,label,severity_index,timestamp,language,user_id
"I constantly feel like I’m not doing enough even when I’m exhausted.","Twitter","Imposter Syndrome",4,"2025-04-15T17:22:00Z","en","user_1123"

### ✅ Example 2 — JSON format

{
  "text": "I’ve been seeing all my friends posting vacation photos and I feel like I’m missing out.",
  "source": "Instagram",
  "label": "FOMO",
  "severity_index": 3,
  "timestamp": "2025-04-14T10:03:21Z",
  "language": "en",
  "user_id": "user_0098"
}
