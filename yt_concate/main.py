from yt_concate.Pipline.steps.get_video_list import GetVideoList
from yt_concate.Pipline.pipeline import Pipeline


class Main:
    Input = {
        "CHANNEL_ID": "UCKSVUHI9rbbkXhvAXK-2uxA",
    }

    step = [
        GetVideoList(),
        ]
    p = Pipeline(step)
    p.run(Input)


if __name__ == "__main__":
    Main()
