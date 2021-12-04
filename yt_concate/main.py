from yt_concate.Pipline.steps.get_video_list import GetVideoList
from yt_concate.Pipline.steps.download_captions import DownLoadCaptions
from yt_concate.Pipline.pipeline import Pipeline
from yt_concate.Pipline.steps.preflight import Preflight
from yt_concate.utils import Utils


class Main:
    Input = {
        "CHANNEL_ID": "UCKSVUHI9rbbkXhvAXK-2uxA",
    }

    step = [
        Preflight(),
        GetVideoList(),
        DownLoadCaptions(),

        ]
    utils = Utils()
    p = Pipeline(step)
    p.run(Input, utils)


if __name__ == "__main__":
    Main()
