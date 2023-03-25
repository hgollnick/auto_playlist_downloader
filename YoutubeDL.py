import yt_dlp
from yt_dlp import YoutubeDL
import os.path
from os import path

ydl_opts = {
    'extract_flat': True,
    'dump_single_json': True,
    'outtmpl': 'C:/Users/henri/Documents/yt-dlp/%%(title)s.%%(ext)s'
}

PATH = "D:\Youtube\\{playlistTitle}"
URLS = ['https://www.youtube.com/playlist?list=PL_CXWO-cR7Cgz3Qy3s0fFijNKP-vbWydw']


def checkPlaylistFolderExistence(object):
    playlistTitle = object['title']
    playlistFolder = eval(f"f'{PATH}'")
    print(path.exists(playlistFolder))
     

with YoutubeDL(ydl_opts) as ydl:
        for URL in URLS:
            object = ydl.extract_info(URL, download=False)
            for jsn in object.get('entries'):
                checkPlaylistFolderExistence(object)
                videoUrl = jsn['url']
                print(videoUrl)
                ydl.download(videoUrl)
                
