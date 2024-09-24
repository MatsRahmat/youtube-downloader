import json
import os
from typing import TextIO

# path = "./testing-directory"

# def json_read(filename: str):
#     with open(filename) as f_in:
#         return json.load(f_in)

# if __name__ == "__main__":
#     jsonData = json_read("links2.json")
#     print(jsonData)

#                   

#             For creating folder


# try:
#     os.mkdir(path)
#     print("Success create folder")
# except FileExistsError:
#     print("Folder already exist")

# if not os.path.isdir(path):
#     print("Directory already exist")
# else:
#     print("Folder in not found")

# s = ""
# if s.strip():
#     print("Not empty")
# else:
#     print("Empty string")

# class A:
#     is_loop = True
#     @staticmethod
#     def main():
#         while(A.is_loop):
#             choosed = int(input("Pilih menu: "))
#             if choosed == 1:
#                 B.main()
                
# class B:
#     is_loop = True

#     @staticmethod
#     def main():
#         if B.is_loop == False:
#             B.is_loop = True
        
#         while(B.is_loop):
#             chois = input("Exit ? Y/N: ")
#             if chois.lower() == "y":
#                 B.is_loop = False


# def read_file(filename):
#     dirname_prefix = "links"
#     path = dirname_prefix + "/" + filename
#     try:
#         if not os.path.isdir(dirname_prefix):
#             os.mkdir(dirname_prefix)
        
#         with open(path, 'r') as file:
#             content = file.read()
#         return content.splitlines()
#     except Exception as e:
#         print(f"Something error: {e}")
        


# def generate_path(filename) -> str:
#     dirname_prefix = "links"
#     path = dirname_prefix + "/" + filename
#     return path

# def check_file_exist(path) -> bool:
#     try:
#         if os.path.exists(path):
#             return False
#         else:
#             return True
#     except Exception as e:
#         print(f"Someting error: {e}")
#         return False

# def write_list_to_file(data, filename):
#     with open(filename, "w") as file:
#         file.writelines(data)
#     print("Success write file")

# def create_newline(data: list[str]) -> list[str]:
#     result = []
#     for url in data:
#         url = url + "\n"
#         result.append(url)
#     return result

# def save_url_to_file(data):
#     prefix_name = "failed_url"
#     count_name = 0
#     path = generate_path(prefix_name)
#     while(True):
#         is_valid = check_file_exist(path + ".txt")
#         if is_valid == False:
#             print(f"path: {path}")
#             path = generate_path(prefix_name + f"-{count_name}")
#             count_name = count_name + 1
#         else:
#             print(f"Valid path: {path}")
#             break
#     # print(f"valid path is: {path}")
#     sanitize_url = creat_newline(data)
#     write_list_to_file(sanitize_url, path + ".txt")

class A:
    def __init__(self, data, prefix_name="failed_url"):
        self.prefix_name = prefix_name
        self.data = self.create_newline(data)
        self.count_name = 0
        self.path = self.generate_path(prefix_name)

        while(True):
            is_valid_name = self.check_file_exist(self.path + ".txt")
            if is_valid_name == False:
                print(f"Path: {self.path}")
                self.path = self.generate_path(self.prefix_name + f"-{self.count_name}")
                self.count_name = self.count_name + 1
            else:
                print(f"Valid name: {self.path}")
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
        print("Success write file")

    def create_newline(self, data: list[str]) -> list[str]:
        result = []
        for url in data:
            url = url + "\n"
            result.append(url)
        return result

list_url = ["https://youtube.com/watch?v=sniQm7pXJo0","https://youtube.com/watch?v=eA2cCQuWg6M"]
if __name__ == "__main__":
#    save_url_to_file(list_url)
    save = A(list_url)
    print(save.get_pathname())

