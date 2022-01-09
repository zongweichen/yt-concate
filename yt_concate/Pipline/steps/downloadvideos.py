import ssl
from .step import Step
from yt_concate.settings import VIDEO_DIR
from pytube import YouTube


class DownLoadVideos(Step):
    def process(self, data, Input, utils):
        yt_set = set([found.yt for found in data])
        print("download videos:", len(yt_set))
        for yt in yt_set:
            url = yt.url
            if utils.check_video_filepath(yt):
                print(f"found existing  video file in {url} skipping")
                continue

            print("downloading", url)
            ssl._create_default_https_context = ssl._create_unverified_context
            YouTube(url).streams.first().download(output_path=VIDEO_DIR, filename=yt.id + ".mp4")
