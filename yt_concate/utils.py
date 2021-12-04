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
    def get_channel_id_from_url(url):
        return url.split("/watch?v=")[-1]

    def get_caption_filepath(self, url):
        return os.path.join(CAPTION_DIR, self.get_channel_id_from_url(url) + '.txt')

    def check_caption_filepath(self, url):
        path = self.get_caption_filepath(url)
        return os.path.exists(path) and os.path.getsize(path) > 0

    @staticmethod
    def get_videolist_filepath(channel_id):
        return os.path.join(DOWNLOAD_DIR, channel_id+".txt")

    def check_videolist_filepath(self, channel_id):
        path = self.get_videolist_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

