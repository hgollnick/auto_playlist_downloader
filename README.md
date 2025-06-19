Here's a `README.md` file that documents the purpose, usage, and structure of your script(s) using `yt_dlp` to interact with YouTube playlists:

---

# 🎥 YouTube Playlist Video Checker & Downloader

This project provides two Python scripts that use [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) to interact with a YouTube playlist. It includes:

* **Downloader Script** – Downloads audio and video separately for higher quality and merges them.
* **Checker Script** – Detects unavailable (removed/private) videos in a playlist.

---

## 📁 Folder Structure

```text
.
├── downloader.py        # Main script to download videos
├── removed_checker.py   # Script to list unavailable/removed videos
├── README.md            # This file
```

---

## 💡 Requirements

* Python 3.7+
* [yt-dlp](https://github.com/yt-dlp/yt-dlp):
  Install with:

```bash
pip install -U yt-dlp
```

---

## 🔧 Configuration

Edit the following constants at the top of the scripts to match your environment:

```python
# Common to both scripts
URLS = ['<Your YouTube Playlist URL>']

# downloader.py specific
PATH = "D:\\Youtube\\{playlistTitle}"
VIDEO_PATH = 'C:/Users/<your-user>/Documents/Test/{VIDEO_TITLE}.{VIDEO_EXT}'
```

---

## ▶️ How to Use

### 1. 📥 Download Playlist Videos (Separate Audio/Video)

**File:** `downloader.py`

This script downloads each video with the best video and audio streams (not resulting in `.mkv`) and saves them to a user-defined directory.

```bash
python downloader.py
```

This script includes:

* Custom format selection (best audio/video combo)
* Auto-folder check for each playlist
* Download to custom paths using `outtmpl`

---

### 2. ❌ Check for Removed Videos

**File:** `removed_checker.py`

This script checks a playlist and prints out which videos are no longer available (removed/private).

```bash
python removed_checker.py
```

The script:

* Loads playlist entries in "flat" mode
* Attempts to extract metadata for each video
* Collects and prints the titles of missing videos

---

## ⚠️ Notes & Warnings

* Avoid using characters like `/` in filenames. They are sanitized in `VIDEO_TITLE.replace('/')`.
* Be careful with `eval(f"f'{...}'")` usage — it can be simplified.
* Make sure your folders (`D:\Youtube\{playlistTitle}`) exist or handle folder creation in the script.
* This implementation assumes all videos have valid audio/video streams in formats compatible for merging. Adjust `format_selector` if needed.

---

## ✅ Todo

* Add automatic folder creation if missing
* Improve error handling and logging
* Refactor `eval(f"f'...'")` into safer alternatives

---

## 🧑‍💻 License

MIT License

---
