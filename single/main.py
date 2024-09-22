from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=RB-RcX5DS5A"
save_path = "downloads"

yt = YouTube(url, on_complete_callback=on_progress)
print(f"Downloading: {yt.title}")

ys = yt.streams.get_audio_only()
ys.download(output_path=save_path, mp3=True)