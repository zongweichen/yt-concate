
from yt_concate.Pipline.steps.step import Step
from yt_concate.model.found import Found


class Search(Step):
    def process(self, data, Input, utils):
        search_word = Input["search_word"]
        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)

        return found

