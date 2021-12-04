import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")


DOWNLOAD_DIR = "download_dir"

CAPTION_DIR = os.path.join("download_dir", "caption_dir")
VIDEO_DIR = os.path.join("download_dir", "video_dir")
