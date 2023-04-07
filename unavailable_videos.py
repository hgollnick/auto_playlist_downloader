import os

from yt_dlp import YoutubeDL

PATH = "D:\Youtube\\{playlistTitle}"
URLS = ['https://www.youtube.com/playlist?list=PL_CXWO-cR7Cgz3Qy3s0fFijNKP-vbWydw']


ydl_opts = {
    'extract_flat': True,
    'dump_single_json': True
}


with YoutubeDL(ydl_opts) as ydl:
    removed_videos = []
    for URL in URLS:
        playlist = ydl.extract_info(URL, download=False)
        for jsn in playlist.get('entries'):
            playlistTitle = playlist['title']
            VIDEO_URL = jsn['url']

            try:
                video = ydl.extract_info(VIDEO_URL, download=False)
            except:
                removed_videos.append(video['title'])
                print("Video unavailable. This video has been removed by the uploader")

            VIDEO_TITLE = video['title']
            VIDEO_EXT = "." + video['ext']

            playlistFolder = eval(f"f'{PATH}'")

            # if VIDEO_TITLE.replace('/', '⧸') + VIDEO_EXT not in os.listdir(playlistFolder):
                # print('Not found: ' + VIDEO_TITLE)
    print(removed_videos)