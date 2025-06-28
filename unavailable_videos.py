import os
from yt_dlp import YoutubeDL

DOWNLOAD_BASE_PATH = os.environ.get('YTDL_DOWNLOAD_PATH', r'D:\Youtube')
URLS = ['https://www.youtube.com/playlist?list=PL_CXWO-cR7Cgz3Qy3s0fFijNKP-vbWydw']

def ensure_playlist_folder_exists(playlist_title):
    playlist_folder = os.path.join(DOWNLOAD_BASE_PATH, playlist_title)
    if not os.path.exists(playlist_folder):
        os.makedirs(playlist_folder)
    return playlist_folder

ydl_opts = {
    'extract_flat': True,
    'dump_single_json': True
}

with YoutubeDL(ydl_opts) as ydl:
    removed_videos = []
    for URL in URLS:
        playlist = ydl.extract_info(URL, download=False)
        playlist_title = playlist['title'].replace('/', '_')
        playlist_folder = ensure_playlist_folder_exists(playlist_title)
        for jsn in playlist.get('entries'):
            VIDEO_URL = jsn['url']
            try:
                video = ydl.extract_info(VIDEO_URL, download=False)
            except Exception as e:
                print(f"Video unavailable: {VIDEO_URL}\nError: {e}")
                removed_videos.append(VIDEO_URL)
                continue
            VIDEO_TITLE = video['title'].replace('/', '_')
            VIDEO_EXT = "." + video['ext']
            # Uncomment below to check if file exists in playlist folder
            # if f"{VIDEO_TITLE}{VIDEO_EXT}" not in os.listdir(playlist_folder):
            #     print('Not found: ' + VIDEO_TITLE)
    print("Removed/unavailable videos:", removed_videos)