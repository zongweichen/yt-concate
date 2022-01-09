

from yt_concate.Pipline.steps.step import Step



class ReadCaption(Step):

    def process(self, data, input, utils):
        for yt in data:
            if not utils.check_caption_filepath(yt):
                continue
            with open(yt.caption_filepath, "r") as f:
                captions = {}
                for line in f:
                    line = line.replace(":", ",")
                    line = line.replace("'", " ")
                    line = line.replace('"', " ")
                    line = line.split(",")
                    time = line[3]
                    caption_line = line[1]
                    captions[caption_line] = time
            yt.captions = captions

        return data






