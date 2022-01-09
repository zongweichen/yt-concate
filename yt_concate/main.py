from yt_concate.Pipline.steps.get_video_list import GetVideoList
from yt_concate.Pipline.steps.initialize_yt import Initialize
from yt_concate.Pipline.steps.download_captions import DownLoadCaptions
from yt_concate.Pipline.pipeline import Pipeline
from yt_concate.Pipline.steps.read_caption import ReadCaption
from yt_concate.Pipline.steps.search import Search
from yt_concate.Pipline.steps.downloadvideos import DownLoadVideos
from yt_concate.Pipline.steps.preflight import Preflight
from yt_concate.Pipline.steps.postflight import Postflight
from yt_concate.utils import Utils


class Main:
    Input = {
        "CHANNEL_ID": "UCKSVUHI9rbbkXhvAXK-2uxA",
        "search_word": "incredible"
    }

    step = [
        Preflight(),
        GetVideoList(),
        Initialize(),
        DownLoadCaptions(),
        ReadCaption(),
        Search(),
        DownLoadVideos(),
        Postflight(),

        ]
    utils = Utils()
    p = Pipeline(step)
    p.run(Input, utils)


if __name__ == "__main__":
    Main()
