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


def read_file(filename):
    dirname_prefix = "links"
    path = dirname_prefix + "/" + filename
    try:
        if not os.path.isdir(dirname_prefix):
            os.mkdir(dirname_prefix)
        
        with open(path, 'r') as file:
            content = file.read()
        return content.splitlines()
    except Exception as e:
        print(f"Something error: {e}")
        
    
        
    

if __name__ == "__main__":
    result = read_file("link.txt")
    print(result)

