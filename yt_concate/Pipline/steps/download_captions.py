import os
import sys
import traceback
from youtube_transcript_api import YouTubeTranscriptApi
from yt_concate.Pipline.steps.step import Step
from yt_concate.settings import CAPTION_DIR


import time

class DownLoadCaptions(Step):
    def process(self, data, Input, utils):
        start = time.time()
        for url in data:
            print("downloading caption for", url)
            if utils.check_caption_filepath(url):
                print("found existing caption file", url)
                continue

            try:
                captions = YouTubeTranscriptApi.get_transcript(utils.get_channel_id_from_url(url))
                text_file = open(utils.get_caption_filepath(url), "w")

                for cap in captions:
                    print(cap, file=text_file)
                    text_file.close()
            except :
                print("caption can not found")
                continue
                text_file.close()
        end = time.time()
        print("took", end - start, "seconds")

