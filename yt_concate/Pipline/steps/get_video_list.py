import urllib.request
import json
import ssl

from yt_concate.settings import API_KEY
from yt_concate.Pipline.steps.step import step


class GetVideoList(step):
    def process(self, data, Input):
        channel_id = Input["CHANNEL_ID"]
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY,
                                                                                                            channel_id)
        video_links = []
        url = first_url
        while True:
            ssl._create_default_https_context = ssl._create_unverified_context

            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])
            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break
        print(video_links)
        return video_links


