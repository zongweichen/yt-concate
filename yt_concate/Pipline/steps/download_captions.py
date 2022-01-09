import os
import time
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import TranscriptsDisabled, NoTranscriptFound
from yt_concate.Pipline.steps.step import Step



class DownLoadCaptions(Step):
    def process(self, data, Input, utils):
        start = time.time()
        for yt in data:
            print("downloading caption for", yt.id)
            if utils.check_caption_filepath(yt):
                print("found existing caption file", yt.url)
                continue

            try:
                captions = YouTubeTranscriptApi.get_transcript(yt.id)
                text_file = open(yt.caption_filepath, "w")

                for cap in captions:
                    print(cap, file=text_file)
                    text_file.close()
            except TranscriptsDisabled:
                print("caption can not found")
            except NoTranscriptFound:
                print("caption can not found")
        end = time.time()
        print("took", end - start, "seconds")
        return data

