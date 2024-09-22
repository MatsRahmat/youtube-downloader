from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

class download_app:
    save_path = "downloads"
    is_loop = True
    menus = ('Single download','Bulk download','Playlist download')
    choosed_menu = ""
    @staticmethod
    def download_menu():
        while(download_app.is_loop):
            for index, value in enumerate(download_app.menus):
                print(f"{index} - {value}")

    @staticmethod
    def decisio():
        pass
    @staticmethod
    def single_download():
        url = input("Enter url video")
        if url != "":
            try:
                yt = YouTube(url, on_complete_callback=on_progress)
                print(f"Downloading: {yt.title}")

                ys = yt.streams.get_audio_only()
                ys.download(output_path=download_app.save_path, mp3=True)
                print("Donwload complete")
            except:
                print("Something error")
    @staticmethod
    def create_download_directory():
        if not os.path.isdir(Downlo)
