import os
from dotenv import load_dotenv
import kaggle

# Load .env file to access Kaggle credentials
load_dotenv()

# Set Kaggle credentials from environment variables
os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')

# Define the dataset name
dataset_name = "elvis23/mental-health-conversational-data"  # Kaggle dataset name

# Define the output directory
output_dir = "/raw_data/kaggle"  # Adjust path as per your folder structure

# Download dataset
os.makedirs(output_dir, exist_ok=True)
kaggle.api.dataset_download_files(dataset_name, path=output_dir, unzip=True)

print(f"✅ Dataset '{dataset_name}' downloaded and extracted to {output_dir}")
