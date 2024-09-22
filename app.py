from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import time

class App:
    is_loop = True
    menus = ('Donwload','Check Data')
    choosed_menu = ""

    @staticmethod
    def main_menu():
        while(App.is_loop):
            if not App.choosed_menu:
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
    is_loop = True
    menus = ('Single download','Bulk download','Playlist download', "Back to main menu")
    choosed_menu = ""

    @staticmethod
    def download_menu() -> bool:
        if Download.is_loop == False:
            Download.is_loop = True

        while(Download.is_loop):
            if not Download.save_path:
                input_save_path = input("Where the file will be saved?: ")
                if(input_save_path):
                    Download.save_path = input_save_path
                    Download.create_save_folder()

            if Download.choosed_menu:
                Download.decisio()
            else:
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
                pass
            case 2:
                print("Menu 2")
                pass
            case 3:
                print("Menu 3")
                pass
            case 4:
               Download.exitDownloadHandler()

    @staticmethod
    def exitDownloadHandler():
        Download.is_loop = False
        Download.choosed_menu = ""


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
    def single_download():
        url = input("Enter url video: ")
        if url:
            try:
                yt = YouTube(url, on_complete_callback=on_progress)
                print(f"Downloading: {yt.title}")

                ys = yt.streams.get_audio_only()
                ys.download(output_path=Download.save_path, mp3=True)
                print("Donwload complete")
                time.sleep(1.5)
            except:
                print("Something error")
       
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
    