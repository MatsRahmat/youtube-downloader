from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
from pytubefix.exceptions import VideoUnavailable
import os
import time
import math

class App:
    is_loop = True
    menus = ('Donwload','Check Data', 'Exit')
    choosed_menu = ""

    @staticmethod
    def main_menu():
        while(App.is_loop):
            if not App.choosed_menu:
                Helper_app.print_info("Main Menu")
                for index, menu in enumerate(App.menus):
                    print(f"[{index + 1}] - {menu}")
                chois = Helper_app.isValidNumber(input("Select Menu: "))
                if(chois):
                    App.decision(chois)    
    
    @staticmethod
    def decision(valueInput):
        match(valueInput):
            case 1:
                # App.choosed_menu = "Download"
                Download.download_menu()
                App.choosed_menu = ""
            case 2:
                # App.choosed_menu = "Detail"
                print("Detail menu is under development, please be patien!")
                time.sleep(1.5)
                App.choosed_menu = ""
            case 3:
                App.is_loop = False
                App.choosed_menu = ""
            case _:
                print("Menu doesn't exist")

    @staticmethod 
    def show_choosed_menu():
        match(App.choosed_menu):
            case "Download":
                Download.download_menu()
                App.choosed_menu = ""
                # print("Choose download menu")
            case "Detail":
                print("Detail menu is under development, please be patien!")
                time.sleep(1.5)
                App.choosed_menu = ""



#                     [ DOWNDLOAD FILE CLASSES ]
class Download:
    save_path = ""
    links_dirname = "links"
    is_loop = True
    menus = ('Single download','Bulk download','Playlist download', "Back to main menu")
    choosed_menu = ""

    @staticmethod
    def download_menu() -> bool:
        if Download.is_loop == False:
            Download.is_loop = True

        while(Download.is_loop):
            if not Download.save_path:
                input_save_path = input("Where the file will be saved?. (Default 'Downloads'): ")
                if(input_save_path):
                    Download.save_path = input_save_path
                    Download.create_save_folder()
                else:
                    Download.save_path = "Downloads"
                    Download.create_save_folder()

            if Download.choosed_menu:
                Download.decisio()
            else:
                Helper_app.print_info("Download Menu")
                for index, value in enumerate(Download.menus):
                    print(f"[{index + 1}] - {value}")
                chois = Helper_app.isValidNumber(int(input("Select menu: ")))
                if(chois):
                    Download.choosed_menu = chois

    @staticmethod
    def decisio():
        match(Download.choosed_menu):
            case 1:
                Download.single_download()
                Download.choosed_menu = ""
            case 2:
                Download.bulk_download_menu()
                Download.choosed_menu = ""
            case 3:
                Download.playlist_download()
                Download.choosed_menu = ""
            case 4:
               Download.exitDownloadHandler()
            case _:
                print("Out of menu!")
                print("".center(40, "_"))

    @staticmethod
    def exitDownloadHandler():
        Download.is_loop = False
        Download.choosed_menu = ""

    @staticmethod
    def bulk_download_menu():
        bulk_menu = ("Manual input", "From file")
        for index, menu in enumerate(bulk_menu):
            print(f"[{index + 1}] - {menu}")
        choosed = int(input("Select download source: "))
        if choosed == 1:
            Download.bukl_download_from_input()
        elif choosed == 2:
            Download.bulk_download_from_file()
        elif choosed > 2:
            print("Out of menu")

    @staticmethod
    def create_save_folder():
        if not os.path.isdir(Download.save_path):
            print(f"Directory not found, creating {Download.save_path}")
            __creatingDir = Helper_app.crate_folder(Download.save_path)
            if not __creatingDir:
                print("Failed create directory for save folder, try again or different name")
                Download.save_path = ""
        else:
            print("Directory is already exist. and ready to use!")
     
    @staticmethod
    def download(url:str):
        def show_progress_bar(stream, chunk, _file_handle, bytes_remaining):
            current = ((stream.filesize - bytes_remaining) / stream.filesize)
            percent = f"{current * 100:.1f}"
            progress = int(50 * current)
            status = "█" * progress + "-" * (50 - progress)
            print(f" ↳ |{status}| {percent}%")
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            # yt = YouTube(url)
            # yt.register_on_progress_callback(show_progress_bar)
            print(f"Downloading: {yt.title}")

            ys = yt.streams.get_audio_only()
            ys.download(output_path=Download.save_path, mp3=True)
            print("\n")
            Helper_app.print_info("Donwload complete")
            time.sleep(1.5)
            return True
        except Exception as e:
            print(f"Something error: {e}")
            return False

    @staticmethod
    def playlist_download():
        print("Playlist download has much limitation, some video maybe unavailabel or cannot be downloaded!")
        url_input = input("Playlist url: ").strip()
        if url_input:
                unavailabel_url = []
                pl = Playlist(url=url_input)
                Helper_app.print_info(f"Downloading {pl.title}, created by: {pl.owner}")
                success_count = 0
                fail_count = 0
                for video in pl.videos:
                    print(f"Download: {video.title}")
                    try:
                        ys = video.streams.get_audio_only()
                        ys.download(mp3=True, output_path=Download.save_path)
                        success_count = success_count + 1
                    except VideoUnavailable as e:
                        print(f"Video unavaliable: {video.title}")
                        fail_count = fail_count + 1
                        unavailabel_url.append(video.watch_url)
                    except Exception as e:
                        print(f"Someting error {e}")
                        fail_count = fail_count + 1
                    print("".center(40, "-"))
                Helper_app.print_info(f"Done download!, success: {success_count} fail:{fail_count}")
                saved = Save_url_to_file(unavailabel_url)
                print(f"Unavailable video url saved in: {saved.path}.txt")
    @staticmethod
    def single_download():
        url = input("Enter url video: ").strip()
        if url:
            Download.download(url)
            
    @staticmethod
    def bukl_download_from_input():
        links = []
        success_count = 0
        fail_count = 0
        print("Type 'Done' when done inserting link")
        while(True):
            input_link = input("Insert link: ")
            if input_link.lower() == "done":
                break
            else:
                links.append(input_link)
        print(f"Result, total link = {len(links)}, download starting")
        for link in links:
            # print(link)
            link = link.strip()
            is_success = Download.download(link)
            if is_success == True:
                success_count = success_count + 1
            else:
                fail_count = fail_count + 1
        Helper_app.print_info(f"Done download!, success: {success_count} fail:{fail_count}")

    @staticmethod
    def bulk_download_from_file():
        filename = input("Insert file name: ").strip()
        if filename == "":
            return
        path = Download.links_dirname + "/" + filename
        success_count = 0
        fail_count = 0
        video_name = []
        try:
            if not os.path.isdir(Download.links_dirname):
                os.mkdir(Download.links_dirname)
            
            print("Getting link....")
            if Helper_app.check_file_exist(path + ".txt"):
                print("File not found!")
                return
            links = Helper_app.read_file_to_list(path)
            print(f"Start downloading {len(links)} url")
            for link in links:
                link = link.strip()
                is_success = Download.download(link)
                if is_success == True:
                    success_count = success_count + 1
                else:
                    fail_count = fail_count + 1
            Helper_app.print_info(f"Done download!, success: {success_count} fail:{fail_count}")
            return
        except Exception as e:
            print(f"Something error: {e}")
        
       
#                          [ HELPER CLASSES ]
class Helper_app:
    @staticmethod
    def isValidNumber(value):
        try:
            return int(value)
        except ValueError:
            return False
    @staticmethod
    def crate_folder(path) -> bool:
        try:
            os.mkdir(path)
            return True
        except FileExistsError:
            print("Failed create folder, folder already exist")
            return False

    @staticmethod
    def read_file_to_list(path):
        with open(path, "r") as file:
            content = file.read()
        return content.splitlines()
    @staticmethod
    def print_info(message):
        total_leng = 90
        content_leng = len(message)
        empty_modulus_message = content_leng % 8
        x =(total_leng - content_leng)
        a = x / 8
        b = a / 2
        total_tabulation = math.ceil(b)
        message_text = ""
        for i in range(total_tabulation):
            message_text = message_text + "\t"
        message_text = message_text + message

        hr_text = "".center(total_leng, "=")
        print(hr_text)
        print(message_text)
        print(hr_text)
    @staticmethod
    def check_file_exist(path):
        return os.path.exists(path)

class Save_url_to_file:
    def __init__(self, data, prefix_name="failed_url"):
        self.prefix_name = prefix_name
        self.data = self.create_newline(data)
        self.count_name = 0
        self.path = self.generate_path(prefix_name)

        while(True):
            is_valid_name = self.check_file_exist(self.path + ".txt")
            if is_valid_name == False:
                self.path = self.generate_path(self.prefix_name + f"-{self.count_name}")
                self.count_name = self.count_name + 1
            else:
                break
        self.write_list_to_file(self.data, self.path + ".txt")
    
    def get_pathname(self):
        return self.path + ".txt"

    def generate_path(self, filename) -> str:
        dirname_prefix = "links"
        path = dirname_prefix + "/" + filename
        return path
        
    def check_file_exist(self, path) -> bool:
        try:
            if os.path.exists(path):
                return False
            else:
                return True
        except Exception as e:
            print(f"Someting error: {e}")
            return False

    def write_list_to_file(self, data, filename):
        with open(filename, "w") as file:
            file.writelines(data)
        print("Success save file")

    def create_newline(self, data: list[str]) -> list[str]:
        result = []
        for url in data:
            url = url + "\n"
            result.append(url)
        return result
