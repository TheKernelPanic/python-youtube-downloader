import pytube
import json
from slugify import slugify

with open('urls.json', 'r', encoding='utf-8') as file:
    urls = json.load(file)

for url in urls['video']:
    video_streams = pytube.YouTube(url).streams

    title = video_streams[0].title
    video_streams.get_lowest_resolution().download(
        output_path='video',
        filename='{}.mp4'.format(slugify(title))
    )

for url in urls['audio']:
    video_streams = pytube.YouTube(url).streams

    title = video_streams[0].title
    video_streams.filter(only_audio=True).first().download(
        output_path='audio',
        filename='{}.mp3'.format(slugify(title))
    )

