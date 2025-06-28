import yt_dlp
from yt_dlp import YoutubeDL
import os
from os import path

# Parameterized paths for better portability
DOWNLOAD_BASE_PATH = os.environ.get('YTDL_DOWNLOAD_PATH', r'D:\Youtube')
VIDEO_PATH_TEMPLATE = os.environ.get('YTDL_VIDEO_PATH', r'C:/Users/henri/Documents/Test/{VIDEO_TITLE}.{VIDEO_EXT}')
URLS = ['https://www.youtube.com/playlist?list=PL_CXWO-cR7Cgz3Qy3s0fFijNKP-vbWydw']


def ensure_playlist_folder_exists(playlist_title):
    playlist_folder = os.path.join(DOWNLOAD_BASE_PATH, playlist_title)
    if not os.path.exists(playlist_folder):
        os.makedirs(playlist_folder)
    return playlist_folder


def format_selector(ctx):
    """ Select the best video and the best audio that won't result in an mkv.
    NOTE: This is just an example and does not handle all cases """

    # formats are already sorted worst to best
    formats = ctx.get('formats')[::-1]

    # acodec='none' means there is no audio
    best_video = next(f for f in formats
                      if f['vcodec'] != 'none' and f['acodec'] == 'none')

    # find compatible audio extension
    audio_ext = {'mp4': 'm4a', 'webm': 'webm'}[best_video['ext']]
    # vcodec='none' means there is no video
    best_audio = next(f for f in formats if (
        f['acodec'] != 'none' and f['vcodec'] == 'none' and f['ext'] == audio_ext))

    # These are the minimum required fields for a merged format
    yield {
        'format_id': f'{best_video["format_id"]}+{best_audio["format_id"]}',
        'ext': best_video['ext'],
        'requested_formats': [best_video, best_audio],
        # Must be + separated list of protocols
        'protocol': f'{best_video["protocol"]}+{best_audio["protocol"]}'
    }


ydl_opts = {
    'extract_flat': True,
    'dump_single_json': True,
    'format': format_selector,
    'outtmpl': {'default': None},  # Will be set per video
}

with YoutubeDL(ydl_opts) as ydl:
    for URL in URLS:
        playlist = ydl.extract_info(URL, download=False)
        playlist_title = playlist['title'].replace('/', '_')
        playlist_folder = ensure_playlist_folder_exists(playlist_title)
        for jsn in playlist.get('entries'):
            VIDEO_URL = jsn['url']
            try:
                video = ydl.extract_info(VIDEO_URL, download=False)
            except Exception as e:
                print(f"Failed to extract video info: {VIDEO_URL}\nError: {e}")
                continue
            VIDEO_TITLE = video['title'].replace('/', '_')
            VIDEO_EXT = video['ext']
            outtmpl = VIDEO_PATH_TEMPLATE.format(VIDEO_TITLE=VIDEO_TITLE, VIDEO_EXT=VIDEO_EXT)
            ydl.params['outtmpl']['default'] = outtmpl
            try:
                ydl.download([VIDEO_URL])
            except Exception as e:
                print(f"Failed to download video: {VIDEO_TITLE}\nError: {e}")
