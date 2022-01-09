
from yt_concate.Pipline.steps.step import Step
from yt_concate.model.yt import YT

class Initialize(Step):
    def process(self, data, Input, utils):
        return[YT(url) for url in data]
