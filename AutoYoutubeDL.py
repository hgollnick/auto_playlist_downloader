import os

from yt_dlp import YoutubeDL
from os import path
from pathlib import Path

PATH = "D:\Youtube\\{playlistTitle}"
VIDEO_PATH = 'C:/Users/henri/Documents/Test/{VIDEO_TITLE}.{VIDEO_EXT}';
URLS = ['https://www.youtube.com/playlist?list=PL_CXWO-cR7Cgz3Qy3s0fFijNKP-vbWydw']


ydl_opts = {
    'extract_flat': True,
    'dump_single_json': True
}


with YoutubeDL(ydl_opts) as ydl:
        for URL in URLS:
            playlist = ydl.extract_info(URL, download=False)
            for jsn in playlist.get('entries'):
                playlistTitle = playlist['title']
                VIDEO_URL = jsn['url']

                video = ydl.extract_info(VIDEO_URL, download=False)

                VIDEO_TITLE = video['title']
                VIDEO_EXT = "." + video['ext']

                playlistFolder = eval(f"f'{PATH}'")
                
                if VIDEO_TITLE.replace('/','⧸') + VIDEO_EXT in os.listdir(playlistFolder):
                    print(VIDEO_TITLE)
                else:
                    print('not found' + VIDEO_TITLE)
   