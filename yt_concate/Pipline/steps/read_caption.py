import os
from pprint import pprint
from yt_concate.Pipline.steps.step import Step
from yt_concate.settings import CAPTION_DIR


class ReadCaption(Step):

    def process(self, data, input, utils):
        data = {}
        for caption_file in os.listdir(CAPTION_DIR):
            with open(os.path.join(CAPTION_DIR, caption_file), "r") as f:
                captions = {}
                for line in f:
                    line = line.replace(":", ",")
                    line = line.replace("'", " ")
                    line = line.replace('"', " ")
                    line = line.split(",")
                    time = line[3]
                    caption_line = line[1]
                    captions[caption_line] = time
            data[caption_file] = captions
        pprint(data)
        return data






