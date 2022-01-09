import os
from yt_concate.settings import CAPTION_DIR
from yt_concate.settings import VIDEO_DIR
from yt_concate.settings import DOWNLOAD_DIR




class Utils:
    def __init__(self):
        pass

    def create_dir(self):
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        os.makedirs(CAPTION_DIR, exist_ok=True)
        os.makedirs(VIDEO_DIR, exist_ok=True)
    @staticmethod
    def check_caption_filepath(yt):
        filepath = yt.caption_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def get_videolist_filepath(self, channel_id):
        return os.path.join(DOWNLOAD_DIR, channel_id+".txt")

    def check_videolist_filepath(self, channel_id):
        path = self.get_videolist_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0
    @staticmethod
    def check_video_filepath(yt):
        filepath = yt.video_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0





