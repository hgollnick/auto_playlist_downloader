from yt_dlp import YoutubeDL
from os import path

PATH = "D:\Youtube\\{playlistTitle}"
VIDEO_PATH = 'C:/Users/henri/Documents/Test/{VIDEO_TITLE}.{VIDEO_EXT}';
URLS = ['https://www.youtube.com/playlist?list=PL_CXWO-cR7Cgz3Qy3s0fFijNKP-vbWydw']


def checkPlaylistFolderExistence(playlist):
    playlistTitle = playlist['title']
    playlistFolder = eval(f"f'{PATH}'")
    print(path.exists(playlistFolder))


ydl_opts = {
    'extract_flat': True,
    'dump_single_json': True
}


with YoutubeDL(ydl_opts) as ydl:
        for URL in URLS:
            playlist = ydl.extract_info(URL, download=False)
            for jsn in playlist.get('entries'):
                checkPlaylistFolderExistence(playlist)
                VIDEO_URL = jsn['url']
    
                video = ydl.extract_info(VIDEO_URL, download=False)

                string_with_ideographic_space = video['title']
                string_with_regular_space = string_with_ideographic_space.replace("\u3000", "　")

                playlistTitle = playlist['title']
                playlistFolder = eval(f"f'{PATH}'")

                print(path.exists(playlistFolder + "\\" + string_with_regular_space + "." + video['ext']))

                VIDEO_TITLE = video['title']
                

   